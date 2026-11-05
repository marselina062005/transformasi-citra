
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Membaca gambar asli
gambar = cv2.imread("foto_asli.png")

if gambar is None:
    print("Gambar tidak ditemukan!")
    exit()

tinggi, lebar = gambar.shape[:2]

# 1. Translation
matriks = np.float32([[1, 0, 50], [0, 1, 30]])
translation = cv2.warpAffine(gambar, matriks, (lebar, tinggi))

# 2. Scaling
scaling_05 = cv2.resize(gambar, None, fx=0.5, fy=0.5)
scaling_2 = cv2.resize(gambar, None, fx=2, fy=2)

# 3. Rotation
pusat = (lebar // 2, tinggi // 2)

rotasi_45 = cv2.warpAffine(
    gambar,
    cv2.getRotationMatrix2D(pusat, 45, 1),
    (lebar, tinggi)
)

rotasi_90 = cv2.rotate(gambar, cv2.ROTATE_90_CLOCKWISE)
rotasi_180 = cv2.rotate(gambar, cv2.ROTATE_180)

# 4. Horizontal Flip
horizontal = cv2.flip(gambar, 1)

# 5. Vertical Flip
vertical = cv2.flip(gambar, 0)

# Menyimpan hasil transformasi
os.makedirs("hasil_transformasi", exist_ok=True)

hasil = {
    "translation": translation,
    "scaling_05": scaling_05,
    "scaling_2": scaling_2,
    "rotation_45": rotasi_45,
    "rotation_90": rotasi_90,
    "rotation_180": rotasi_180,
    "horizontal_flip": horizontal,
    "vertical_flip": vertical
}

for nama, citra in hasil.items():
    cv2.imwrite(f"hasil_transformasi/{nama}.png", citra)

print("Transformasi citra berhasil!")
print("Semua hasil tersimpan di folder hasil_transformasi.")
