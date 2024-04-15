import os
import numpy as np
import matplotlib.image as img
from skimage.metrics import structural_similarity
import cp 
import rosslerSystem as key_rossler
import lorenzSystem as key_lorenz
import langfordSystem as key_langford


# Load Tiny ImageNet dataset
dataset_path = "./tiny-imagenet-200/test/"
image_files = os.listdir(dataset_path)

ssim_values_rossler = []
ssim_values_lorenz = []
ssim_values_langford = []
i = 0

for image_file in image_files:
    image_path = os.path.join(dataset_path, image_file)
    original_image = img.imread(image_path)
    

    if original_image.shape == (64, 64, 3):
        print(i+1)
        i = i+1

        # Generate encrypted images using each chaotic model
        encrypted_image_rossler = cp.generate_and_encrypt_image(image_path, key_rossler.rossler_key)
        encrypted_image_lorenz = cp.generate_and_encrypt_image(image_path, key_lorenz.lorenz_key)
        encrypted_image_langford = cp.generate_and_encrypt_image(image_path, key_langford.langford_key)

        # Compute SSIM for each pair of original and encrypted images
        ssim_rossler = structural_similarity(original_image, encrypted_image_rossler, channel_axis = -1, multichannel=True)
        ssim_lorenz = structural_similarity(original_image, encrypted_image_lorenz, channel_axis = -1, multichannel=True)
        ssim_langford = structural_similarity(original_image, encrypted_image_langford, channel_axis = -1, multichannel=True)

        # Append SSIM values to the lists
        ssim_values_rossler.append(ssim_rossler)
        ssim_values_lorenz.append(ssim_lorenz)
        ssim_values_langford.append(ssim_langford)

# Calculate statistics
average_ssim_rossler = np.mean(ssim_values_rossler)
variance_ssim_rossler = np.var(ssim_values_rossler)
average_ssim_lorenz = np.mean(ssim_values_lorenz)
variance_ssim_lorenz = np.var(ssim_values_lorenz)
average_ssim_langford = np.mean(ssim_values_langford)
variance_ssim_langford = np.var(ssim_values_langford)

# Print statistics
print("Average SSIM for Rossler's Chaos:", average_ssim_rossler)
print("Variance of SSIM for Rossler's Chaos:", variance_ssim_rossler)
print("Average SSIM for Lorenz's Chaos:", average_ssim_lorenz)
print("Variance of SSIM for Lorenz's Chaos:", variance_ssim_lorenz)
print("Average SSIM for Langford's Chaos:", average_ssim_langford)
print("Variance of SSIM for Langfords's Chaos:", variance_ssim_langford)