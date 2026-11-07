#!/usr/bin/python3
"""Export an employee's TODO list to a CSV file."""

import csv
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

    # Fetch employee TODO tasks
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id
    )
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Export tasks to CSV
    filename = "{}.csv".format(employee_id)

    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
