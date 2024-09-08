from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load('trained_model.pkl')

columns = [
    'Par_education', 'gender_male', 'race/ethnicity_group B',
    'race/ethnicity_group C', 'race/ethnicity_group D',
    'race/ethnicity_group E', 'lunch_standard',
    'test preparation course_none', 'math score_scaled',
    'reading score_scaled', 'writing score_scaled'
]
@app.route('/predict', methods=['POST'])

def predict():
    try:
        data = request.json
        input_df = pd.DataFrame([data])
        input_df = input_df.reindex(columns=columns, fill_value=0)
        predicted_score = model.predict(input_df)
        return jsonify({'predicted_score': round(predicted_score[0], 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
