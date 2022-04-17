import pandas as pd
from sklearn.linear_model import LogisticRegression


df=pd.read_csv('DATA/diabetes.csv')
df.head()
X=df[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']].values
y=df['Outcome'].values
model=LogisticRegression(solver='newton-cg')
model.fit(X,y)
print('Accuracy = ',model.score(X,y)*100,'%')
print(model.predict([[6,148,72,35,0,33.6,0.627,50]]))
