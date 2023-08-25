from src.solar_flare_fetcher import SolarFlareFetcherNOAA
from src.solar_flare_fetcher import SolarFlareFetcherSWL
import unittest


class TestSolarFlareFetcher(unittest.TestCase):
    """ Class to contain unit tests for methods in the SolarWeatherFetcher class. """

    def test_noaa_get_solar_flare_data_returns_non_empty_data(self):
        data = SolarFlareFetcherNOAA.fetch_website_data()
        self.assertTrue(len(data) > 0)

    def test_swl_get_solar_flare_data_returns_non_empty_data(self):
        data = SolarFlareFetcherSWL.fetch_website_data()
        self.assertTrue(len(data) > 0)
