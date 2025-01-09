from flask import jsonify, request
from app.database import get_db
from app.models import DataBase as Data

def update_data(data_id):
  db = next(get_db())
  data = request.json
  existing_data = db.query(Data).filter(Data.id == data_id).first()

  if not existing_data:
    return jsonify({"message": "Data not found"}), 404

  existing_data.image_url = data.get("image_url", existing_data.image_url)
  existing_data.product_name = data.get("product_name", existing_data.product_name)
  existing_data.price = data.get("price", existing_data.price)
  existing_data.brand = data.get("brand", existing_data.brand)
  existing_data.status = data.get("status", existing_data.status)
  existing_data.created_at = data.get("created_at", existing_data.created_at)
  existing_data.updated_at = data.get("updated_at", existing_data.updated_at)

  db.commit()
  return jsonify({"message": "Data updated successfully!", "id": existing_data.id}), 200