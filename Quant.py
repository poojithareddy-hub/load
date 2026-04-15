import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("image.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
levels = [2, 4, 8]
plt.figure(figsize=(10, 4))
plt.subplot(1, 4, 1)
plt.title("Original")
plt.imshow(image)
plt.axis("off")
for i, L in enumerate(levels):
delta = 256 // L
quantized = (image // delta) * delta
plt.subplot(1, 4, i + 2)
plt.title(f"L = {L}")
plt.imshow(quantized)
plt.axis("off")
plt.tight_layout()
plt.show()
