from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
import numpy as np

# Initial tiny dataset to kick things off
texts = [
    "I love this!",
    "You are awful",
    "This is so good",
    "I hate this"
]
labels = [0, 1, 0, 1]  # 0 = non-toxic, 1 = toxic

# Create vectorizer
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(texts)

# Create online classifier
clf = SGDClassifier(
    loss="log_loss",
    learning_rate="constant",
    eta0=0.01,
    max_iter=1,
    tol=None
)

classes = np.array([0, 1])
clf.partial_fit(X_train, labels, classes=classes)

# --- ONLINE LOOP ---
while True:
    # Step 1: Get input
    sentence = input("\nWrite a sentence: ").strip()
    if sentence.lower() in ["exit", "quit"]:
        break

    # Step 2: Convert to numeric vector
    X_new = vectorizer.transform([sentence])

    # Step 3: Predict toxicity
    pred = clf.predict(X_new)[0]
    print(f"Prediction: {'TOXIC' if pred == 1 else 'NON-TOXIC'}")

    # Step 4: Ask for feedback
    while True:
        feedback = input("Was it toxic? (y/n): ").strip().lower()
        if feedback in ["y", "n"]:
            break
        print("Please enter 'y' or 'n'.")

    true_label = 1 if feedback == "y" else 0

    # Step 5: Teach the model immediately
    clf.partial_fit(X_new, [true_label])
    print("✅ Model updated with your feedback!")
