import numpy as np
import matplotlib.pyplot as plt

slika = plt.imread("C:\\Users\\Nikola\\Desktop\\LV2\\tiger.png")
slika_gray = slika[:, :, 0].copy()

slika_svjetlija = slika_gray + 0.6
slika_svjetlija[slika_svjetlija > 1] = 1

plt.figure()
plt.title("a) Posvjetljena slika")
plt.imshow(slika_svjetlija, cmap="gray")

slika_rotirana = np.rot90(slika_gray, k=3)
plt.figure()
plt.title("b) Rotacija 90°")
plt.imshow(slika_rotirana, cmap="gray")

slika_zrcalo = np.fliplr(slika_gray)
plt.figure()
plt.title("c) Zrcaljena slika")
plt.imshow(slika_zrcalo, cmap="gray")

slika_manjarez = slika_gray[::10, ::10]
plt.figure()
plt.title("d) Smanjena rezolucija (10x)")
plt.imshow(slika_manjarez, cmap="gray")

visina, sirina = slika_gray.shape
start = sirina // 4
end = sirina // 2
slika_cetvrtina = np.zeros_like(slika_gray)
slika_cetvrtina[:, start:end] = slika_gray[:, start:end]

plt.figure()
plt.title("e) Druga četvrtina slike")
plt.imshow(slika_cetvrtina, cmap="gray")
plt.show()
