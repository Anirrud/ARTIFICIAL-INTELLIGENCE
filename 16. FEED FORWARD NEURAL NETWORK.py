from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
import numpy as np

def get_user_input():
    input_data = []
    for i in range(4):
        value = float(input(f"Enter input {i+1}: "))
        input_data.append(value)
    return input_data

def main():
    # Load Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Normalize input data
    scaler = StandardScaler()
    X_normalized = scaler.fit_transform(X)

    # Train the MLP classifier
    clf = MLPClassifier(hidden_layer_sizes=(8, 8), activation='relu', solver='adam', max_iter=2000)
    clf.fit(X_normalized, y)

    # Get user input
    user_input = np.array([get_user_input()])
    user_input_normalized = scaler.transform(user_input)

    # Make prediction for user input
    prediction = clf.predict(user_input_normalized)
    class_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    predicted_class = class_names[prediction[0]]

    print("Predicted class:", predicted_class)

if __name__ == "__main__":
    main()
