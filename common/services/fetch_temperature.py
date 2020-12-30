import requests
from common.util.constants import Constants
from config import Config
import json


class TemperatureService():

    def function_get_city_temp(self):
        con = Constants()
        config = Config()
        parameters = {
            "appid": config.API_KEY
        }
        response = requests.get(con.open_weather_url + "?q=" + config.city_name, params=parameters)
        temp_data = response.json()['main']['temp']
        temp_data = temp_data - 273.15          # Convert temp Kelvin to Degree Celsius
        temp_data = str(round(temp_data, 2))
        return temp_data