
import csv

COLUMNS = ["id", "name", "score"]
RYAN = [1, "Ryan", 100]
KYLE = [2, "Kyle", 90]
JOHN = [3, "John", 80]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def createCsv():
    with open("data.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(COLUMNS)
        writer.writerow(RYAN)
        writer.writerow(KYLE)
        writer.writerow(JOHN)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    createCsv()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
