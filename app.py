import json
import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


app=Flask(__name__)
# load the model 
rain=pickle.load(open(r'C:\Users\oussa\OneDrive\Bureau\app\models\rain_predictor.pkl','rb'))
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/page1', methods=["POST"])
def predict():
  A = [float(x) for x in request.form.values()]
  pred_rain=rain.predict_proba([A])[0][1]
  return render_template("home.html", prediction_text="rain probability = {}".format(pred_rain))




if __name__ == '__main__':
    app.run(debug=True)