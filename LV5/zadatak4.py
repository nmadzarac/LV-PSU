#Po uzoru na prethodne zadatke izgradite model logističke regresije. Što primjećujete kod vrednovanja ovog modela? Što
#je uzrok dobivenim rezultatima?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

df = pd.read_csv('C:\\Users\\student\\Desktop\\LV5\\occupancy_processed.csv')

feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'
class_names = ['Slobodna', 'Zauzeta']

X = df[feature_names].to_numpy()
y = df[target_name].to_numpy()

plt.figure()
for class_value in np.unique(y):
    mask = y == class_value
    plt.scatter(X[mask, 0], X[mask, 1], label=class_names[int(class_value)])

logreg = LogisticRegression()
logreg.fit(X, y)

y_pred = logreg.predict(X)

plt.xlabel('S3_Temp')
plt.ylabel('S5_CO2')
plt.title('Zauzetost prostorije')
plt.legend()
plt.show()

print(classification_report(y, y_pred, target_names=class_names))

