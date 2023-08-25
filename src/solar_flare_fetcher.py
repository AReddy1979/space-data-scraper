from bs4 import BeautifulSoup
import requests
import json
import time


class SolarFlareFetcherSWL:
    """ Class for fetching solar flare activity from spaceweatherlive
    """

    @staticmethod
    def fetch_website_data() -> list:
        """ Requests the HTML content from the spaceweatherlive website containing the current and highest solar flare
        classifications for the past 24 and 72 hours.

         Returns:
             lst: a list of each minute of solar weather data (time, density, speed, temperature) for the last 24 hours
             """

        url = "https://www.spaceweatherlive.com/includes/live-data.php?object=solar_flare_3d&lang=EN"

        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, br"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 403:
            print("Updating data...")

        while response.status_code == 403:
            time.sleep(5)
            response = requests.get(url, headers=headers)

        content = BeautifulSoup(response.content, "html.parser")
        flare_activity_json = json.loads(content.text)

        current_flare = flare_activity_json["val"].strip("</div>")
        max_flare_24_hours = flare_activity_json["val24"].strip("</div>")
        max_flare_72_hours = flare_activity_json["val72"].strip("</div>")

        return [current_flare, max_flare_24_hours, max_flare_72_hours]

    @staticmethod
    def format_website_data() -> str:
        """ Converts the solar flare data from spaceweatherlive into a more readable string

        Returns:
            formatted_str: string containing the data formatted in a readable way
    """

        flare_data = SolarFlareFetcherSWL.fetch_website_data()

        formatted_str = \
            "The current solar flare class according to Spaceweatherlive is: " + flare_data[0] + \
            "\n The largest solar flare class in the past 24 hours is: " + flare_data[1] + \
            "\n The largest solar flare class in the past 72 hours is: " + flare_data[2]

        return formatted_str


class SolarFlareFetcherNOAA:
    @staticmethod
    def fetch_website_data() -> list:

        url = "https://services.swpc.noaa.gov/json/goes/primary/xray-flares-latest.json"

        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, br"
        }

        response = requests.get(url, headers=headers)

        flare_activity_json = json.loads(response.content)[0]

        current_flare = flare_activity_json["current_class"]
        flare_event_begin = flare_activity_json["begin_class"]
        flare_event_max = flare_activity_json["max_class"]
        flare_event_end = flare_activity_json["end_class"]

        return [current_flare, flare_event_begin, flare_event_max, flare_event_end]

    @staticmethod
    def format_website_data() -> str:

        flare_data = SolarFlareFetcherNOAA.fetch_website_data()

        formatted_str = "The current solar flare class according to NOAA is: " + flare_data[0]

        if flare_data[1] == "":
            return formatted_str

        elif flare_data[2] == "":
            formatted_str = formatted_str + \
                            "\n A solar flare event is ocurring." + \
                            "\n The solar flare is beginning as class: " + flare_data[1]

        else:
            formatted_str = formatted_str + \
                            "\n A recent solar flare event has occurred." + \
                            "\n The solar flare begun as class: " + flare_data[1] + \
                            "\n It peaked at: " + flare_data[2] + \
                            "\n The ended as: " + flare_data[3]

        return formatted_str
