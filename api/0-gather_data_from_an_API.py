#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Get employee information
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get employee TODO tasks
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Filter employee tasks
    employee_tasks = [
        task for task in todos_data
        if task.get("userId") == employee_id
    ]

    # Get completed tasks
    completed_tasks = [
        task for task in employee_tasks
        if task.get("completed") is True
    ]

    # Display employee progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name,
        len(completed_tasks),
        len(employee_tasks)
    ))

    # Display completed task titles
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))

