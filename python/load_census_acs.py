from utilities import *
import string
from inflection import parameterize

def load_all_acs_from_directory(target_directory):
    try:
        for zipped_acs_file in target_directory.glob('**/*.zip'):
            logging.info("Currently working on {zipped_acs_file}".format(**{'zipped_acs_file': zipped_acs_file}))

            name_of_new_dir_for_unzip = zipped_acs_file.stem
            path_for_new_dir_for_unzip = zipped_acs_file.parent

            # ensure that the file extracted correctly
            new_acs_path_of_files = unzip_file_to_its_own_directory(zipped_acs_file)
            acs_table_name_prefix = parameterize(str(name_of_new_dir_for_unzip))
            if new_acs_path_of_files:
                try:
                    glob_pattern = "**/*.{ACS_FILE_SUFFIX}".format(**{'ACS_FILE_SUFFIX': ACS_FILE_SUFFIX})
                    for acs_file in new_acs_path_of_files.glob(glob_pattern):
                        usable_acs_file_name = parameterize(str(acs_file.stem))
                        table_name = "{acs_table_name_prefix}_{usable_acs_file_name}".format(
                            **{'acs_table_name_prefix': acs_table_name_prefix,
                               'usable_acs_file_name': usable_acs_file_name})
                        logging.info("Table name for {acs_file} is {table_name}".format(
                            **{'acs_file': acs_file, 'table_name': table_name}))
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    logging.error(exc_type, fname, exc_tb.tb_lineno)

    except Exception as e:
        error_message = "There was an error: {e}".format(**{'e': e})
        logging.info(error_message)
        return False


def do_all_the_voter_file_loading():
    load_all_acs_from_directory(target_directory=ACS_SUBDIRECTORY)


if __name__ == "__main__":
    logging.info("Step 5 load all Census ACS Files to the database")
    do_all_the_voter_file_loading()
