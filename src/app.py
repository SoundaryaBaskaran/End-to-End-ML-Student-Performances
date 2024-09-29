from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        return render_template('home.html', results=results[0])

# New route to handle Postman API requests
@app.route('/predictAPI', methods=['POST'])
def predict_api():
    try:
        # Expecting a JSON payload from Postman
        data = request.get_json()

        # Creating an instance of CustomData using the JSON data
        custom_data = CustomData(
            gender=data['gender'],
            race_ethnicity=data['race_ethnicity'],
            parental_level_of_education=data['parental_level_of_education'],
            lunch=data['lunch'],
            test_preparation_course=data['test_preparation_course'],
            reading_score=float(data['writing_score']),
            writing_score=float(data['reading_score'])
        )

        # Convert the data into a DataFrame
        pred_df = custom_data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()

        # Get the prediction
        results = predict_pipeline.predict(pred_df)

        # Return the result as JSON
        return jsonify({
            'prediction': results[0]
        })

    except Exception as e:
        # In case of an error, return the error message
        return jsonify({
            'error': str(e)
        }), 400

if __name__ == '__main__':
    print("Starting Flask app at http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
