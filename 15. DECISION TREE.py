
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def get_user_input():
    sepal_length = float(input("Enter sepal length: "))
    sepal_width = float(input("Enter sepal width: "))
    petal_length = float(input("Enter petal length: "))
    petal_width = float(input("Enter petal width: "))
    return [sepal_length, sepal_width, petal_length, petal_width]

def main():
    # Load Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train decision tree classifier
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    # Evaluate classifier
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    # Get user input
    user_input = [get_user_input()]

    # Make prediction for user input
    prediction = clf.predict(user_input)
    print("Predicted class:", prediction[0])
    print("Predicted class name:", iris.target_names[prediction[0]])

if __name__ == "__main__":
    main()
