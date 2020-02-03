#!/usr/bin/python3
"""to do list information about an employee """

import requests
import sys

base = 'https://jsonplaceholder.typicode.com/'


def tasks_employee():
    """get tasks done of an employee"""
    if len(sys.argv) < 2:
        print("Missing id")
        return
    try:
        id_e = int(sys.argv[1])
    except ValueError:
        print("id must be an integer")
        return
    req = requests.get(base + 'users/' + str(id_e))
    user = req.json()
    req2 = requests.get(base + 'todos/')
    todos = req2.json()
    tasks = []
    finished = 0
    not_finished = 0
    total = 0

    for todo in todos:
        if todo.get('userId') == id_e:
            if todo.get('completed') is True:
                finished = finished + 1
                tasks.append(todo.get('title'))
            else:
                not_finished = not_finished + 1
    total = finished + not_finished
    print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
                                                          finished, total))
    for task in tasks:
        print("\t {}".format(task))

if __name__ == "__main__":
    tasks_employee()
