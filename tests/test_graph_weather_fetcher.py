from src.solar_weather_fetcher import SolarWeatherFetcher
import unittest


class TestSolarWeatherFetcher(unittest.TestCase):
    """ Class to contain unit tests for methods in the SolarWeatherFetcher class. """

    def test_get_graph_wind_data_returns_non_empty_data(self):
        data = SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json", "temperature")
        self.assertTrue(len(data) > 0)

    def test_get_graph_wind_data_invalid_link_returns_empty_data(self):
        data = SolarWeatherFetcher._get_solar_wind_data("https://services.swpc.noaa.gov/products/", "temperature")
        self.assertTrue(len(data) == 0)

    def test_fetch_valid_website_returns_non_empty_data(self):
        data = SolarWeatherFetcher.fetch_website_data("https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json")
        self.assertTrue(len(data) > 0)

    def test_fetch_invalid_link_returns_empty_data(self):
        data = SolarWeatherFetcher.fetch_website_data("https://services.swpc.noaa.gov/products/")
        self.assertTrue(len(data) == 0)