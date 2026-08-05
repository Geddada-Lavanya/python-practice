Problem 1: Solution

import pandas as pd
data = {
    'Name': ['Riya', 'Karan', None, 'Meena', 'Amit', None, 'Sneha', 'Vikas', 'Neha', 'Tina'],
    'Age': [28, 30, 22, None, 26, 21, None, 24, 29, None],
    'Gender': ['F', 'M', 'M', 'F', 'M', 'M', 'F', 'M', 'F', 'F'],
    'Score': [91, None, 76, 84, 89, 95, None, 88, 93, 90]
}

df = pd.DataFrame(data)
df.to_csv('raw_data.csv', index=False)
print("Data saved to 'raw_data.csv'.")

df_read = pd.read_csv('raw_data.csv')
print("\n First 5 rows of the dataset:")
print(df_read.head())

df_dropped = df_read.dropna()
print("\nData after dropping rows with missing values:")
print(df_dropped)

print("\nMissing values in each column:")
print(df_read.isnull().sum())

df_filled = df_read.copy()
df_filled['Name'].fillna('some name', inplace=True)
df_filled['Age'].fillna(21, inplace=True)

print("\n Data after filling missing values:")
print(df_filled)

df_filled.to_csv('cleaned_data.csv', index=False)
print("\nCleaned data saved to 'cleaned_data.csv'.")

Problem 2: Soultion 

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'EmpName': ['Amit', 'Riya', 'Karan', 'Riya', 'Amit', 'Sneha', 'Karan', 'Meena', 'Amit', 'Sneha'],
    'EmpId': [101, 102, 103, 102, 101, 104, 103, 105, 101, 104],
    'EmpSalary': [50000, 60000, 55000, 60000, 50000, 58000, 55000, 52000, 50000, 58000]
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

plt.figure(figsize=(8, 5))
plt.bar(df['EmpName'], df['EmpSalary'], color='skyblue')
plt.title('Original Employee Salaries')
plt.xlabel('Employee Name')
plt.ylabel('Salary')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

duplicates = df[df.duplicated()]
print("\nDuplicate Rows Detected:")
print(duplicates)

df_cleaned = df.drop_duplicates()
print("\n Cleaned Data (Duplicates Removed):")
print(df_cleaned)

plt.figure(figsize=(8, 5))
plt.bar(df_cleaned['EmpName'], df_cleaned['EmpSalary'], color='lightgreen')
plt.title('Cleaned Employee Salaries')
plt.xlabel('Employee Name')
plt.ylabel('Salary')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

Problem 3: Solution

import cv2
import os

video_path = 'downloaded-file.mp4'  # Replace with your video file name
output_folder = 'frames'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

cap = cv2.VideoCapture(video_path)
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_filename = os.path.join(output_folder, f'frame_{frame_count:03d}.jpg')
    cv2.imwrite(frame_filename, frame)
    frame_count += 1

cap.release()
print(f" {frame_count} frames saved to '{output_folder}' folder.")

Problem 4 : solution

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")   # Replace with your image path
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR → RGB for correct display

rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
rotate_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

plt.figure(figsize=(12,8))

plt.subplot(2,3,1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2,3,2)
plt.imshow(rotate_90)
plt.title("Rotated 90°")
plt.axis("off")

plt.subplot(2,3,3)
plt.imshow(rotate_180)
plt.title("Rotated 180°")
plt.axis("off")

plt.subplot(2,3,4)
plt.imshow(rotate_270)
plt.title("Rotated 270°")
plt.axis("off")

plt.subplot(2,3,5)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")

plt.tight_layout()
plt.show()

Problem 5 : Solution

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    'Experience': [1, 2, 3, 4, 5, 6, 8, 10],
    'Salary': [25000, 30000, 35000, 40000, 45000, 50000, 60000, 70000]
}

df = pd.DataFrame(data)

X = df[['Experience']]
y = df['Salary']

