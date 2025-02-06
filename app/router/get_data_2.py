from flask import jsonify
from app.database import get_db
from datetime import datetime
from sqlalchemy import text

def get_data_2():
    db = None
    try:
        #* ตรวจสอบว่า get_db() ทำงานได้หรือไม่
        db = next(get_db())
        print("✅ Database connection successful")

        #* ดึงข้อมูลจากฐานข้อมูลด้วย text()
        query = text("SELECT * FROM product_")
        product = db.execute(query).fetchall()
        print(f"🛒 Retrieved {len(product)} products from database.")

        #* ถ้าไม่มีข้อมูล
        if not product:
            result = {
                "details": {"status": "success", "code": "code::0000", "reason": "No product data."},
                "result": {
                    "data": [],
                    "date_now": str(int(datetime.utcnow().timestamp() * 1000))
                }
            }
            return jsonify(result)

        #* จัดรูปแบบข้อมูล
        product_list = [
            {
                "product_id": data[0],
                "image_url": data[1],
                "product_name": data[2],
                "price": data[3],
                "brand": data[4],
            }
            for data in product
        ]

        result = {
            "details": {"status": "success", "code": "code::0000", "reason": ""},
            "result": {
                "data": product_list,
                "date_now": str(int(datetime.utcnow().timestamp() * 1000))
            }
        }
        return jsonify(result)

    except Exception as err:
        print(f"❌ Error: {err}")

        error_response = {
            "details": {"status": "error", "code": "code::error_0002", "reason": str(err)},
            "result": {"data": [], "date_now": str(int(datetime.utcnow().timestamp() * 1000))}
        }
        return jsonify(error_response)

    finally:
        if db:
            db.close()
            print("🔒 Database connection closed")
