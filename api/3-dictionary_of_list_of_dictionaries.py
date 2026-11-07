#!/usr/bin/python3
"""Export all employees' TODO lists to a JSON file."""

import json
import requests


if __name__ == "__main__":
    # Fetch all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users_response.raise_for_status()
    users_data = users_response.json()

    # Fetch all TODO tasks
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todos_url)
    todos_response.raise_for_status()
    todos_data = todos_response.json()

    # Create a dictionary containing all employees
    all_employees = {}

    for user in users_data:
        user_id = str(user.get("id"))
        username = user.get("username")

        all_employees[user_id] = []

        # Find all tasks belonging to this employee
        for task in todos_data:
            if task.get("userId") == user.get("id"):
                task_dict = {
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }

                all_employees[user_id].append(task_dict)

    # Export all employees' tasks to JSON
    with open(
        "todo_all_employees.json",
        mode="w",
        encoding="utf-8"
    ) as json_file:
        json.dump(all_employees, json_file)
