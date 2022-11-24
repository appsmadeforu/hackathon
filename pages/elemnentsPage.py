from libraries.SeleniumWrappers import SeleniumWrappers



class ElementsPage(SeleniumWrappers):

    page_title = ("et_pb_menu__logo", "class")
    tb_name = ("et_pb_contact_name_0", "id")
    tb_email = ("et_pb_contact_email_0", "id")
    button_email = ("et_pb_contact_submit", "class")
    radio_button_male = ("//*[@name='gender' and @value='male']", "xpath")
    checkbox_bike = ("//*[@type='checkbox' and @value='Bike']", "xpath")
    checkbox_car = ("//*[@type='checkbox' and @value='Car']", "xpath")

    def check_page_title(self):
        if self.get_element(*self.page_title):
            # actual_tile = self.get_element(*self.page_title).text
            actual_page_title = self.get_page_title()
            print("actual_page_title=" + actual_page_title)
            self.assert_two_values(actual_page_title, "Simple HTML Elements For Automation - Ultimate QA4546")

    def verfiy_text_boxes(self):
        if self.get_element(*self.tb_name):
            self.input_element_text("TestName", *self.tb_name)
            # self.get_element(*self.tb_name_new).send_keys("Test_Name")
            print("text box name - value entered")
        if self.get_element(*self.tb_email):
            self.input_element_text("TestEmail", *self.tb_email)
            # self.get_element(*self.tb_name_new).send_keys("Test_Name")
            print("text box Email - value entered")

    def verify_button(self):
        if self.get_element(*self.button_email):
            self.click_button(*self.button_email)
            print("Button Clicked")

    def verify_radio_button(self):
        if self.get_element(*self.radio_button_male):
            self.select_radio_button(*self.radio_button_male)

    def verify_check_boxes(self):
        if self.get_element(*self.checkbox_bike):
            self.select_checkbox_byflag(True, *self.checkbox_bike)
            self.select_checkbox_byflag(True, *self.checkbox_car)
            self.select_checkbox_byflag(False, *self.checkbox_car)
