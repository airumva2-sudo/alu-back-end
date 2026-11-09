#!/usr/bin/python3
"""Export employee TODO list data to JSON."""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    user_response = requests.get(user_url)
    user = user_response.json()

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(
        todos_url, params={"userId": employee_id}
    )
    todos = todos_response.json()

    tasks = []
    for todo in todos:
        task = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user.get("username")
        }
        tasks.append(task)

    filename = "{}.json".format(employee_id)
    with open(filename, mode="w") as jsonfile:
        json.dump({str(employee_id): tasks}, jsonfile)
