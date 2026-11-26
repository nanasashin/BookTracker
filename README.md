# LocalHost Setup

## 0. Setup

Install Dependencies
```
pip install "fastapi[standard]"

pip install "fastapi[standard]" sqlmodel
```

## 1. Running the server

Run this command in app directory
```
uvicorn main:app --host 127.0.0.1 --port 8080
```

## 2. Running local host
Open this http in a browser
```
http://127.0.0.1:8080/
```