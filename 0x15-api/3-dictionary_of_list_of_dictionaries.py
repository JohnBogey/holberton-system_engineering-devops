#!/usr/bin/python3
''' returns info on employee based on ID arg into csv '''

import json
import requests
from sys import argv

if __name__ == "__main__":
    url_user = "https://jsonplaceholder.typicode.com/users"
    url_tasks = "https://jsonplaceholder.typicode.com/todos"
    r_users = requests.get(url_user).json()
    r_tasks = requests.get(url_tasks).json()

    data = {}

    for user in r_users:
        task_list = []
        for task in r_tasks:
            task_dict = {}
            if task['userId'] == user['id']:
                task_dict["task"] = task['title']
                task_dict["completed"] = task['completed']
                task_dict["username"] = user['username']
                task_list.append(task_dict)
        data[user['id']] = task_list

    with open("todo_all_employees.json", "w") as out:
        json.dump(data, out)
