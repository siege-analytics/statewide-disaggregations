#!/usr/bin/env python3

__author__ = 'Dheeraj Chand'
__copyright__ = 'Copyright 2019, Graham'
__credits__ = ['Alex Leith']
__version__ = '0.1.2'
__maintainer__ = 'Dheeraj Chand'
__email__ = 'Dheeraj Chand'
__status__ = 'Dev'

from settings import *
import logging
import pathlib
import sys

logging.basicConfig(level=logging.INFO)





def download_census_shapefiles():
    for census_year in CENSUS_YEARS:

        for geography, parameters in CENSUS_GEOGRAPHIES_TO_DOWNLOAD.items():

            # 1 Create a directory for the target geography

            info_message = "Working on {year}:{geography}, which is {file_type}".format(**{'year': census_year,
                                                                                           'geography': geography,
                                                                                           'file_type': parameters[
                                                                                               'PATTERN']})

            logging.info(info_message)
            new_geography_directory = pathlib.Path(CENSUS_SUBDIRECTORY) / census_year / geography
            pathlib.Path(new_geography_directory).mkdir(parents=True, exist_ok=True)
            logging.info("Found or created a directory for: {path}".format(**{'path': str(new_geography_directory)}))

            try:

                if parameters["PATTERN"] == 'SINGLE':

                    remote_zipfile = parameters['URL'].format(**{'year': census_year})
                    local_zipfile_name = remote_zipfile.split('/')[-1]
                    local_zipfile_path = str(pathlib.Path(new_geography_directory) / local_zipfile_name)

                    info_message = "Remote = {remote_zipfile} \n File Name To Save = {local_zipfile_name} \n Local Path = {local_zipfile_path}".format(
                        **{'remote_zipfile': remote_zipfile,
                           'local_zipfile_name': local_zipfile_name,
                           'local_zipfile_path': local_zipfile_path}
                    )

                    logging.info(info_message)

                    download_file(remote_zipfile, local_zipfile_path)

                # The geography will have multiple files to be downloaded based on statefips
                else:

                    for statefips in FIPS_STATES_TO_DOWNLOAD:
                        statefips = "{:02d}".format(statefips)
                        remote_zipfile = parameters['URL'].format(**{'year': census_year, 'statefips': statefips})
                        local_zipfile_name = remote_zipfile.split('/')[-1]
                        local_zipfile_path = str(pathlib.Path(new_geography_directory) / local_zipfile_name)

                        info_message = "Remote = {remote_zipfile} \n File Name To Save = {local_zipfile_name} \n Local Path = {local_zipfile_path}".format(
                            **{'remote_zipfile': remote_zipfile,
                               'local_zipfile_name': local_zipfile_name,
                               'local_zipfile_path': local_zipfile_path}
                        )

                        logging.info(info_message)

                        download_file(remote_zipfile, local_zipfile_path)

            except Exception as e:

                error_message = ("There was an error: {e}".format(**{'e': e}))
                logging.error(error_message)
                sys.exit()


if __name__ == "__main__":
    logging.info("Step 2 fetch the Census TIGER shapefiles")
    download_census_shapefiles()
