from datetime import datetime
from flask import jsonify, request
from app.database import get_db
from app.models import DataBase as Data
from app.core.function import generate_id, generate_date_time

def add_data():
    db = next(get_db())
    data = request.json
    new_data = Data(
        product_id=generate_id(),
        image_url=data.get("image_url"), 
        product_name=data.get("product_name"),
        price=data.get("price"), 
        brand=data.get("brand"),
        status=data.get("status", 'active'),
        created_at=data.get("created_at", datetime.now()),
        updated_at=data.get("updated_at", '0'),
    )
    db.add(new_data)
    db.commit()
    return jsonify({
        "message": "Employee added successfully!", 
        "id": new_data.product_id,
        "timestamp": generate_date_time(),
    }), 201
