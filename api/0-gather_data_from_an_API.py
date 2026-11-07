#!/usr/bin/python3
"""Gather data from an API and display an employee's TODO list progress."""

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data.get("name")

    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id
    )
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = [
        task for task in todos_data if task.get("completed")
    ]

    number_of_done_tasks = len(completed_tasks)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            number_of_done_tasks,
            total_tasks
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
