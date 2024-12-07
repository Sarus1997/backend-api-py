# 🛠️ Backend API Py

## 🚀 Installation

1. **Clone the project from GitHub**

   ```bash
   git clone <repository_url>
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
