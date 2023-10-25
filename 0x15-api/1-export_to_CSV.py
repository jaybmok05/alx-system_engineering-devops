#!/usr/bin/python3
"""This script is used to get information about an
employee exported into CSV
"""
import csv
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        id = int(sys.argv[1])
        API_URL = 'https://jsonplaceholder.typicode.com'
        user_res = requests.get('{}/users/{}'.format(API_URL, id)).json()
        todos_res = requests.get('{}/todos'.format(API_URL)).json()
        user_name = user_res.get('username')
        todos = [todo for todo in todos_res if todo.get('userId') == id]

        # Create a CSV file for the user
        file_name = f'{id}.csv'

        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                "TASK_TITLE"])

            for todo in todos:
                writer.writerow([todo['userId'], user_name, todo['completed'],
                    todo['title']])
