#!/usr/bin/python3
''' returns info on employee based on ID arg into csv '''

import requests
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    url_tasks = "https://jsonplaceholder.typicode.com/todos"
    r_name = requests.get(url_user).json()["name"]
    r_tasks = requests.get(url_tasks).json()

    with open("{}.csv".format(id), "a") as csv:
        for task in r_tasks:
            if task['userId'] == int(id):
                csv.write('"{}","{}","{}","{}"\n'
                          .format(id, r_name, str(task['completed']),
                                  task['title']))
