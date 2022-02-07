from flask import Flask,render_template,url_for,request,jsonify
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__, template_folder='template')
model = joblib.load('mm.pkl', 'r')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        int_features = [float(x) for x in request.form.values()]
        final_features = [(int_features)]

        pred = model.predict(final_features)
        output_val = pred

        if output_val == 0:
            return render_template('less.html', prediction_text= 'Fortunately for you. Your cancer is benign.')
        else:
            return render_template('more.html', prediction_text = 'Unfortunately you have a malignant cancer. But no worries check out some information below.')
        

    return render_template('predictor.html')

if __name__ == '__main__':
    app.run(debug=True)