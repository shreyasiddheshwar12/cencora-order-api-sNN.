LAB 1 - Create GitHub Repository and Sample Application
Objective: Create a small Pharmaceutical Order API used throughout the CI/CD lab.
1. Create a new repository named cencora-order-api-sNN.
2. Add README.md with project purpose and team members.
3. Create folder app and file app/main.py.
4. Create requirements.txt, Dockerfile and .dockerignore.
5. Commit all files to main branch.
# app/main.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get('/health')
def health():
    return jsonify({'status': 'UP', 'service': 'cencora-order-api'})

@app.post('/orders')
def create_order():
    payload = request.get_json(silent=True) or {}
    required = ['orderId', 'customerId', 'medicineCode', 'quantity']
    missing = [x for x in required if x not in payload]
    if missing:
        return jsonify({'status': 'ERROR', 'missing': missing}), 400
    return jsonify({'status': 'ACCEPTED', 'order': payload}), 202

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# requirements.txt
flask==3.0.3

# Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app	
EXPOSE 8080
CMD ["python", "app/main.py"]

