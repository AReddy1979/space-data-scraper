import requests
import string
from bs4 import BeautifulSoup
import ast


class SolarWeatherFetcher:
    """ Class for fetching the solar weather data that comes from the NOAA website.
    """

    @staticmethod
    def fetch_website_data(url: string) -> list:
        """ Requests the HTML content from the NOAA website containing the data for solar weather in the last 24 hours
        Args:
            url: the url that we want to fetch
        Returns:
            lst: a list of each minute of solar weather data (time, density, speed, temperature) for the last 24 hours
        """
        website = requests.get(url)
        content = str(BeautifulSoup(website.content, 'html.parser'))
        lst = []

        content = content.replace('null', "\"0\"")
        
        try:
            lst = ast.literal_eval(content)
        except SyntaxError:
            
            lst = []

        return lst

    @staticmethod
    def format_website_data() -> string:
        """ Gets the list of solar weather data from the NOAA website and converts it into a more readable string

        Returns:
            formatted_str: string containing the data formatted in a readable way
        """

        content = SolarWeatherFetcher.fetch_website_data("")
        content[0][1] = 'density (1/cm^3)'
        content[0][2] = 'speed (km/s)'
        content[0][3] = 'temperature (K)'

        formatted_str = ""

        for data in content:
            formatted_str = formatted_str + '\n' + str(data)

        return formatted_str

    @staticmethod
    def _get_solar_wind_data(url: str, col_name: str) -> list:
        """
        Pages of data on the NOAA website contain multiple types of numerical data which are grouped into different
        columns. (i.e. Column 1 is timestamp, Column 2 is density, etc.)
        This function retrieves the column of data specified by col_nam, so it can be used for plotting.
        Args:
            url: The url to the website where the data is located.
            col_name: The column name of the column of data that is to be used.
        Returns:
            A list containing the values retrieved from the column of the data that is specified by col_name
        """
        solar_weather_data = SolarWeatherFetcher.fetch_website_data(url)
        data_size = len(solar_weather_data)
        plot_data = (data_size - 1) * [0]

        if (data_size > 0):
            col = solar_weather_data[0].index(col_name)

        if (col_name == "time_tag"):
            for index in range(1, data_size):
                plot_data[index - 1] = solar_weather_data[index][col]

        else:
            for index in range(1, data_size):
                plot_data[index - 1] = float(solar_weather_data[index][col])

        return plot_data

