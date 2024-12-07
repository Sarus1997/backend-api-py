from flask import Blueprint, jsonify, request
from sqlalchemy.exc import NoResultFound
from app.database import get_db
from app.models import Employee

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/employees", methods=["GET"])
def get_employees():
    """ดึงข้อมูลพนักงานทั้งหมด"""
    db = next(get_db())
    employees = db.query(Employee).all()
    return jsonify([{"id": emp.id, "first_name": emp.first_name, "last_name": emp.last_name} for emp in employees])

@api_blueprint.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    """ดึงข้อมูลพนักงานตาม ID"""
    db = next(get_db())
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify({"id": employee.id, "first_name": employee.first_name, "last_name": employee.last_name})

@api_blueprint.route("/employees", methods=["POST"])
def add_employee():
    """เพิ่มพนักงานใหม่"""
    db = next(get_db())
    data = request.json
    new_employee = Employee(first_name=data["first_name"], last_name=data["last_name"])
    db.add(new_employee)
    db.commit()
    return jsonify({"message": "Employee added successfully!", "id": new_employee.id}), 201

@api_blueprint.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    """อัปเดตข้อมูลพนักงาน"""
    db = next(get_db())
    data = request.json
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    # อัปเดตข้อมูล
    employee.first_name = data.get("first_name", employee.first_name)
    employee.last_name = data.get("last_name", employee.last_name)
    db.commit()
    return jsonify({"message": "Employee updated successfully!"})

@api_blueprint.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    """ลบข้อมูลพนักงาน"""
    db = next(get_db())
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    db.delete(employee)
    db.commit()
    return jsonify({"message": "Employee deleted successfully!"})
