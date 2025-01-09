import os
import uuid
from datetime import datetime

#* ฟังก์ชันสำหรับสร้าง secret key
def generate_secret_key() -> str:
  return os.urandom(32).hex()

#* ฟังก์ชันสำหรับสร้าง id แบบสุ่ม ไม่ซ้ำ
def generate_id(provided_id: str = None) -> str:
  return provided_id or str(uuid.uuid4())

#* ฟังก์ชันสำหรับสร้างวันที่และเวลา
def generate_date_time() -> str:
  now = datetime.now()
  return now.strftime('%Y-%m-%d %H:%M:%S')
