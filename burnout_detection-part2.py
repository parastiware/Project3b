import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Step 1: Load dataset
# We have a CSV file with columns: 'text' (containing concatenated text from issue title, body, and comments) and 'burnout_label'
data = pd.read_csv('updated_comments.csv')

# Step 2: Data preprocessing
# Assuming you've already performed necessary data cleaning and preprocessing steps

# Step 3: Feature extraction
# Using TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(max_features=1000)  # You can adjust max_features as needed
X = tfidf_vectorizer.fit_transform(data['Text'])
y = data['Burnout']

# Step 4: Splitting dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Model training
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 6: Model evaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred));