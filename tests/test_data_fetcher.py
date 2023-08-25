from src.data_fetcher import DataFetcher
import unittest
import datetime
import requests
import os


class TestDataFetcher(unittest.TestCase):
    """ Class to contain unit tests for methods in the DataFetcher class. """

    def test_format_date_double_digit_day_and_month(self):
        """ Test if the method can format dates with double-digit month and day values.
        """
        test_date = datetime.date(2020, 12, 20)
        formatted_date = DataFetcher._format_date(test_date)

        self.assertEqual(len(formatted_date), 8)
        self.assertEqual(formatted_date, "20201220")

    def test_format_date_single_digit_month(self):
        """ Test if the method can format dates with single-digit month values by adding
        a leading zero to the month.
        """
        test_date = datetime.date(2020, 3, 17)
        formatted_date = DataFetcher._format_date(test_date)

        self.assertEqual(len(formatted_date), 8)
        self.assertEqual(formatted_date, "20200317")

    def test_format_date_single_digit_day(self):
        """ Test if the method can format dates with single-digit day values by adding
        a leading zero to the day.
        """
        test_date = datetime.date(2020, 10, 5)
        formatted_date = DataFetcher._format_date(test_date)

        self.assertEqual(len(formatted_date), 8)
        self.assertEqual(formatted_date, "20201005")

    def test_format_date_single_digit_day_and_month(self):
        """ Test if the method can format date with both single-digit day values and
        single-digit month values by adding leading a leading zero to both.
        """
        test_date = datetime.date(2020, 6, 8)
        formatted_date = DataFetcher._format_date(test_date)

        self.assertEqual(len(formatted_date), 8)
        self.assertEqual(formatted_date, "20200608")

    def test_build_data_directory_url_double_digit_month(self):
        """ Test that the method can create the correct URL for the directory containing
        the desired data files with a double-digit month.
        """
        test_date = datetime.date(2020, 12, 30)
        directory_url = DataFetcher._build_data_directory_url(test_date)

        self.assertEqual(directory_url, "https://www.ngdc.noaa.gov/dscovr/data/2020/12/")

    def test_build_data_directory_url_single_digit_month(self):
        """ Test that the method can create the correct URL for the directory containing
        the desired dat files with a single-digit month value.
        """
        test_date = datetime.date(2020, 6, 22)
        directory_url = DataFetcher._build_data_directory_url(test_date)

        self.assertEqual(directory_url, "https://www.ngdc.noaa.gov/dscovr/data/2020/06/")

    def test_build_data_directory_url_valid_url(self):
        """ Test if the method returns a valid URL that can be requested with a non-404
        response code.
        """
        test_date = datetime.date(2020, 12, 30)
        directory_url = DataFetcher._build_data_directory_url(test_date)

        response_status = requests.get(directory_url).status_code
        self.assertTrue(response_status < 400)

    def test_find_file_url_returns_url(self):
        """ Test that the method returns a valid URL that can be requested with a non-404
        response code.
        """
        test_date = datetime.date(2020, 12, 30)
        directory_url = DataFetcher._find_file_url(test_date)

        response_status = requests.get(directory_url).status_code
        self.assertTrue(response_status < 400)

    def test_find_file_url_fails_safely(self):
        """ Test if there is no file found that the method throws an exception by looking for
        a file with a date one year from now (doesn't exist). """

        today_date = datetime.date.today()
        test_date = datetime.date(today_date.year + 1, today_date.month, today_date.day)

        try:
            directory_url = DataFetcher._find_file_url(test_date)
        except FileNotFoundError:
            self.assertTrue(True)
            return
        self.assertTrue(False)

    def test_fetch_file_returns_filename(self):
        """ Test that the method returns the correct filename based on the input date.
        """
        test_date = datetime.date(2020, 3, 17)
        filename = DataFetcher.fetch_file(test_date)

        self.assertEqual(filename, "20200317.nc.gz")
        os.remove("20200317.nc.gz")

    def test_fetch_file_creates_data_file(self):
        """ Test that the method creates a file in the filesystem with the correct name
        based on the input date.
        """
        test_date = datetime.date(2020, 3, 17)
        filename = DataFetcher.fetch_file(test_date)

        self.assertTrue(os.path.exists("./" + filename))
        self.assertEqual(filename, "20200317.nc.gz")
        os.remove("20200317.nc.gz")
