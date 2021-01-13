# twitter-sentiment-analysis
Sentiment Analysis to Turkish Tweets

This project includes Twitter scraper, and preprocess of tweeets, and analysis of tweets using MNB, KNN, and SVM algortihms by using Sci-Kit learn.

# Twitter Scraper
* This scraper works with using selenium and beautifulsoup libraries.
* However you could check https://github.com/JustAnotherArchivist/snscrape which offers much better way to scrape tweets currently.

# Preprocess
* Remove URL's
* Replace emoticons
* Remove Tags
* Remove Punctuation
* Lowercase all strings
* Remove repeating characters
* I used Zemberek-NLP https://github.com/ahmetaa/zemberek-nlp for Lemmatization.

# Analysis 
I used Sci-Kit library to analyze tweets.
