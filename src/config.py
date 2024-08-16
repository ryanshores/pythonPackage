import pathlib
import logging

PROJECT_DIR = pathlib.Path(__file__).parent.parent.resolve()
OUTPUT_DIR = PROJECT_DIR / "tmp"


def configure_logger():
    logging.basicConfig(level=logging.DEBUG,
                        filename=OUTPUT_DIR / "run.log",
                        filemode='w',
                        format='[%(levelname).1s] %(message)s -> %(name)s.%(funcName)s:%(lineno)d @ %(asctime)s',
                        datefmt='%m-%d.%H:%M:%S')

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(levelname).1s] %(message)s -> %(funcName)s:%(lineno)d')
    console.setFormatter(formatter)

    logging.getLogger('').addHandler(console)

    logging.info("Logging Configured")
