from datetime import datetime
from flask import jsonify, request
from app.database import get_db
from app.models import Product as Pro
from app.core.function import generate_id, generate_date_time

def update_data():
  db = next(get_db())
  data = request.json
  product_id = data.get("product_id")
  
  # Fetch the existing record
  existing_data = db.query(Pro).filter(Pro.product_id == product_id).first()
  
  if not existing_data:
    return jsonify({"message": "Product not found"}), 404
  
  # Update the fields
  existing_data.image_url = data.get("image_url", existing_data.image_url)
  existing_data.product_name = data.get("product_name", existing_data.product_name)
  existing_data.price = data.get("price", existing_data.price)
  existing_data.brand = data.get("brand", existing_data.brand)
  existing_data.status = data.get("status", 'update')
  existing_data.updated_at = data.get("updated_at", datetime.now())
  
  db.commit()
  
  return jsonify({
    "message": "Product updated successfully!", 
    "id": existing_data.product_id,
    "timestamp": generate_date_time(),
  }), 200 