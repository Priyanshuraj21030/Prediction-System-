# Medical Prediction System

A comprehensive web application that uses machine learning to predict breast cancer and diabetes risks. This system provides accurate medical predictions using advanced algorithms while maintaining a user-friendly interface.

## Application Screenshots

### Main Page
!(/home_page.png)

## Features

### 1. Breast Cancer Prediction
![Breast Cancer Prediction](/breast_home.png)

- Advanced machine learning algorithm with 95%+ accuracy
- Comprehensive analysis of 30 different parameters
- Real-time prediction results
- Detailed information about breast cancer, symptoms, and risk factors

### 2. Diabetes Prediction
![Diabetes Prediction](/diabetes_home.png)

- Sophisticated prediction model for diabetes risk assessment
- Analysis based on key health parameters
- Instant results with personalized insights
- User-friendly interface for data input

## Technology Stack

### Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap 5.3
- Font Awesome Icons
- jQuery

### Backend

- Python
- Flask
- NumPy
- Pandas
- Scikit-learn

## Running the Applications

Follow these steps in order to run all applications:

### Step 1: **Run Breast Cancer Prediction App**

Open a terminal and run:
```bash
cd breast
cd Breast-Cancer-Predictor
python app.py
```
This will start the breast cancer prediction service on http://localhost:5000

### Step 2: **Run Diabetes Prediction App**

Open a new terminal and run:
```bash
cd "Diabetes-Detection"
cd "Diabetes Prediction App"
python app.py
```
This will start the diabetes prediction service on http://localhost:5001

### Step 3: **Access the Main Application**

Navigate to the templates folder and open index.html in your web browser:
```bash
cd templates
```
Open index.html in your preferred web browser

## Important Notes

1. Make sure to run the applications in the specified order
2. Keep all terminals open while using the applications
3. Required dependencies:
   - For Diabetes: 'scaler.pkl' and 'lr.pkl'
   - For Breast Cancer: Random Forest model is trained at runtime
4. The applications run on different ports:
   - Breast Cancer Prediction: http://localhost:5000
   - Diabetes Prediction: http://localhost:5001

## **Dependencies**

Install required dependencies using:
bash
pip install -r requirements.txt

Required packages:

- Flask
- NumPy
- Pandas
- Scikit-learn
- Pickle

## Support

For support, please open an issue in the repository.

---
