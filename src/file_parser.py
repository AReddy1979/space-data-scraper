import gzip
import netCDF4
import string


class FileParser:
    """ Class for processing the files that are downloaded from the NOAA website. They
    need to be decompressed and the NetCDF (.nc) file needs to be parsed.
    """

    @staticmethod
    def _decompress(data_filename: string) -> string:
        """ Decompress the file that is passed as and argument to get the NetCDF that's inside.
        Args:
            data_filename: The name of the compressed Gzip (.gz) file that we want to decompress
        Returns:
            nc_filename: The name of the newly created netCDF data file
        """
        nc_file = gzip.open(data_filename)

        # Remove the ".gz" from the end of the filename and open the destination file
        nc_filename = data_filename[0: len(data_filename) - 3]
        nc_file = open(nc_filename, "wb")

        # Open the gzip file and write the contents to the destination ".nc" file
        data_file = gzip.open(data_filename, "rb")
        data_file_contents = data_file.read()
        nc_file.write(data_file_contents)

        data_file.close()
        nc_file.close()

        return nc_filename

    @staticmethod
    def extract_data(compressed_data_filename: string) -> netCDF4.Dataset:
        """ Extract the data from the compressed data file received from the NOAA website.
        Args:
            compressed_data_filename: The name of the compressed data file that the data will be extracted from
        Returns:
            nc_data: Data in the netCDF format
        """
        nc_data_filename = FileParser._decompress(compressed_data_filename)
        nc_data = netCDF4.Dataset(filename=nc_data_filename, mode="r", format="NETCDF3_CLASSIC")

        return nc_data
