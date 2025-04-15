import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

def load_data(csv_file):
    # For demonstration, assume processed_profiles.csv has columns:
    # 'activity_score', 'completeness', 'language_score', 'engagement', 'label'
    data = pd.read_csv(csv_file)  # Use the csv_file parameter
    X = data[['activity_score', 'completeness', 'language_score', 'engagement']]
    y = data['label']  # 0 for Real, 1 for Fake
    return X, y

def train_model(X, y):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the Random Forest classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # Predict on the test set and evaluate the model
    y_pred = clf.predict(X_test)
    print("Model Evaluation:\n", classification_report(y_test, y_pred))
    
    return clf

if __name__ == '__main__':
    # Load the processed CSV file
    X, y = load_data('processed_profiles.csv')
    
    # Train the model
    model = train_model(X, y)
    
    # Save the model to the model directory (ensure that the '../model/' folder exists)
    joblib.dump(model, '../model/fake_profile_model.pkl')
    print("Model saved to ../model/fake_profile_model.pkl")
