import joblib
import pandas as pd
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix


def accuracy():
    data = pd.read_csv('data_test.csv')
    data_test, label_test = data['text'], data['label']
    text_vector = joblib.load('models/vectorizer.joblib')
    model = joblib.load('models/trained_model.joblib')
    x_test_tfidf = text_vector.transform(data_test)
    predictions = model.predict(x_test_tfidf)
    acc = accuracy_score(label_test, predictions)
    print("Accuracy:", acc)
    cm = confusion_matrix(label_test, predictions)
    print(cm)

    # Assuming cm is your confusion matrix
    # Create a heatmap using Seaborn
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, cmap='Blues', fmt='g')
    plt.text(0.5, 0.9, 'True Negative', horizontalalignment='center', verticalalignment='center', fontsize=12)
    plt.text(1.5, 1.9, 'True Positive', horizontalalignment='center', verticalalignment='center', fontsize=12, color='white')
    plt.text(0.5, 1.9, 'False Negative', horizontalalignment='center', verticalalignment='center', fontsize=12)
    plt.text(1.5, 0.9, 'False Positive', horizontalalignment='center', verticalalignment='center', fontsize=12)

    # # Accuracy Score
    # plt.text(0.5, -0.2, f'Accuracy: {acc:.2f}', ha='center', fontsize=12, transform=plt.gca().transAxes)

    # Add labels, title, and axis ticks
    plt.xlabel('Predicted labels')
    plt.ylabel('True labels')
    plt.title('Confusion Matrix')
    plt.show()


accuracy()

# Train Model Link
# https://colab.research.google.com/drive/12hgP6aB-vFBX7JWUlvnHZoBwg3D5-SzG?usp=sharing
# https://assets.researchsquare.com/files/rs-3156168/v1/f87824c6-4d9e-4f19-a27f-818a851b1de9.pdf?c=1689691469
