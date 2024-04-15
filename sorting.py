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


def selection_sort(list_of_numbers, direction):
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


def bubble_sort(list_of_numbers):
    size = len(list_of_numbers)
    for idx in range(size - 1):
        for idy in range(size - idx - 1):
            if list_of_numbers[idy] > list_of_numbers[idy + 1]:
                list_of_numbers[idy], list_of_numbers[idy + 1] = list_of_numbers [idy + 1], list_of_numbers[idy]
                sorted = 0
        if sorted == 1:
            break

    return list_of_numbers


def insertion_sort(list_of_numbers):
    measure = len(list_of_numbers)
    for idx in range(measure):
def main():
    pass


if __name__ == '__main__':
    my_data = read_data("numbers.csv")
    sorted_list = selection_sort(my_data["series_1"], "vzestupne")
    bubble_method = bubble_sort(my_data["series_2"])
    print(my_data)
    print(sorted_list)
    print(bubble_method)
    main()
