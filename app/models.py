from sqlalchemy import Column, Integer, String
from app.database import Base

class Product(Base):
  __tablename__ = "product_" #* ชื่อตารางที่จะสร้างในฐานข้อมูล

  product_id = Column(Integer, primary_key=True, index=True)
  image_url = Column(String(50), nullable=False)
  product_name = Column(String(50), nullable=False)
  price = Column(Integer, nullable=False)
  brand = Column(String(50), nullable=False)
  status = Column(String(50), nullable=False)
  created_at = Column(Integer, nullable=False)
  updated_at = Column(String(50), nullable=False)

class User(Base):
    __tablename__ = "users"

    id = Column(String(255), primary_key=True, nullable=False, unique=True, index=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    f_name = Column(String(255), nullable=True, default=None)
    l_name = Column(String(255), nullable=True, default=None)
    profile_picture = Column(String, nullable=True, default=None)
    oauth_provider = Column(String(10), nullable=True, default='email')
    role = Column(String(10), nullable=True, default='user')
    oauth_id = Column(String(255), nullable=True, default=None)
    status = Column(String(50), nullable=True, default='active')
    last_login_at = Column(String(50), nullable=True, default=None)
    reset_token = Column(String(255), nullable=True, default=None)
    reset_token_expires_at = Column(String(50), nullable=True, default=None)
    created_at = Column(String(50), nullable=True, default=None)
    updated_at = Column(String(50), nullable=True, default=None)

class Category(Base): #* ตารางที่สอง
  __tablename__ = "category" #* ชื่อตารางที่จะสร้างในฐานข้อมูล

  category_id = Column(Integer, primary_key=True, index=True)
  category_name = Column(String(50), nullable=False)

