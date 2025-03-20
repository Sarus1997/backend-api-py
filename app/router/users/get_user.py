from flask import jsonify
from app.database import get_db
from app.models import User as u  # นำเข้าโมเดล User

def get_user():
    db = next(get_db())
    users = db.query(u).order_by(u.id).all()  # ใช้ 'id' หรือฟิลด์ที่ต้องการ
    result = [
        {
            "id": data.id,
            "username": data.username,
            "email": data.email,
            "password_hash": data.password_hash,
            "f_name": data.f_name,
            "l_name": data.l_name,
            "profile_picture": data.profile_picture,
            "oauth_provider": data.oauth_provider,
            "role": data.role,
            "oauth_id": data.oauth_id,
            "status": data.status,
            "last_login_at": data.last_login_at,
            "reset_token": data.reset_token,
            "reset_token_expires_at": data.reset_token_expires_at,
            "created_at": data.created_at,
            "updated_at": data.updated_at,
        } 
        for data in users
    ]
    return jsonify({"result": result})
