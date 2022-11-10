import boto3


def aws_client():
    devicefarm_client = boto3.client("devicefarm", region_name="us-west-2")
    testgrid_response = devicefarm_client.create_test_grid_url(
        projectArn="arn:aws:devicefarm:us-west-2:465255333558:testgrid-project:2a118269-8093-4428-82a7-2ac02e69f17f",
        expiresInSeconds=300)
    return testgrid_response['url']

