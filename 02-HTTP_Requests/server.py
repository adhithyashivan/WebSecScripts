from flask import Flask, request, jsonify, Response

app = Flask(__name__)
employees = {1: {"id": 1, "name": "John Doe", "salary": "50000", "age": "30"}}
next_id = 2


def handle_options(allowed_methods):
    return Response(headers={
        "Allow": allowed_methods,
        "Content-Type": "application/json"
    })


@app.route("/api/v1/employees", methods=["GET", "OPTIONS"])
def get_employees():
    if request.method == "OPTIONS":
        return handle_options("GET, OPTIONS")
    return jsonify(list(employees.values()))


@app.route("/api/v1/employee/<int:emp_id>", methods=["GET", "OPTIONS"])
def get_employee(emp_id):
    if request.method == "OPTIONS":
        return handle_options("GET, OPTIONS")
    emp = employees.get(emp_id)
    return jsonify(emp) if emp else ("Not Found", 404)


@app.route("/api/v1/create", methods=["POST", "OPTIONS"])
def create_employee():
    if request.method == "OPTIONS":
        return handle_options("POST, OPTIONS")
    global next_id
    data = request.get_json()
    new_emp = {**data, "id": next_id}
    employees[next_id] = new_emp
    next_id += 1
    return jsonify(new_emp), 201


@app.route("/api/v1/update/<int:emp_id>", methods=["PUT", "OPTIONS"])
def update_employee(emp_id):
    if request.method == "OPTIONS":
        return handle_options("PUT, OPTIONS")
    if emp_id not in employees:
        return "Not Found", 404
    employees[emp_id].update(request.get_json())
    return jsonify(employees[emp_id])


@app.route("/api/v1/delete/<int:emp_id>", methods=["DELETE", "OPTIONS"])
def delete_employee(emp_id):
    if request.method == "OPTIONS":
        return handle_options("DELETE, OPTIONS")
    if emp_id in employees:
        del employees[emp_id]
        return jsonify({"status": "deleted"})
    return "Not Found", 404


if __name__ == "__main__":
    app.run(port=5000)
