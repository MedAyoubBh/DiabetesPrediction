from django.shortcuts import render
import pandas as pd
from sklearn.linear_model import LogisticRegression

def home(request):
    return render(request,"home.html")

def predict(request):
    return render(request,"predict.html")

def result(request):
    
    df=pd.read_csv('static\DiabetesPrediction\data\diabetes.csv')
    X=df[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']].values
    y=df['Outcome'].values
    model=LogisticRegression(solver='newton-cg')
    model.fit(X,y)
    Pregnancies=float(request.GET['Pregnancies'])
    Glucose=float(request.GET['Glucose'])
    BloodPressure=float(request.GET['BloodPressure'])    
    SkinThickness=float(request.GET['SkinThickness'])
    Insulin=float(request.GET['Insulin'])
    BMI=float(request.GET['BMI'])
    DiabetesPedigreeFunction=float(request.GET['DiabetesPedigreeFunction'])
    Age=float(request.GET['Age'])


    prediction=model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

    if prediction==[0]:
        return render(request,"negative.html")
    else :
        return render(request,'positive.html')