import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

# Load dataset (adjust path if needed)
data = pd.read_csv('scripts/fake_account__data_dict.csv')

# Example: assuming these are the feature columns
feature_columns = ['profile_pic', 'num_posts', 'followers', 'following', 'bio_length', 'is_private']
X = data[feature_columns]

# Target column (1 = fake, 0 = real)
y = data['label']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save the trained model
os.makedirs('server/models', exist_ok=True)
joblib.dump(model, 'server/models/fake_profile_model.pkl')
print("Model saved to server/models/fake_profile_model.pkl")
