from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Final_XGB_Model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        trend_value = float(request.form['trend'])
        hd_value = float(request.form['hd'])
        speed_value = float(request.form['speed'])
        ram_value = float(request.form['ram'])
        screen_value = float(request.form['screen'])
        prediction = model.predict([trend_value,hd_value,speed_value,ram_value,screen_value])
        if prediction < 0:
            return render_template('index.html',prediction_texts="Please Enter Right Input Values")
        else:
            return render_template('index.html',prediction_text="Your computer Price is {}".format(prediction))
    else:
     return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

    
    