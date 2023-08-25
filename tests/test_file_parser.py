from src.file_parser import FileParser
import unittest
import os


class TestFileParser(unittest.TestCase):
    """ Class for testing the NetCDF file extractor and parser"""

    def test_decompress_no_file(self):
        """ Test that the decompression method fails with an error if the file
        passed does not exist.
        """
        passed = False

        try:
            FileParser._decompress("non_existent.nc.gzip")
        except FileNotFoundError:
            passed = True

        self.assertTrue(passed)

    def test_decompress_non_compressed_file(self):
        """ Test that the decompression method fails with an error if the file
        passed is not a compressed file.
        """
        passed = False

        try:
            FileParser._decompress("test_data_file.nc")
        except Exception:
            passed = True

        self.assertTrue(passed)

    def test_decompress_working_gzip(self):
        """ Test that the decompression method works if a valid compressed gzip
        file is passed.
        """
        FileParser._decompress("test_data_file.nc.gzip")
        self.assertTrue(os.path.exists("test_data_file.nc"))
        os.remove("test_data_file.nc")

    def test_extract_data_broken_file(self):
        """ Test that the extraction fails with an error if the data file passed
        is not a gzipped netCDF file.
        """
        passed = False

        try:
            FileParser.extract_data("test_file_broken.txt")
        except FileNotFoundError:
            passed = True

        self.assertTrue(passed)

    def test_extract_data_non_ncdf(self):
        """ Test that the method fails with an error if the file passed is not
        a valid netCDF file.
        """
        passed = False

        try:
            FileParser.extract_data("test_file_broken.txt.gz")
        except FileNotFoundError:
            passed = True

        self.assertTrue(passed)

    def test_extract_data_working_file(self):
        """ Test that the method works when passed a valid gzipped netCDF file.
        """
        FileParser.extract_data("test_data_file.nc.gzip")
        self.assertTrue(os.path.exists("test_data_file.nc"))
        os.remove("test_data_file.nc")
