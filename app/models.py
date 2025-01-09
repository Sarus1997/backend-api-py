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

class Category(Base): #* ตารางที่สอง
  __tablename__ = "category" #* ชื่อตารางที่จะสร้างในฐานข้อมูล

  category_id = Column(Integer, primary_key=True, index=True)
  category_name = Column(String(50), nullable=False)

