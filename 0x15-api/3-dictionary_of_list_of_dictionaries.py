#!/usr/bin/python3
"""to do list information about an employee export to json """

import json
import requests
import sys

base = 'https://jsonplaceholder.typicode.com/'


def tasks_employee():
    """get tasks of an employee"""
    req = requests.get(base + 'users/')
    users = req.json()
    req2 = requests.get(base + 'todos/')
    todos = req2.json()
    all_data = {}
    for user in users:
        username = user.get('username')
        user_todos = []
        for todo in todos:
            if todo.get('userId') == user.get('id'):
                mydict = {}
                mydict['username'] = username
                mydict['task'] = todo.get('title')
                mydict['completed'] = todo.get('completed')
                user_todos.append(mydict)
        all_data[str(user.get('id'))] = user_todos
    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_data, f)

if __name__ == "__main__":
    tasks_employee()
