from flask import Flask, request, jsonify

app = Flask(__name__)
employees = {
    1: {"id": 1, "name": "John Doe", "salary": "50000", "age": "30"}
}
next_id = 2


@app.route("/api/v1/employees", methods=["GET"])
def get_employees():
    return jsonify(list(employees.values()))


@app.route("/api/v1/employee/<int:emp_id>", methods=["GET"])
def get_employee(emp_id):
    emp = employees.get(emp_id)
    return jsonify(emp) if emp else ("Not Found", 404)


@app.route("/api/v1/create", methods=["POST"])
def create_employee():
    global next_id
    data = request.get_json()
    new_emp = {
        "id": next_id,
        "name": data["name"],
        "salary": data["salary"],
        "age": data["age"]
    }
    employees[next_id] = new_emp
    next_id += 1
    return jsonify(new_emp), 201


@app.route("/api/v1/update/<int:emp_id>", methods=["PUT"])
def update_employee(emp_id):
    if emp_id not in employees:
        return "Not Found", 404
    data = request.get_json()
    employees[emp_id].update({
        "name": data["name"],
        "salary": data["salary"],
        "age": data["age"]
    })
    return jsonify(employees[emp_id])


@app.route("/api/v1/delete/<int:emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    if emp_id in employees:
        del employees[emp_id]
        return jsonify({"status": "deleted"})
    return "Not Found", 404


if __name__ == "__main__":
    app.run(port=5000)
