import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import langfordSystem as key

path = str(input('Path to image: \n'))
image = img.imread(path)

plt.imshow(image)
plt.show()

height = image.shape[0]
width = image.shape[1]

x, y, keys = key.langford_key(0.1, 1.0, 0.01, height*width)
print(height*width)
l = 0

encryptedImage = np.zeros(shape=[height, width, 3], dtype=np.uint8)

for i in range(height):
    for j in range(width):
        zk = (int((keys[l]*pow(10, 5))%256))
        encryptedImage[i, j] = image[i, j]^zk
        l += 1

plt.imshow(encryptedImage)
plt.show()

decryptedImage = np.zeros(shape=[height, width, 3], dtype=np.uint8)

l = 0
for i in range(height):
    for j in range(width):
        zk = (int((keys[l]*pow(10, 5))%256))
        decryptedImage[i, j] = encryptedImage[i, j]^zk
        l += 1

plt.imshow(decryptedImage)
plt.show()