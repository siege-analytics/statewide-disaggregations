from python.utilities import *


def load_all_voterfiles_from_directory(target_directory):

    # loop through all states

    for COMPLETE_STATE in STATE_NAME_ABBREVIATION_FIPS_CODE:

        # set variables from the string

        STATE_NAME = COMPLETE_STATE[0]
        STATE_ABBREVIATION = COMPLETE_STATE[1]
        STATE_FIPS = COMPLETE_STATE[2]

        # look for a file that matches the known pattern

        target_file_string = VOTER_FILE.format(
            **{'state_abbreviation': STATE_ABBREVIATION, 'suffix': VOTER_FILE_SUFFIX})

        target_file = target_directory / target_file_string

        if target_file.is_file():
            logging.info("Found file: {target_file} \n".format(target_file=target_file))
            table_name = str(target_file.stem.lower())

            # https://medium.com/@apoor/quickly-load-csvs-into-postgresql-using-python-and-pandas-9101c274a92f
            try:
                engine = create_sqlalchemy_connection()
                row_number = 0
                for df in pd.read_csv(target_file, chunksize=10000, sep=VOTER_FILE_DELIMITER, dtype='str'):
                    logging.info("starting on row_num {row_number}".format(row_number=row_number))
                    df.to_sql(
                        table_name,
                        engine,
                        index=False,
                        if_exists='append'  # if the table already exists, append this data
                    )
                    row_number += 10000




            except Exception as e:
                logging.error(e)
        else:
            continue
    return True


def do_all_the_voter_file_loading():
    # load_all_voterfiles_from_directory(target_directory=VOTERS_TO_DO_SUBDIRECTORY)
    first_dict = {'state': 'Texas'}
    write_state_run_settings_to_file(first_dict)
    second_dict = {'state_abbreviation': 'TX'}
    write_state_run_settings_to_file(second_dict)


if __name__ == "__main__":
    logging.info("Step 4 load all voter_files to the database")
    do_all_the_voter_file_loading()
