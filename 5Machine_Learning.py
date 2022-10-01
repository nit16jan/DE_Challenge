import pandas as pd
from sklearn import model_selection
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv(r'C:\Downloads\car.data',header=None)
dict = {0: 'buying',1: 'maint',2: 'doors',
       3:'persons',4:'lug_boot',5:'safety',6:'class'}
df.rename(columns=dict,
          inplace=True)
df[['maint','doors','persons','lug_boot','safety','class']]
str_cols = df.columns[df.dtypes.eq('object')]

#Converting string values to integers for model training
clfs = {c:LabelEncoder() for c in str_cols}
for col, clf in clfs.items():
    df[col] = clfs[col].fit_transform(df[col])

# print(clfs['safety'].inverse_transform(df['safety']))

#Split data for training(70%) and testing(30%)
features_train, features_test, label_train, label_test = model_selection.train_test_split(df[['maint','doors','lug_boot','safety','class']],
                                                                          df['buying'], test_size=0.3,random_state=42)


#Import Model 
# tried Naive Bayes, SVC and Adaboost. Adaboost gave max accuracy 

from sklearn.ensemble import AdaBoostClassifier

#Create a  Classifier
clf = AdaBoostClassifier(n_estimators=50, random_state=0)

#Train the model using the training sets
clf.fit(features_train, label_train)

#Predict the response for test dataset
label_pred = clf.predict(features_test)

from sklearn import metrics

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(label_test, label_pred))

# Predict Buying for
# Maintenance = High (LabelEncoder = 0)
# Number of doors = 4 (LabelEncoder = 2)
# Lug Boot Size = Big (LabelEncoder = 0)
# Safety = High  (LabelEncoder = 0)
# Class Value = Good  (LabelEncoder = 1)

print(clf.predict([[0, 2, 0, 0, 1]])) #Output is 1 (Decoded buying value "high") 

