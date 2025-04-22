import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

class RandomForestModel:
    def __init__(self):
        if model:
            self.model = model
        else:
            RandomForestClassifier()

    def train_model(self, x_train, y_train):
        self.model.fit(x_train, y_train)

    def create_prediction(self, x_test):
        return self.model.predict(x_test)

    def evaluate_model(self, x_test, y_test):
        y_hat = self.predict(x_test)
        accuracy = accuracy_score(y_test, predictions)
        evaluation = {
            "Classification Report" : classification_report(y_test, y_hat),
            "Confusion Matrix Visualization" : confusion_matrix(y_test, predictions),
            "Accuracy Score" : accuracy
        }
        return evaluation

    def save_model(self, path = "BestModelOOP.pkl"):
        try:
            with open(path, "wb") as file:
                pickle.dump(self.model, file)
        except:
            print("Cannot saving model due some error")

    def load_model(self, path = "BestModelOOP.pkl"):
        try :
            with open(path, "rb") as file:
                self.model = pickle.load(file)
            print(f"Model Successfully load from {path} file!")
        except :
            print("Error on Loading Model!")