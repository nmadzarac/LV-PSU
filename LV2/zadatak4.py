import numpy as np
import matplotlib.pyplot as plt

def check(kvadrat, redovi, stupci):
    crne = np.zeros((kvadrat, kvadrat))
    bijele = np.ones((kvadrat, kvadrat)) * 255
    red1 = np.hstack([crne, bijele] * (stupci // 2))
    if stupci % 2 != 0:
        red1 = np.hstack([red1, crne])
    red2 = np.hstack([bijele, crne] * (stupci // 2))
    if stupci % 2 != 0:
        red2 = np.hstack([red2, bijele])
    polje = np.vstack([red1, red2] * (redovi // 2))
    if redovi % 2 != 0:
        polje = np.vstack([polje, red1])
    return polje

img = check(50, 4, 5)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()
