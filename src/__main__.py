import config
import logging
import writeScores

def main():
    config.configure_logger()
    logging.info('### START')
    writeScores.createCsv()
    logging.info('### END')

if __name__ == '__main__':
    main()
