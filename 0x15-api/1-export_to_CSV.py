#!/usr/bin/python3
"""to do list information about an employee export to csv """

import csv
import requests
import sys

base = 'https://jsonplaceholder.typicode.com/'


def tasks_employee():
    """get tasks of an employee"""
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
    lista = []
    status = []

    for todo in todos:
        if todo.get('userId') == id_e:
            lista.append(todo)
    with open(str(id_e) + '.csv', 'w') as f:
        wr = csv.writer(f, lineterminator='\n', quoting=csv.QUOTE_ALL)
        for todo in lista:
            wr.writerow(['{}'.format(line) for line in (todo.get('userId'),
                                                        user.get('username'),
                                                        todo.get('completed'),
                                                        todo.get('title'))])

if __name__ == "__main__":
    tasks_employee()
