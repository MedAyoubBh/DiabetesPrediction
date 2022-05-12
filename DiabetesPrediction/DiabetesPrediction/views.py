import random
from django.shortcuts import redirect, render
from jinja2 import Undefined
import psycopg2
import pickle

def login(request):
    return render(request,"login.html")

def home(request):
    conn = psycopg2.connect(
    database="bd", user='postgres', password='root', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    str='SELECT * from public."user" where username = \''+request.GET["username"]+'\' and password = \''+request.GET["password"]+'\''
    cursor.execute(str)
    result = cursor.fetchall()
    conn.close()

    if result==[]:
        return redirect('../')
    else:
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

    # load the model from disk
    filename = 'finalized_model.sav'
    model = pickle.load(open(filename, 'rb'))
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
    
