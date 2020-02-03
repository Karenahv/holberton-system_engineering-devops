#!/usr/bin/python3
"""to do list information about an employee export to json """

import json
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
    mylist = []
    mydict = {}
    lista = []
    mydict_final = {}
    for todo in todos:
        if todo.get('userId') == id_e:
            lista.append(todo)
    user_name = user.get('username')
    mylist = [{'task': todo.get('title'),
               'completed': todo.get('completed'),
               'username': user.get('username')}
              for todo in lista]
    mydict_final[str(id_e)] = mylist
    with open(str(id_e) + '.json', 'w') as f:
        json.dump(mydict_final, f)

if __name__ == "__main__":
    tasks_employee()
