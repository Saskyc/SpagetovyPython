#https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html
# Authors: The scikit-learn developers
# SPDX-License-Identifier: BSD-3-Clause

# Standard scientific Python imports
import matplotlib.pyplot as plt

# Import datasets, classifiers and performance metrics
from sklearn import datasets, metrics, svm
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title("Training: %i" % label)

# flatten the images
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Create a classifier: a support vector classifier
clf = svm.SVC(gamma=0.001)

# Split data into 50% train and 50% test subsets
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False
)

# Learn the digits on the train subset
clf.fit(X_train, y_train)

# Predict the value of the digit on the test subset
predicted = clf.predict(X_test)

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, prediction in zip(axes, X_test, predicted):
    ax.set_axis_off()
    image = image.reshape(8, 8)
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    ax.set_title(f"Prediction: {prediction}")

print(
    f"Classification report for classifier {clf}:\n"
    f"{metrics.classification_report(y_test, predicted)}\n"
)

from PIL import Image
import numpy as np

import os
directory = os.path.join(os.getcwd(), "images")

#Create lists for images and labels
images = []
labels = []


for label in os.listdir(directory):
    label_path = os.path.join(directory, label)
    if not os.path.isdir(label_path):
        print("This is not directory", label_path)
        continue
    print("This is directory", label_path)

    for file in os.listdir(label_path):
        img_path = os.path.join(label_path, file)
        if(img_path.endswith(".db")):
            continue
        #Load image
        img = Image.open(img_path).convert("L") # grayscale
        img = img.resize((8, 8)) #give in tuple 8x8 pixels

        #Converting to numpy
        img_array = np.array(img, dtype = np.float32)

        #Normalize Like sklearn digits (0-16 range), so the datasets match
        img_array = (img_array / 255.0) * 16.0

        print("Trying to predict in label", label_path, "|", "in picture:", img_path)

        sample = img_array.reshape(1, -1)  # (1, 64)
        print("Prediction is:", clf.predict(sample))
        print("Prediction is:", clf.predict(sample))
        print("Prediction is:", clf.predict(sample))

        images.append(img_array)
        labels.append(int(label))