from flask import Flask, jsonify, request

app = Flask(__name__)

# ตัวอย่าง API
@app.route('/api/v1/greet', methods=['GET'])
def greet():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/v1/data', methods=['POST'])
def create_data():
    data = request.json
    return jsonify({"received": data}), 201

if __name__ == '__main__':
    app.run(debug=True)
