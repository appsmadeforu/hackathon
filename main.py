import logging
import time

import boto3
import requests
import datetime


REGION = 'us-west-2'
PROJECT_NAME = 'Hackathon Mobile App Android'
DEVICE_POOL_NAME = 'HackathonPool'
RUN_TIMEOUT_SECONDS = 60 * 60
WEB_URL_TEMPLATE = 'https://us-west-2.console.aws.amazon.com/devicefarm/home#/mobile/projects/%s/runs/%s'


device_farm = boto3.client('devicefarm', region_name=REGION)
logger = logging.getLogger(__name__)


def get_project_arn(name):
    for project in device_farm.list_projects()['projects']:
        if project['name'] == name:
            return project['arn']
    raise KeyError('Could not find project %r' % name)


def get_device_pool(project_arn, name):
    for device_pool in device_farm.list_device_pools(arn=project_arn)['devicePools']:
        if device_pool['name'] == name:
            return device_pool['arn']
    raise KeyError('Could not find device pool %r' % name)


def _upload_presigned_url(url, file_path):
    with open(file_path, 'rb') as file_stream:
        result = requests.put(url, data=file_stream, headers={'content-type': 'application/octet-stream'})
        assert result.status_code == 200


def create_upload(project_arn, upload_type, name, file_path):
    logger.info('Uploading %s %r' % (upload_type, file_path))
    result = device_farm.create_upload(
        projectArn=project_arn,
        name=name,
        type=upload_type,
        contentType='application/octet-stream',
    )
    upload = result['upload']
    _upload_presigned_url(upload['url'], file_path)
    return upload['arn']


def schedule_run(project_arn, name, device_pool_arn, app_arn, test_package_arn):
    logger.info('Scheduling test run %r' % name)
    result = device_farm.schedule_run(
        projectArn=project_arn,
        appArn=app_arn,
        devicePoolArn=device_pool_arn,
        name=name,
        test={
            'type': 'INSTRUMENTATION',
            'testPackageArn': test_package_arn,
        }
    )
    run = result['run']
    return run['arn']


def _poll_until(method, arn, get_status_callable, success_statuses, timeout_seconds=180):
    check_every_seconds = 10 if timeout_seconds == RUN_TIMEOUT_SECONDS else 1
    start = time.time()
    while True:
        result = method(arn=arn)
        current_status = get_status_callable(result)
        if current_status in success_statuses:
            return result
        logger.info('Waiting for %r status %r to be in %r' % (arn, current_status, success_statuses))
        now = time.time()
        if now - start > timeout_seconds:
            raise StopIteration('Time out waiting for %r to be done' % arn)
        time.sleep(check_every_seconds)


def wait_for_upload(arn):
    return _poll_until(
        device_farm.get_upload,
        arn,
        get_status_callable=lambda x: x['upload']['status'],
        success_statuses=('SUCCEEDED', ),
    )


def wait_for_run(test_package_arn):
    result = _poll_until(
        device_farm.get_run,
        test_package_arn,
        get_status_callable=lambda x: x['run']['status'],
        success_statuses=('COMPLETED', ),
        timeout_seconds=RUN_TIMEOUT_SECONDS,
    )
    final_run = result['run']
    logger.info('Final run counts: %(counters)s' % final_run)
    return final_run['result'] == 'PASSED'


def get_run_web_url(project_arn, test_run_arn):
    project_arn_id = project_arn.split(':')[6]
    test_run_arid = test_run_arn.split('/')[1]
    return WEB_URL_TEMPLATE % (
        project_arn_id,
        test_run_arid,
    )


if __name__ == '__main__':
    logging.basicConfig(format='%(message)s')
    logger.setLevel(logging.INFO)
    project_arn = get_project_arn(PROJECT_NAME)
    logger.info('Project: %r' % project_arn)
    device_pool_arn = get_device_pool(project_arn, DEVICE_POOL_NAME)
    logger.info('Device pool: %r' % device_pool_arn)
    app_arn = create_upload(
        project_arn,
        'ANDROID_APP',
        'app-debug.apk',
        '/tmp/app-debug.apk',
    )
    wait_for_upload(app_arn)
    logger.info('App: %s' % app_arn)
    test_package_arn = create_upload(
        project_arn,
        'INSTRUMENTATION_TEST_PACKAGE',
        'app-debug-androidTest.apk',
        '/tmp/app-debug-androidTest.apk',
    )
    wait_for_upload(test_package_arn)
    logger.info('Test package: %s' % test_package_arn)
    test_run_arn = schedule_run(
        project_arn,
        name='Hackathon Android App Test cases'+"-"+(datetime.date.today().isoformat()),
        device_pool_arn=device_pool_arn,
        app_arn=app_arn,
        test_package_arn=test_package_arn,
    )
    logger.info('Scheduled test run %r' % test_run_arn)
    logger.info('View scheduled run at %s' % get_run_web_url(project_arn, test_run_arn))
    success = wait_for_run(test_run_arn)
    logger.info('Success')
