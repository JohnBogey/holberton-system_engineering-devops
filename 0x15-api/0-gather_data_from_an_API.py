#!/usr/bin/python3
''' returns info on employee based on ID arg '''

import requests
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    url_tasks = "https://jsonplaceholder.typicode.com/todos"
    r_name = requests.get(url_user).json()["name"]
    r_tasks = requests.get(url_tasks).json()

    task_done = 0
    task_total = 0
    task_list = []

    for task in r_tasks:
        if task['userId'] == int(id):
            task_total += 1
            if task['completed'] is True:
                task_done += 1
                task_list.append(task['title'])
    print("Employee {} is done with tasks({}/{}):"
          .format(r_name, task_done, task_total))
    for title in task_list:
            print("\t {}".format(title))
