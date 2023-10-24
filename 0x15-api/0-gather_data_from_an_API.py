#!/usr/bin/python3
"""This script is used to get information about an
employee
"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        id = int(sys.argv[1])
        API_URL = 'https://jsonplaceholder.typicode.com'
        user_res = requests.get('{}/users/{}'.format(API_URL, id)).json()
        todos_res = requests.get('{}/todos'.format(API_URL)).json()
        user_name = user_res.get('name')
        todos = [todo for todo in todos_res if todo.get('userId') == id]
        todos_done = [todo for todo in todos if todo.get('completed')]

        print('Employee {} is done with tasks({}/{}):'.format(user_name,
                                                             len(todos_done),
                                                             len(todos)))

        for todo_done in todos_done:
            print('\t {}'.format(todo_done.get('title')))
