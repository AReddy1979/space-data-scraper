import datetime
import requests
import string


class DataFetcher:
    """ Class for fetching the data that comes from the NOAA website.
    """

    @staticmethod
    def _format_date(file_date: datetime.date) -> string:
        """ Format the datetime.date object passed to take the following form as a string:
                <4-digit-year><2-digit-month><2-digit-day>
        Args:
            file_date: datetime.date object to be formatted
        Returns:
            formatted_date: a string of the form described above
        """
        formatted_date = ""
        formatted_date += str(file_date.year)

        if file_date.month < 10:
            formatted_date += "0"
        formatted_date += str(file_date.month)

        if file_date.day < 10:
            formatted_date += "0"
        formatted_date += str(file_date.day)

        return formatted_date

    @staticmethod
    def _build_data_directory_url(file_date: datetime.date) -> string:
        """ Build the name of the directory that the date file will be in on the NOAA website.
        Args:
            file_date: The date that the data was recorded for the file we are looking for
        Returns:
            directory_url: A URL to the directory containing the data file we want
        """
        directory_url = "https://www.ngdc.noaa.gov/dscovr/data/"
        directory_url += str(file_date.year) + "/"
        if file_date.month < 10:
            directory_url += "0"
        directory_url += str(file_date.month) + "/"

        return directory_url

    @staticmethod
    def _find_file_url(file_date: datetime.date) -> string:
        """ Find the URL for the data file for the day that is specified on the NOAA site. We must
            scan the HTML of the page to find the file. Each file has a start time, end time, and
            post time. The start and end times are always 000000 and 595959 respectively, but the
            post time is unknown, so we must scan the webpage for the file so it can be downloaded.

            The file URL will be of the format (with 4-digit years and 2-digit months and days):

                https://www.ngdc.noaa.gov/dscovr/data/<year>/<month>/oe_fc1_dscovr_s<year><month><day>
                000000_e<year><month><day>235959_p<year><month><day><6-digit-time>_pub.nc.gz

        Args:
            file_date: construct the file name and path
        Returns:
            url_string
        """
        url_string = DataFetcher._build_data_directory_url(file_date)

        file_name_start = "oe_fc1_dscovr" + "_s" + DataFetcher._format_date(file_date) + "000000" \
                          + "_e" + DataFetcher._format_date(file_date) + "235959" + "_p"

        file_name_end = ""

        for page_line in requests.get(url_string).iter_lines(decode_unicode=True):
            if file_name_start in page_line:
                for i in range(0, len(page_line) - 2):
                    if page_line[i] == "_" and page_line[i + 1] == "p":
                        file_name_end += page_line[i + 2: i + 26]
                        break

        if len(file_name_end) == 0:
            raise FileNotFoundError("The data file for that date does not exist")

        url_string += file_name_start + file_name_end

        return url_string

    @staticmethod
    def fetch_file(file_date: datetime.date) -> string:
        """ Returns a response from the website when making a GET request for a data file.
        Args:
            file_date: The date for which the data file was generated by NOAA and the one which
                        will be fetched from the NOAA website
        Returns:
            compressed_data_filename: The name of the compressed data file that was downloaded
        """
        response = requests.get(DataFetcher._find_file_url(file_date), stream=True)
        compressed_data_filename = DataFetcher._format_date(file_date) + ".nc.gz"

        data_file = open(compressed_data_filename, "wb")

        for chunk in response.iter_content(chunk_size=128):
            data_file.write(chunk)

        data_file.close()

        return compressed_data_filename
