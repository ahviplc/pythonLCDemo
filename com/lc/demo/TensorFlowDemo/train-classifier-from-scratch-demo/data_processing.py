#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
data_processing.py
TensorFlow实例-从头开始做一个汽车状态分类器: 分析数据
Version: 1.0
Author: LC
DateTime:2019年1月21日14:34:22
一加壹博客最Top-一起共创1+1>2的力量！~LC
LC博客url: http://oneplusone.top/index.html
"""
import pandas as pd
from urllib.request import urlretrieve


def load_data(download=True):
    # download data from : http://archive.ics.uci.edu/ml/datasets/Car+Evaluation
    if download:
        data_path, _ = urlretrieve("http://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data", "car2.csv")
        print("Downloaded to car2.csv")

    # use pandas to view the data structure
    col_names = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
    data = pd.read_csv("car2.csv", names=col_names)
    return data


def convert2onehot(data):
    # covert data to onehot representation
    return pd.get_dummies(data, prefix=data.columns)


if __name__ == "__main__":
    data = load_data(download=True)
    new_data = convert2onehot(data)

    print(data.head())
    print("\nNum of data: ", len(data), "\n")  # 1728
    # view data values
    for name in data.keys():
        print(name, pd.unique(data[name]))
    print("\n", new_data.head(2))
    new_data.to_csv("car_onehot2.csv", index=False)
