__author__ = 'Dheeraj Chand'
__copyright__ = 'Copyright 2019, Graham'
__credits__ = ['Alex Leith']
__version__ = '0.1.2'
__maintainer__ = 'Dheeraj Chand'
__email__ = 'Dheeraj Chand'
__status__ = 'Dev'

from utilities import *
from settings import *
import logging
import pathlib

def make_required_paths(paths_collection):

    for rp in paths_collection:
        try:
            message = "Currently working on {task}".format(**{'task': str(rp)})
            logging.info(message)
            print(message)
            pathlib.Path(rp).mkdir(parents=True, exist_ok=True)

        except Exception as e:
            message = "Fatal exception: {e}".format(**{'e': e})
            logging.error(message)
            sys.exit(0)

if __name__ == "__main__":
    logging.info("Step 1: create download paths")
    make_required_paths(REQUIRED_PATHS)
