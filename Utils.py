import re
import datetime


def url_remover(tweet):
    new_tweet = []
    for words in tweet:
        is_url = False
        pattern_count = 0
        for letters in words:
            if letters == 'c' or letters == 'o' or letters == 'm' or letters == '.':
                pattern_count += 1
                if pattern_count == 4:
                    is_url = True
                    break
            else:
                pattern_count = 0
        if not is_url:
            new_tweet.append(words)
    return new_tweet


def tag_and_empty_remover(tweet):
    new_tweet = []
    for words in tweet:
        words = words.translate(str.maketrans('', '', '!\"$%&\'()*+,-./:;<=>?[\]^_`{|}~'))
        should_removed = False
        word_length = len(words)
        if word_length == 0:
            should_removed = True
        elif word_length == 1:
            if words[0] == '\n':
                should_removed = True
        else:
            if words[0] == '@' or words[0] == '#':
                should_removed = True
        if not should_removed:
            new_tweet.append(words)
    return new_tweet


def to_lower(tweet):
    lower_dict = {
        'A': 'a', 'B': 'b', 'C': 'c', 'Ç': 'ç', 'D': 'd', 'E': 'e', 'F': 'f',
        'G': 'g', 'Ğ': 'ğ', 'H': 'h', 'I': 'ı', 'İ': 'i', 'J': 'j', 'K': 'k',
        'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'Ö': 'ö', 'P': 'p', 'Q': 'q',
        'R': 'r', 'S': 's', 'Ş': 'ş', 'T': 't', 'U': 'u', 'Ü': 'ü', 'V': 'v',
        'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'
    }
    n_tweet = []
    for word in tweet:
        n_word = ''
        for letter in word:
            if letter in lower_dict.keys():
                letter = lower_dict.get(letter)
            n_word += letter
        n_tweet.append(n_word)
    return n_tweet


def replace_emoticon(tweet):
    new_tweet = []
    for word in tweet:
        check_pos = re.findall(r'(?::\)|:-\)|=\)|:D|:d|<3|\(:|:\'\)|\^\^|;\)|\(-:)', word)
        check_neg = re.findall(r'(:-\(|:\(|;\(|;-\(|=\(|:/|:\\|-_-|\):|\)-:)', word)
        if check_pos:
            word = "xgülücük"
        elif check_neg:
            word = "xüzülcük"
        new_tweet.append(word)
    return new_tweet


def remove_repeating_char(tweet):
    new_tweet = []
    for word in tweet:
        new_word = ""
        prev_char = ''
        for char in word:
            if prev_char == char:
                continue
            new_word = new_word + char
            prev_char = char
        new_tweet.append(new_word)
    return new_tweet


def time_formatter(time):
    return time.split()[0]


def turn_to_time(time, period_of_days):
    date = time.split("-")
    year = int(date[0])
    month = int(date[1])
    day = int(int(date[2]) / period_of_days)
    if day == 0:
        day = 1
    else:
        day *= period_of_days
    y = datetime.date(year, month, day)
    return y
