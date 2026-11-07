#!/usr/bin/python3
"""Export an employee's TODO list to a JSON file."""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Get employee information
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    user_response = requests.get(user_url)
    user_response.raise_for_status()
    user_data = user_response.json()

    username = user_data.get("username")

    # Get all TODO tasks
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todos_url)
    todos_response.raise_for_status()
    todos_data = todos_response.json()

    # Build the list of tasks belonging to the employee
    tasks_list = []

    for task in todos_data:
        if task.get("userId") == employee_id:
            task_dict = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            tasks_list.append(task_dict)

    # Create the JSON dictionary
    json_data = {
        str(employee_id): tasks_list
    }

    # Write data to the JSON file
    filename = "{}.json".format(employee_id)

    with open(filename, mode="w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file)
