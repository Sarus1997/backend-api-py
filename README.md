# 🛠️ Backend API Py

## 🚀 Installation

1. **Clone the project from GitHub**

   ```bash
   git clone https://github.com/Sarus1997/backend-api-py.git
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create the database**

   ```bash
   mysql -u root -p<password> < employee_db.sql
   ```

# 🖥️ Usage

Run the application

   ```bash
   python main.py
   ```

Retrieve all employees

   ```bash
curl -X GET http://localhost:5000/api/v1/employees
   ```

Retrieve employee details by ID

   ```bash
curl -X GET http://localhost:5000/api/v1/employees/<id>
   ```

Add a new employee

   ```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"first_name":"<first_name>","last_name":"<last_name>"}' \
http://localhost:5000/api/v1/employees

   ```

Update employee information

   ```bash
curl -X PUT -H "Content-Type: application/json" \
-d '{"first_name":"<first_name>","last_name":"<last_name>"}' \
http://localhost:5000/api/v1/employees/<id>
   ```

Delete an employee

   ```bash
curl -X DELETE http://localhost:5000/api/v1/employees/<id>
   ```
