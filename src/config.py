import pathlib
import logging

PROJECT_DIR = pathlib.Path(__file__).parent.parent.resolve()
OUTPUT_DIR = PROJECT_DIR / "tmp"


def configure_logger():
    logging.basicConfig(level=logging.DEBUG,
                        filename=OUTPUT_DIR / "run.log",
                        filemode='w',
                        format='%(asctime)s - %(levelname)-8s - %(message)s',
                        datefmt='%Y/%m/%d %I:%M:%S %p')

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)-8s | %(message)s')
    console.setFormatter(formatter)

    logging.getLogger('').addHandler(console)

    logging.info("Logging Configured")
