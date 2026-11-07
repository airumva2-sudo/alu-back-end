#!/usr/bin/python3
"""Export an employee's TODO list to a JSON file."""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Fetch employee information
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    user_response = requests.get(user_url)
    user_data = user_response.json()

    username = user_data.get("username")

    # Fetch TODO tasks
    tasks_url = "https://jsonplaceholder.typicode.com/todos"
    tasks_response = requests.get(tasks_url)
    tasks_data = tasks_response.json()

    # Filter tasks belonging to the employee
    employee_tasks = [
        task for task in tasks_data
        if task.get("userId") == employee_id
    ]

    # Prepare JSON data
    tasks_list = []

    for task in employee_tasks:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        tasks_list.append(task_dict)

    json_data = {
        str(employee_id): tasks_list
    }

    # Export to JSON file
    filename = "{}.json".format(employee_id)

    with open(filename, mode="w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file)
