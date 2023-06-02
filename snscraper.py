import snscrape.modules.twitter as sntwitter

wordsList = ['kaşık', 'rölanti', 'siyah', 'kayna', 'taş', 'bir', 'kot',
             'haber', 'gez', 'mahya', 'teşkilat', 'sayım', 'çal', 'silindir', 'şapka',
             'sindirim', 'sistemi', 'boğaz', 'kavga', 'toz']
timeList = []

with open('Tweets-8-Jan.txt', 'w') as text_file:
    for time in timeList :
        for word in wordsList:
            for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'"{word}" -canım -masaj -seks -sevişme lang:tr until:{time} -filter:links -filter:replies').get_items()):
                content = tweet.content.replace('\n', '')
                content = content.replace(',', ' ')
                print(f'{content},{tweet.date}', file=text_file)
                if i > 100:
                    break
            print('\tWord Finished')
        print('\tTime Finished')