#!/usr/bin/python3
"""Export an employee's TODO list to a CSV file."""

import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    tasks_url = "https://jsonplaceholder.typicode.com/todos"
    tasks_response = requests.get(tasks_url)
    tasks_data = tasks_response.json()

    employee_tasks = [
        task for task in tasks_data
        if task.get("userId") == employee_id
    ]

    filename = "{}.csv".format(employee_id)

    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in employee_tasks:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
