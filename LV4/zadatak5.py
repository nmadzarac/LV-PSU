#Potrebno je izgraditi model koji procjenjuje cijenu automobila na temelju numeričkih ulaznih veličina.
#1. Izbacite veličine koje nisu potrebne poput imena automobila. Koriste pandas funkciju df.drop.
#2. Podijelite skup na train i test u omjeru 80% – 20%. Koristite ugrađenu sklearn funkciju:
#from sklearn.model_selection import train_test_split
#3. Skalirajte ulazne podatke korištenjem sklearn funkcija:
#from sklearn.preprocessing import MinMaxScaler, StandardScaler
#4. Odredite parametre linearnog regresijskog modela.
#5. Evaluirajte izgrađeni model na trening i testnom skupu pomoću sklearn funkcija:
#from sklearn.metrics import mean_absolute_error, r2_score,
#mean_squared_error, max_error
#6. Što se događa s pogreškom na testnom skupu kada mijenjate broj ulaznih veličina?


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error, max_error


df = pd.read_csv('cars_processed.csv')
print(df.info())

X = df[['km_driven', 'year', 'engine', 'max_power']]
y = df['selling_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=300)

Scaler = StandardScaler()
X_train_s = Scaler.fit_transform(X_train)
X_test_s = Scaler.transform(X_test)

linear_model = LinearRegression()
linear_model.fit(X_train_s, y_train)

y_pred_train = linear_model.predict(X_train_s)
y_pred_test = linear_model.predict(X_test_s)

print("R2 test", r2_score(y_pred_test, y_test))
print("RMSE test:", np.sqrt(mean_squared_error(y_pred_test, y_test)))
print("Max error test:", max_error(y_pred_test, y_test))
print("MAE test:", mean_absolute_error(y_pred_test, y_test))
y_pred_rupee = np.exp(y_pred_test)
y_test_rupee = np.exp(y_test)
print("TRUE RMSE",np.sqrt(mean_squared_error(y_pred_rupee, y_test_rupee)))
print("TRUE MAE",mean_absolute_error(y_pred_rupee, y_test_rupee))

fig = plt.figure(figsize=[13, 10])
ax = sns.regplot(y_pred_test, y_test, line_kws={'color': 'green'})
ax.set(xlabel = 'Predikcija', ylabel = 'Stvarna vrijednost', title='Rezultati na testnim podacima')
plt.show()
