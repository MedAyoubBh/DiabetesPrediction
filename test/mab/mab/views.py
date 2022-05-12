import random
from django.shortcuts import redirect, render
import pandas as pd
from sklearn.linear_model import LogisticRegression

def home(request):
    return render(request,"home.html")

def predict(request):
    return render(request,"predict.html")

def result(request):
    
    try:
        Pregnancies=float(request.GET['Pregnancies'])
        Glucose=float(request.GET['Glucose'])
        BloodPressure=float(request.GET['BloodPressure'])    
        SkinThickness=float(request.GET['SkinThickness'])
        Insulin=float(request.GET['Insulin'])
        BMI=float(request.GET['BMI'])
        DiabetesPedigreeFunction=float(request.GET['DiabetesPedigreeFunction'])
        Age=float(request.GET['Age'])
    except :
        return redirect('/predict/')

    df=pd.read_csv('static\DiabetesPrediction\data\diabetes.csv')
    X=df[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']].values
    y=df['Outcome'].values
    model=LogisticRegression(solver='newton-cg')
    model.fit(X,y)
    prediction=model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
    if prediction==[0]:
        return render(request,"negative.html")
    else :
        con=["Maintain blood sugar balance","Blood glucose self-monitoring","Have a medical follow-up","Do more physical activity","Have a personalized food program set up by a dietitian","Eat balanced meals at regular times","Do not skip meals","Adopt a varied diet"]
        con1=random.choice(con)
        cons=["","",""]
        for i in range(0,3):
            cs=random.choice(con)
            while cs==con1 or cs==cons[0] or cs==cons[1] or cs==cons[2] :
                cs=random.choice(con)
            cons[i]=cs
        con2=cons[0]
        con3=cons[1]
        con4=cons[2]
        return render(request,'positive.html',{"cons1":con1,"cons2":con2,"cons3":con3,"cons4":con4})
    
