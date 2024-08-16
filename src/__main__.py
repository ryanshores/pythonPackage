import config
import logging
import writeScores
from src.writeScores import logger

LOGFILE_DIR = '../tmp/run.log'

def main():
    config.configure_logger()
    logging.info('### START')
    logging.error("error")
    logger.debug("debug")
    logger.warning("warn")
    logger.fatal("fatal")
    writeScores.createCsv()
    logging.info('### END')

if __name__ == '__main__':
    main()