model = LinearRegression()
model.fit(X, y)

experience_input = [[7]]
predicted_salary = model.predict(experience_input)
print(f"Predicted Salary for 7 years experience: ₹{predicted_salary[0]:.2f}")

plt.scatter(X, y, color='blue', label='Actual Data')  # Scatter plot of actual data
plt.plot(X, model.predict(X), color='red', label='Regression Line')  # Regression line
plt.scatter(7, predicted_salary, color='green', marker='o', s=100, label='Predicted (7 yrs)')  # Predicted point
plt.title("Salary Prediction based on Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary (₹)")
plt.legend()
plt.grid(True)
plt.show()

Problem 6: Solution

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

data = {
    'StudyHours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Result':       [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]  # 0 = Fail, 1 = Pass
}
df = pd.DataFrame(data)

X = df[['StudyHours']]
y = df['Pass']

model = LogisticRegression()
model.fit(X, y)

y_pred = model.predict(X)
print("Predictions:", y_pred.tolist())

plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict_proba(X)[:,1], color='red', label='Logistic Curve')
plt.title("Logistic Regression: Study Hours vs Pass/Fail")
plt.xlabel("Study Hours")
plt.ylabel("Probability of Passing")
plt.legend()
plt.grid(True)
plt.show()

Problem  7 : Solution 

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, y_pred))
plt.figure(figsize=(15, 10))
plot_tree(
    clf,
    filled=True,
    rounded=True,
    class_names=iris.target_names,
    feature_names=iris.feature_names,
    fontsize=10
)
plt.show()

Program  8: Solution 

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import pandas as pd


nltk.download('punkt_tab')
nltk.download('wordnet')


stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

input_file = "/content/sampletexts.txt"
output_file = "text_processing_results.csv"

data = []

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        sentence = line.strip()
        if sentence == "":
            continue

        
        tokens = word_tokenize(sentence)

        
        stems = [stemmer.stem(word) for word in tokens]

       
        lemmas = [lemmatizer.lemmatize(word) for word in tokens]

        data.append({
            "Original Sentence": sentence,
            "Tokens": " ".join(tokens),
            "Stems": " ".join(stems),
            "Lemmas": " ".join(lemmas)
        })

        
        df_display = pd.DataFrame({
            "Original Sentence": [sentence],
            "Tokens": [" | ".join(tokens)],
            "Stems": [" | ".join(stems)],
            "Lemmas": [" | ".join(lemmas)]
        })

        print("\n=== Sentence Processing ===")
        print(df_display.to_string(index=False))
        print("===========================\n")


df = pd.DataFrame(data)
df.to_csv(output_file, index=False)

print(f"\nAll results saved to: {output_file}")

Program  9: Solution 

import pandas as pd
import re
sentences = [
    "I love natural language processing.",
    "Language models learn from text.",
    "Word embeddings capture semantic meaning.",
    "Natural language processing is fun and powerful."
]

lower_sentences = [s.lower() for s in sentences]

def tokenize(sentence):
    
    sentence = re.sub(r'[^\w\s]', '', sentence) # Removes punctuation using regular expressions.Splits sentences into words (tokens).
    return sentence.split()
tokenized_sentences = [tokenize(s) for s in lower_sentences]
vocab = sorted(list(set([word for sent in tokenized_sentences for word in sent])))
print("Vocabulary:\n", vocab)
bow_matrix = []
for sent in tokenized_sentences:
    word_count = [sent.count(word) for word in vocab]
    bow_matrix.append(word_count)
df_bow = pd.DataFrame(bow_matrix, columns=vocab)
print("\nBag-of-Words Matrix:\n")
print(df_bow)
df_bow.to_csv("bag_of_words_output.csv", index=False)
print("\nSaved as 'bag_of_words_output.csv'")

