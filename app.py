from flask import Flask, render_template, request, jsonify
#import joblib
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
#model = joblib.load('crime_model.pkl')

# Define the web page routes
@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the user input
    region = request.form.get('region')
    date = request.form.get('date')
    time = request.form.get('time')

    # call your machine learning model to predict the crime
    predicted_crime = predict(region, date, time)

    # return the predicted crime as JSON response
    return jsonify({'predicted_crime': predicted_crime})

# create a function to retrieve crime data from the database and send it to the frontend as a JSON object
@app.route('/crime_data')
def crime_data():
    conn = sqlite3.connect('crime.db')
    c = conn.cursor()
    c.execute('SELECT * FROM crime')
    rows = c.fetchall()
    data = []
    for row in rows:
        data.append({
            'year': row[0],
            'crime_type': row[1],
            'count': row[2]
        })
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
