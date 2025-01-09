from flask import jsonify, request
from app.database import get_db
from app.models import Product as Pro

def delete_data(data_id):
  db = next(get_db())
  existing_data = db.query(Pro).filter(Pro.id == data_id).first()

  if not existing_data:
    return jsonify({"message": "Data not found"}), 404

  db.delete(existing_data)
  db.commit()
  return jsonify({"message": "Data deleted successfully!"}), 200