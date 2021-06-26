# -*- coding: utf-8 -*-
"""

@File    : file_util.py
@Description :
@Author  : ljw
@Time    : 2021/6/18 14:16

"""
import csv
import os


def save_csv_data(username, password, fpath):
    all_info = read_csv_data(fpath)
    for info in all_info[1:]:
        if info and username == info[0]:
            delete_csv_data(info[0], info[1], all_info, fpath)
    with open(fpath, 'a+', newline='') as csv_writer:
        writer = csv.writer(csv_writer)
        if not read_csv_data(fpath):
            writer.writerow(['username', 'password'])
            writer.writerow([username, password])
        else:
            writer.writerow([username, password])


def read_csv_data(fpath):
    with open(fpath, 'r', newline='') as csv_reader:
        reader = csv.reader(csv_reader)
        return [row for row in reader]


def delete_csv_data(username, password, a, fpath):
    os.remove(fpath)
    for line in a:
        if line[0] == username and line[1] == password:
            continue
        else:
            with open(fpath, 'a', newline='') as csv_writer:
                writer = csv.writer(csv_writer)
                writer.writerow([line[0], line[1]])


if __name__ == '__main__':
    a=read_csv_data("../data/login_info.csv")
    print(a)
    # save_csv_data("2", "5")
    # save_csv_data("3", "6")
    # save_csv_data("1", "7")
    # save_csv_data("1", "0")
    # save_csv_data("2", "3")
