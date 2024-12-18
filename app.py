from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Register routes (these will be created in later steps)
@app.route('/')
def index():
    return {"message": "Welcome to the Library Management System API"}

if __name__ == '__main__':
    app.run(debug=True)
