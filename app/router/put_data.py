from flask import jsonify, request
from app.database import get_db
from app.models import DataBase as Data

def update_employee(employee_id):
  db = next(get_db())
  data = request.json
  employee = db.query(Data).filter(Data.id == employee_id).first()
  if not employee:
    return jsonify({"error": "Employee not found"}), 404

  employee.first_name = data.get("first_name", employee.first_name)
  employee.last_name = data.get("last_name", employee.last_name)
  db.commit()
  return jsonify({"message": "Employee updated successfully!"})
