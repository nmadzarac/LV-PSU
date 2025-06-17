#Umjesto algoritma K najbližih susjeda koristite stablo odlučivanja te ponovite korake a) do d) iz prethodnog zadatka.
#a) Vizualizirajte dobiveno stablo odlučivanja.
#b) Što se događa s rezultatima ako mijenjate parametar max-depth stabla odlučivanja?
#c) Što se događa s rezultatima ako ne koristite skaliranje ulaznih veličina?

from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

df = pd.read_csv('C:\\Users\\student\\Desktop\\LV5\\occupancy_processed.csv')

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

X = scaled_data[:, :-1]
y = scaled_data[:, -1]

dt = DecisionTreeClassifier(max_depth=2)
dt.fit(X, y)

y_pred = dt.predict(X)

plt.figure(figsize=(12, 8))
plot_tree(dt, filled=True)
plt.show()
