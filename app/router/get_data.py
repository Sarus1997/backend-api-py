from flask import jsonify
from app.database import get_db
from app.models import DataBase as Data

def get_data():
  
  db = next(get_db())
  product = db.query(Data).all()
  return jsonify([
    {
      "product_id": data.product_id,
      "image_url": data.image_url, 
      "product_name": data.product_name,
      "price": data.price,
      "brand": data.brand,
      "status": data.status,
      "created_at": data.created_at,
      "updated_at": data.updated_at,
    } 
    for data in product
  ])
