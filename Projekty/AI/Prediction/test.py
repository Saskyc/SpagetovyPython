import random
import time
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

print("Hello world")

# ----- Model -----

model = keras.Sequential([
    layers.Input(shape=(1,)),
    layers.Dense(8, activation="relu"),
    layers.Dense(3, activation="softmax")  # outputs probs for 1,2,3
])

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.01),
    loss="sparse_categorical_crossentropy"
)

# ----- Helpers -----

def predict(x: int) -> int:
    x_arr = np.array([[x]], dtype=np.float32)
    probs = model(x_arr, training=False).numpy()[0]
    return int(np.argmax(probs)) + 1  # back to 1,2,3

def train(x: int, target: int):
    x_arr = np.array([[x]], dtype=np.float32)
    y_arr = np.array([target - 1], dtype=np.int32)  # labels must be 0-based
    model.train_on_batch(x_arr, y_arr) 

# ----- Stats -----

total = 0
right = 0
wrong = 0

print("Loop")

# ----- Online loop -----

while True:
    x = random.randrange(1, 4)

    prediction = predict(x)
    print(f"Input: {x} | Prediction: {prediction}")

    correct = (prediction == x)

    # This is the key part:
    # - if correct → reinforce prediction
    # - if wrong → train toward the true value (x)
    train(x, x)

    total += 1
    if correct:
        right += 1
    else:
        wrong += 1

    acc = right / total
    print(f"Total: {total} | Right: {right} | Wrong: {wrong} | Acc: {acc:.2f}\n")

    time.sleep(1)
