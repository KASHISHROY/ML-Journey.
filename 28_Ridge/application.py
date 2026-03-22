import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

#Flask application create
application=Flask(__name__)
app=application


#import ridge regressor and Standard scaler pickle as our app should intercat with the model do transformation of the data->scaler and predict->ridge
#load from pickle
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))

#route for the home page
@app.route("/")
def index():
    return render_template('index.html')   #looks for the index.html in the emplates folder

#route for prediction->get&post method
@app.route('/predicate',methods=['GET','POST'])
def predict_datapoint():
    if request.method=="POST": #whenever post interact with ridge model
        #get value from form
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        #first transform to standardize all of them
        new_data_scaled=standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_model.predict(new_data_scaled)

        return render_template('home.html',results=result[0])    #show the result in home.html page again,the result returned is in form of list,first value
        
    else:   #display the form
        return render_template('home.html')



if __name__=="__main__":
    app.run(host="0.0.0.0")