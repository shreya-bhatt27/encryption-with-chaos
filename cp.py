import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from skimage.metrics import structural_similarity
from scipy.stats import entropy
import rosslerSystem as key_rossler
import lorenzSystem as key_lorenz
import langfordSystem as key_langford
import random 


def generate_and_encrypt_image(image_path, chaos_model_func):
    image = img.imread(image_path)
    height, width, _ = image.shape

    x, y, keys = chaos_model_func(random.uniform(0.0, 2.0),random.uniform(0.0, 2.0), random.uniform(0.0, 2.0), height * width)

    encrypted_image = np.zeros(shape=[height, width, 3], dtype=np.uint8)
    l = 0
    for i in range(height):
        for j in range(width):
            zk = int((keys[l] * pow(10, 5)) % 256)
            encrypted_image[i, j] = image[i, j] ^ zk
            l += 1

    return encrypted_image


def calculate_metrics(original_image, encrypted_image):
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(original_image)

    plt.subplot(1, 2, 2)
    plt.title("Encrypted Image")
    plt.imshow(encrypted_image)
    plt.show()

    entropy_original = entropy(original_image.ravel())
    entropy_encrypted = entropy(encrypted_image.ravel())

    print("Entropy of Original Image:", entropy_original)
    print("Entropy of Encrypted Image:", entropy_encrypted)

    ssim_index = structural_similarity(original_image, encrypted_image, channel_axis = -1, multichannel=True)
    print("SSIM between Original and Encrypted Image:", ssim_index)