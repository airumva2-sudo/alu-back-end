#!/usr/bin/python3
"""Gather employee TODO list progress from an API."""

import requests
import sys

employee_id = int(sys.argv[1])

# Get employee information
user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
    employee_id
)
user = requests.get(user_url).json()

# Get all tasks belonging to the employee
todos_url = "https://jsonplaceholder.typicode.com/todos"
todos = requests.get(
    todos_url, params={"userId": employee_id}
).json()

# Get only completed tasks
completed_tasks = [
    task for task in todos if task.get("completed")
]

# Display employee progress
print(
    "Employee {} is done with tasks({}/{}):".format(
        user.get("name"),
        len(completed_tasks),
        len(todos)
    )
)

# Display completed task titles
for task in completed_tasks:
    print("\t {}".format(task.get("title")))