Program 10 : Solution 

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix
df = pd.read_csv("/content/creditcard (1).csv")
print("Dataset shape:", df.shape)
print(df.head())
df = df.dropna(subset=['Class'])
scaler = StandardScaler()
df['scaled_amount'] = scaler.fit_transform(df[['Amount']])
df['scaled_time'] = scaler.fit_transform(df[['Time']])
df = df.drop(['Amount', 'Time'], axis=1)

X = df.drop('Class', axis=1)
y = df['Class']   # 1 = Fraud, 0 = Normal
iso_forest = IsolationForest(
    n_estimators=100,
    contamination=0.0017,  
    random_state=42
)

y_pred = iso_forest.predict(X)
y_pred_converted = np.where(y_pred == -1, 1, 0)
print("\nConfusion Matrix:")
print(confusion_matrix(y, y_pred_converted))
print("\nClassification Report:")
print(classification_report(y, y_pred_converted))
print("\nTotal predicted fraud cases:", y_pred_converted.sum())
print("Actual fraud cases:", 
output_df = df.copy()
output_df['Actual_Class'] = y.sum))
output_df['Predicted_Class'] = y_pred_converted
output_df.to_csv("isolation_forest_fraud_results.csv", index=False)
print("\nCSV file saved as 'isolation_forest_fraud_results.csv'")

Problem 11 : Solution 

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

ratings = pd.DataFrame({
    'userId':[1,1,2,2,3,3],
    'movieId':[10,20,10,30,20,40],
    'rating':[4,5,5,3,2,4]
})
movies = pd.DataFrame({
    'movieId':[10,20,30,40],
    'title':['Inception','The Matrix','Interstellar','The Dark Knight']
})

user_movie = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)
sim = cosine_similarity(user_movie)
sim_df = pd.DataFrame(sim, index=user_movie.index, columns=user_movie.index)

def recommend(user, n=2):
    scores = {}
    for u in sim_df[user].sort_values(ascending=False).index[1:]:
        for m,r in user_movie.loc[u].items():
            if user_movie.loc[user,m]==0: scores[m]=scores.get(m,0)+r
    top = sorted(scores,key=scores.get,reverse=True)[:n]
    return movies[movies['movieId'].isin(top)]['title'].tolist()

print("Recommendations for User 1:", recommend(2))

Problem 12: Solution 

def chatbot():
    print(" Chatbot: Hello! I am your assistant.")
    print("Type 'bye', 'exit', or 'quit' to end the chat.\n")

    responses = {
        "hello": "Hello! How can I help you?",
        "hi": "Hi there! What can I do for you?",
        "how are you": "I'm doing great! Thanks for asking.",
        "your name": "I am a simple chatbot created using Python.",
        "help": "Sure! I can answer basic questions.",
        "course": "This chatbot is useful for AI and Python projects.",
        "thanks": "You're welcome! ",
        "thank you": "Happy to help!",
        "time": "I cannot tell the current time, but I’m always here for you!",
        "python": "Python is a popular programming language for AI and ML."
    }

    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input in ["bye", "exit", "quit"]:
            print(" Chatbot: Goodbye! Have a nice day.")
            break
        
        response_found = False
        for key in responses:
            if key in user_input:
                print(" Chatbot:", responses[key])
                response_found = True
                break

        if not response_found:
            print(" Chatbot: Sorry, I didn't understand that. Can you rephrase?")

chatbot()




class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row,col=len(board),len(board[0])
        visited=set()
        def backtrack(r,c,i):
            if i==len(word):
                return True
                
            if r<0 or c<0 or r==row or c == col or (r,c) in visited or word[i]!=board[r][c]:
                return False

            visited.add((r,c))
            res=backtrack(r-1,c,i+1) or backtrack(r,c-1,i+1) or backtrack(r+1,c,i+1) or backtrack(r,c+1,i+1)


        for r in range(row):
            for c in range(col):
                if backtrack(r,c,i=0):
                    return True
        return False

        