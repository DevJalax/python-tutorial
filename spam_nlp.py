from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import ensemble 
from sklearn.metrics import classification_report, accuracy_score

text = ["the moon is white", "the sun is yellow", "the moon and the sun are planets"]
#instantiate the class
cv = CountVectorizer()
#tokenize and build vocab
cv.fit(text)
print(cv.vocabulary_)
#transform the text
vector = cv.transform(text)
print(vector.toarray())

text_vec = CountVectorizer().fit_transform(df['text'])
X_train, X_test, y_train, y_test = train_test_split(text_vec, df['spam'], test_size = 0.45, random_state = 42, shuffle = True)

classifier = ensemble.GradientBoostingClassifier(
    n_estimators = 100, #how many decision trees to build
    learning_rate = 0.5, #learning rate
    max_depth = 6
)

classifier.fit(X_train, y_train)
predictions = classifier.predict(X_test)
print(classification_report(y_test, predictions))
