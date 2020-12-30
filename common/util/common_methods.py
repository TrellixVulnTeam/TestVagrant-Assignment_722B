from selenium import webdriver
import pytest
from common.object_repository.ndtv_home import NDTVHome
from common.util.constants import Constants
from common.services.fetch_temperature import TemperatureService
from config import Config
import time
from common.custom_exceptions.temp_range_error import TempRangeError, TempInRange, TempOutOfRange


class CommonMethods():



    def test_navigate_to_weather_map(self, driver):

        ndtv_obj_repo = NDTVHome()
        con = Constants()
        driver.get(con.NDTV_url)

        btn_latest = driver.find_element_by_xpath(ndtv_obj_repo.link_latest)
        btn_latest.click()

        link_section = driver.find_element_by_xpath(ndtv_obj_repo.btn_section)
        link_section.click()

        link_weather = driver.find_element_by_xpath(ndtv_obj_repo.link_weather)
        link_weather.click()

    def function_is_present(self, driver, element, elementName):
        obj_element = driver.find_element_by_xpath(element)
        self.function_highlight_element(obj_element)
        print(elementName + " is Present")

    def function_highlight_element(self, element):
        """Highlights (blinks) a Selenium Webdriver element"""
        driver = element._parent

        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
        original_style = element.get_attribute('style')
        apply_style("background: yellow; border: 2px solid green;")
        time.sleep(.3)
        apply_style(original_style)

    def function_compare_temperature(self, ui_temp, api_temp):
        config = Config()
        temp_range_allowed = float(config.range_variation_allowed)
        temp_difference = float(ui_temp) - float(api_temp)
        try:
            if temp_difference <= temp_range_allowed:
                print("The temperature matches")
            else:
                print("The does not match temperature matches")
                raise TempOutOfRange
        except TempOutOfRange as error:
            print('TempOutOfRange Exception occurred: ', error.msg)
            pytest.fail(error.msg)