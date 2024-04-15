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
                    data[key] = [int(value)]
                else:
                    data[key].append(int(value))
            iteration = iteration + 1

        return data


def selection_sort(list_of_numbers, *direction):
    lenght = len(list_of_numbers)
    for idx in range(lenght):
        min_idx = idx
        for idy in range(idx + 1, lenght):
            if direction == "vzestupne":
                if list_of_numbers[idy] < list_of_numbers[min_idx]:
                    min_idx = idy
            elif direction == "sestupne":
                if list_of_numbers[idy] > list_of_numbers[min_idx]:
                    min_idx = idy
            else:
                return print("Špatná direction")
        list_of_numbers[idx], list_of_numbers[min_idx] = \
            list_of_numbers[min_idx], list_of_numbers[idx]

    return list_of_numbers

def main():
    pass


if __name__ == '__main__':
    my_data = read_data("numbers.csv")
    sorted_list = selection_sort(my_data["series_1"])
    print(my_data)
    print(sorted_list)
    main()
