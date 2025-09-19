How to run 
1. Install Python 3.13.7 and MySQL
2. Run env "venv\Scripts\activate.bat"
3. Install all dependency "pip install -r requirements.txt"
4. Create database name topsis_db
5. Run db migrations with 
    flask db init
    flask db migrate -m "initial tables"
    flask db  upgrade
6. Run application "python app.py"
