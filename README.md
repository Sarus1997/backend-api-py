# การติดตั้งและใช้งาน

## การติดตั้ง

1. ทำการ clone โครงการจาก github
2. ทำการติดตั้ง dependencies ด้วยคำสั่ง `pip install -r requirements.txt`
3. ทำการสร้าง database ด้วยคำสั่ง `mysql -u root -p<password> < employee_db.sql`

## การใช้งาน

1. ทำการรันโปรแกรมด้วยคำสั่ง `python main.py`
2. ทำการดึงข้อมูลพนักงานทั้งหมดด้วยคำสั่ง `curl -X GET http://localhost:5000/api/v1/employees`
3. ทำการดึงข้อมูลพนักงานตาม ID ด้วยคำสั่ง `curl -X GET http://localhost:5000/api/v1/employees/<id>`
4. ทำการเพิ่มพนักงานใหม่ด้วยคำสั่ง `curl -X POST -H "Content-Type: application/json" -d '{"first_name":"<first_name>","last_name":"<last_name>"}' http://localhost:5000/api/v1/employees`
5. ทำการอัปเดตข้อมูลพนักงานด้วยคำสั่ง `curl -X PUT -H "Content-Type: application/json" -d '{"first_name":"<first_name>","last_name":"<last_name>"}' http://localhost:5000/api/v1/employees/<id>`
6. ทำการลบข้อมูลพนักงานด้วยคำสั่ง `curl -X DELETE http://localhost:5000/api/v1/employees/<id>`
