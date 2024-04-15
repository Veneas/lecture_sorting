import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r", newline="\n") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        iteration = 0
        for row in reader:
            for key, value in row.items():
                if iteration == 0:
                    data[key] =  [int(value)]
                else:
                    data[key].append(int(value))
            iteration = iteration + 1

        return data

def main():
    pass


if __name__ == '__main__':
    my_data = read_data("numbers.csv")
    print(my_data)
    main()
