#!/usr/bin/python3
"""Display an employee's TODO list progress using a REST API."""
import requests
import sys

employee_id = int(sys.argv[1])
base_url = "https://jsonplaceholder.typicode.com"

user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
todos = requests.get(
    "{}/users/{}/todos".format(base_url, employee_id)
).json()

done = [t.get("title") for t in todos if t.get("completed")]

print("Employee {} is done with tasks({}/{}):".format(
    user.get("name"), len(done), len(todos)))
for title in done:
    print("\t {}".format(title))
