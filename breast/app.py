import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        final_features = [np.array(features)]
        prediction = model.predict(final_features)
        
        output = "Malignant" if prediction[0] == 1 else "Benign"
        return render_template('index.html', 
                             prediction_text=f'The tumor is predicted to be: {output}')
    except Exception as e:
        return render_template('index.html', 
                             prediction_text='Error: Please check your input values')

# ... rest of the code ... 