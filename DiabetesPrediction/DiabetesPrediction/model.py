import pandas as pd
from sklearn.neural_network import MLPClassifier
import pickle

df=pd.read_csv('static\DiabetesPrediction\data\diabetes.csv')
X=df[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']].values
y=df['Outcome'].values
model=MLPClassifier(hidden_layer_sizes=(100,80,50),max_iter=100000,solver="lbfgs",random_state=3)
model.fit(X,y)
# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))