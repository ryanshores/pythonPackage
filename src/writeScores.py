import config
import csv
import logging

logger = logging.getLogger(__name__)

COLUMNS = ['id', 'name', 'score']
RYAN = [1, 'Ryan', 100]
KYLE = [2, 'Kyle', 90]
JOHN = [3, 'John', 80]

OUTPUT_FILE = config.OUTPUT_DIR / 'scores.csv'

def createCsv():
    logger.debug('Creating scores.csv')
    with open(OUTPUT_FILE, "w") as f:
        writer = csv.writer(f)
        writer.writerow(COLUMNS)
        writer.writerow(RYAN)
        writer.writerow(KYLE)
        writer.writerow(JOHN)