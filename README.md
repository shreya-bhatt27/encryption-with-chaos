# encryption-with-chaos
This repository consists the codebase for our term project for the course Order and Chaos (IIT KGP) titled 'Image Encryption using Chaotic systems'.

# Image Encryption using Chaos

This project demonstrates image encryption using chaotic systems such as the Rössler, Lorenz, and Langford systems. Chaotic systems are utilized to generate pseudorandom sequences, which are then employed for encrypting images.

## Table of Contents
- [Introduction](#introduction)
- [Instructions](#instructions)
  - [Running the Project](#running-the-project)
  - [Downloading the Tiny Image Dataset](#downloading-the-tiny-image-dataset)
  - [Running for Test Image](#running-for-test-image)
- [Results](#results)
  - [Example Image](#example-image)
- [Phase Portraits](#phase-portraits)

## Introduction

In this project, we utilize chaotic systems—specifically the Rössler, Lorenz, and Langford systems to generate chaotic sequences. These sequences are then employed in encrypting images. The encryption process involves changing the pixel values of an image using the numbers generated from chaotic sequences, thereby scrambling the image content.

## Instructions

### Running the Project

To run the project, run the following lines on terminal.
```
git clone https://github.com/shreya-bhatt27/encryption-with-chaos
cd encryption-with-chaos
mkdir tiny-imagenet-200
```
Then download the Tiny Image Dataset from their official web page, copy and paste the required number of images (we took 1000 images for our study) from the dataset into the tiny-imagenet-200 folder created in the previous step.
Then to run the encryption code over the test images, and calculate the required metrics, run the following lines on terminal.
```
python loop_cp.py
```

### Running code for a Test Image

To run the encryption process for a test image:
```
python ec.py
```
Give the path to your image in the interactive bar. You can then visualize the encrypted and decrypted images.

## Results

### Example Image

Here's an example of an encrypted image using the Rössler chaotic system:

![Encrypted Image](example_encrypted_image.jpg)

## Phase Portraits

Phase portraits for the Rössler, Lorenz, and Aizawa systems have been plotted using the RK4 method. These phase portraits provide insights into the behavior of the chaotic systems used for encryption. The code for the plots is in the phase_portraits.ipynb file

