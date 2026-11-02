import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
df = pd.read_csv("emails.csv")
print("Dataset Loaded Successfully!\n")
print(df.head())

# ✅ Clean column names (remove spaces and hidden chars)
df.columns = df.columns.str.strip()

# ✅ Identify the target column robustly
target_col = None
for col in df.columns:
    if col.lower().strip() in ['prediction', 'spam', 'label']:
        target_col = col
        break

if target_col is None:
    raise Exception("Target column not found! Ensure 'Prediction' exists in CSV.")

print(f"\nTarget Column Detected: {target_col}")

# ✅ Extract target and convert to numeric
y = pd.to_numeric(df[target_col], errors='coerce')

# ✅ Convert all non-zero values to 1 (spam)
y = (y > 0).astype(int)

# ✅ Drop target + non-data columns
df.drop(columns=[target_col, 'Email No.'], errors='ignore', inplace=True)

# ✅ Features
X = df

print("\nClass distribution after conversion:")
print(y.value_counts())

# ✅ Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ KNN model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

# ✅ SVM model
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)

def evaluate_model(y_true, y_pred, model_name):
    print(f"\n---- {model_name} ----")
    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("\nConfusion Matrix:\n", confusion_matrix(y_true, y_pred))
    print("\nClassification Report:\n", classification_report(y_true, y_pred, zero_division=0))

# ✅ Evaluate both models
evaluate_model(y_test, y_pred_knn, "KNN Classifier")
evaluate_model(y_test, y_pred_svm, "SVM Classifier")
