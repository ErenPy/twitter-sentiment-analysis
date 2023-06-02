import snscrape.modules.twitter as sntwitter
import csv


accounts_list = []
with open('names.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        for elements in row:
            accounts_list.append(elements)

with open('Tweets-13-Jan.txt', 'a') as text_file:
    for account in accounts_list:
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'(from:{account}) -filter:links -filter:replies').get_items()):
            content = tweet.content.replace('\n', '')
            content = content.replace(',', ' ')
            content = content.replace('\'', ' ')
            content = content.replace('\"', ' ')
            print(f'{content},{tweet.date}', file=text_file)
            if i > 2000:
                break
        print('Account Finished')
