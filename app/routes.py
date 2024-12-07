from flask import Blueprint, jsonify, request
from app.database import get_db
from app.models import Employee

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/employees", methods=["GET"])
def get_employees():
    db = next(get_db())
    employees = db.query(Employee).all()
    return jsonify([{"id": emp.id, "first_name": emp.first_name, "last_name": emp.last_name} for emp in employees])

@api_blueprint.route("/employees", methods=["POST"])
def add_employee():
    db = next(get_db())
    data = request.json
    new_employee = Employee(first_name=data["first_name"], last_name=data["last_name"])
    db.add(new_employee)
    db.commit()
    return jsonify({"message": "Employee added successfully!"}), 201
