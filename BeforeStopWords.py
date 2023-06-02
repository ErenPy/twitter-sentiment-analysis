import Utils
import pandas


# Create Data Frame Including Raw Data and Raw Time use The Scraped Twitter Data
df = pandas.read_csv('????????', lineterminator='\n', columns=["Tweets", "Time"])
tweets = df.Tweets

# Ready to Lemmatization
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

# Remove Repeating Tweets
df_BL = pandas.DataFrame(new_tweet_set, columns=["BeforeLemma"])
df = df.join(df_BL)
index = df.BeforeLemma.drop_duplicates(keep='first').index
df = df.loc[index]
df = df.reset_index()
del df["index"]

# Create File to Send Lemma
with open('ready-to-lemma.txt', 'w') as f:
    for item in df.BeforeLemma:
        f.write("%s\n" % item)

# Check The Lemma Process is Finished
input("If You Made Lemma Files Ready Press Any Key...")

# Create New DataFrame from Lemmatized Output and ML Results
df_Lem = pandas.read_csv('Desktop/twitter-research/After-15-Dec/output2.txt', names=["Lemma"], skip_blank_lines=False)
df = df.join(df_Lem)
df_Lab = pandas.read_csv('Desktop/twitter-research/After-15-Dec/file2.txt', names=["Labels"])
df = df.join(df_Lab)

# Fix Time Input
list2 = []
for time in df.Time:
    list2.append(Utils.time_formatter(time))

df.Time = list2
