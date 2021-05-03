#!/usr/bin/python3
''' returns info on employee based on ID arg into csv '''

import requests
import json
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    url_tasks = "https://jsonplaceholder.typicode.com/todos"
    r_name = requests.get(url_user).json()["name"]
    r_tasks = requests.get(url_tasks).json()

    task_list = []
    for task in r_tasks:
        task_dict = {}
        if task['userId'] == int(id):
            task_dict["task"] = task['title']
            task_dict["completed"] = task['completed']
            task_dict["username"] = r_name
            task_list.append(task_dict)

    data = {}
    data[id] = task_list

    with open("{}.json".format(id), "w") as out:
        json.dump(data, out)
