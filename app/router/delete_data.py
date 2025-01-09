from flask import jsonify
from app.database import get_db
from app.models import DataBase as Data

def delete_employee(employee_id):
  db = next(get_db())
  employee = db.query(Data).filter(Data.id == employee_id).first()
  if not employee:
      return jsonify({"error": "Employee not found"}), 404

  db.delete(employee)
  db.commit()
  return jsonify({"message": "Employee deleted successfully!"})
