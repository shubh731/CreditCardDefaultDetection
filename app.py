from flask import Flask,request,render_template,jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import sys,os
from src.pipelines.Predict_pipeline import PredictPipeline,CustomData

from src.Exception import CustomException
from src.logger import logging


app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my application"


@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    
    else:
        data=CustomData(
            limit_bal=int(request.form.get('limit_bal',0)),
            sex=int(request.form.get('sex')),
            education= int(request.form.get('education')),
            marriage= int(request.form.get('marriage')),
            age= int(request.form.get('age',0)),
            pay_0=int(request.form.get('pay_0')),
            pay_2= int(request.form.get('pay_2')),
            pay_3=int(request.form.get('pay_3')),
            pay_4=int(request.form.get('pay_4')),
            pay_5=int(request.form.get('pay_5')),
            pay_6=int(request.form.get('pay_6')),
            bill_amt1=int(request.form.get('bill_amt1')),
            bill_amt2=int(request.form.get('bill_amt2')),
            bill_amt3=int(request.form.get('bill_amt3')),
            bill_amt4=int(request.form.get('bill_amt4')),
            bill_amt5=int(request.form.get('bill_amt5')),
            bill_amt6=int(request.form.get('bill_amt6')),
            pay_amt1=int(request.form.get('pay_amt1')),
            pay_amt2=int(request.form.get('pay_amt2')),
            pay_amt3=int(request.form.get('pay_amt3')),
            pay_amt4=int(request.form.get('pay_amt4')),
            pay_amt5=int(request.form.get('pay_amt5')),
            pay_amt6=int(request.form.get('pay_amt6'))
        )
            
        final_new_data=data.get_data_as_dataframe()

        predict_pipeline=PredictPipeline()
        prediction=predict_pipeline.predict(final_new_data)

        result = ""

    if prediction == 1:

        result = "The credit card holder will be Defaulter in the next month"
    else:
        result = "The Credit card holder will not be Defaulter in the next month"

    return render_template('home.html', prediction_text = result)

        # return render_template('home.html',final_result=results)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug= True)