from flask import Flask, render_template, request
import subprocess
import threading

app = Flask(__name__)

def run_breast_cancer_app():
    subprocess.run(["python", "breast/Breast-Cancer-Predictor/app.py"], port=5001)

def run_diabetes_app():
    subprocess.run(["python", "Diabetes-Detection/Diabetes Prediction App/app.py"], port=5002)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Start the other apps in separate threads
    breast_thread = threading.Thread(target=run_breast_cancer_app)
    diabetes_thread = threading.Thread(target=run_diabetes_app)
    
    breast_thread.start()
    diabetes_thread.start()
    
    # Run the main app
    app.run(port=5000, debug=True) 