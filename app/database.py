from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ตั้งค่าการเชื่อมต่อ
DATABASE_URL = "mysql+mysqlconnector://root:root@localhost/employee_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ฟังก์ชันสำหรับดึง session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
