from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn import metrics
import numpy as np
import pandas as pd
import Utils


labeled_df = pd.read_csv("~/Desktop/twitter-research/After-15-Dec/data-labeled-500.csv",
                             lineterminator='\n', names=['Tweets', 'Labels'])
print(labeled_df)
tweets = labeled_df.Tweets
new_tweet_set = []
for tweet in tweets:
    text = tweet.split()
    text = Utils.url_remover(text)
    text = Utils.replace_emoticon(text)
    text = Utils.tag_and_empty_remover(text)
    text = Utils.to_lower(text)
    text = Utils.remove_repeating_char(text)

    new_tweet = ''
    for words in text:
        new_tweet += words + ' '
    new_tweet_set.append(new_tweet)

text_clf = Pipeline([('vect', CountVectorizer(ngram_range=(1, 2), token_pattern=r'\b\w+\b', min_df=1)),
                     ('tfidf', TfidfTransformer()), ('clf', MultinomialNB())])

# Before Lemma
text_clf.fit(new_tweet_set, labeled_df.Labels)

predicted = text_clf.predict(new_tweet_set)
actual = labeled_df.Labels

right = 0
count = 0
predictions = []
for p in predicted:
    predictions.append(p)
    print("Predicted: " + str(p) + "\n")
    if int(actual[count]) == int(p):
        right += 1
    count += 1

print(np.mean(predicted == actual))
print(metrics.confusion_matrix(actual, predicted))
print("Accuracy: " + str((float(right)/len(actual)) * 100))