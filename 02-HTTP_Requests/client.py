import requests

PROXY = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}

BASE_URL = "http://127.0.0.1:5000/api/v1"
HEADERS = {
    "Accept": "application/json",
    "User-Agent": "PythonClient/1.0"
}


def show_response(r):
    print(f"Status: {r.status_code}")
    print("Response:", r.text[:200], "\n")


def run_all():
    print("➡ GET all employees")
    r = requests.get(f"{BASE_URL}/employees", headers=HEADERS, proxies=PROXY)
    show_response(r)

    print("➡ POST create employee")
    r = requests.post(f"{BASE_URL}/create", json={"name": "Alice",
                      "salary": "70000", "age": "28"}, headers=HEADERS, proxies=PROXY)
    show_response(r)

    emp_id = r.json().get("id")

    print(f"➡ GET employee ID {emp_id}")
    r = requests.get(f"{BASE_URL}/employee/{emp_id}",
                     headers=HEADERS, proxies=PROXY)
    show_response(r)

    print(f"➡ PUT update employee ID {emp_id}")
    r = requests.put(f"{BASE_URL}/update/{emp_id}", json={"name": "Alice Updated",
                     "salary": "80000", "age": "29"}, headers=HEADERS, proxies=PROXY)
    show_response(r)

    print(f"➡ DELETE employee ID {emp_id}")
    r = requests.delete(f"{BASE_URL}/delete/{emp_id}",
                        headers=HEADERS, proxies=PROXY)
    show_response(r)


if __name__ == "__main__":
    run_all()
