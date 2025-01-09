from flask import jsonify, request
from app.database import get_db
from app.models import DataBase as Data

def add_data():
  db = next(get_db())
  data = request.json
  new_data = Data(
      image_url=data["image_url"], 
      product_name=data["product_name"],
      price=data["price"], 
      brand=data["brand"],
      status=data["status"], 
      created_at=data["created_at"],
      updated_at=data["updated_at"],
  )
  db.add(new_data)
  db.commit()
  return jsonify({"message": "Employee added successfully!", "id": new_data.id}), 201
