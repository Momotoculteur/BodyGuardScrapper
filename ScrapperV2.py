from bs4 import BeautifulSoup
import re
import time
import requests
import urllib3
from multiprocessing.dummy import Pool
from multiprocessing import cpu_count

url = 'https://www.gobodyguard.fr/api/generate_comment.php'

dict = {
    '\\u00e0': 'a',
    '\\u00e2': 'a',
    '\\u00e4': 'a',
    '\\u00C3': 'A',
    '\\u00C2': 'A',
    '\\u00C1': 'A',
    '\\u00C0': 'A',
    '\\u00c0': 'A',
    '\\u00e7': 'c',
    '\\u00c7': 'C',
    '\\u00e8': 'e',
    '\\u00e9': 'e',
    '\\u00ea': 'e',
    '\\u00eb': 'e',
    '\\u00c8': 'E',
    '\\u00C9': 'E',
    '\\u00c9': 'E',
    '\\u00CA': 'E',
    '\\u00CB': 'E',
    '\\u00ee': 'i',
    '\\u00ef': 'i',
    '\\u00ce': 'I',
    '\\u00CC': 'I',
    '\\u00CD': 'I',
    '\\u00CE': 'I',
    '\\u00CF': 'I',
    '\\u00f4': 'o',
    '\\u00f6': 'o',
    '\\u00D2': 'O',
    '\\u00D3': 'O',
    '\\u00D4': 'O',
    '\\u00D5': 'O',
    '\\u00D6': 'O',
    '\\u00f9': 'u',
    '\\u00fb': 'u',
    '\\u00fc': 'u',
    '\\u00D9': 'U',
    '\\u00DA': 'U',
    '\\u00DB': 'U',
    '\\u00DC': 'U',
    '\\u2019': "'",
    '\\u2018': "'",
    '\\u20ac': "euros",
    '\\n': '',
    '&lt;': 'inferieur',
    '&le;': 'inferieur egale',
    '&gt;': 'superieur',
    '&ge;': 'superieur egale',
    '\\u00a0': '',
    '\\u00ab': "'",
    '\\u00bb': "'",
    ',': ' ',
    '\\t': ' ',
    '\\ud83d': '',
    '\\ude09': '',
    '\\ude18': '',
    '\\ude08': ''
}

def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U0001F1F2-\U0001F1F4"  # Macau flag
                               u"\U0001F1E6-\U0001F1FF"  # flags
                               u"\U0001F600-\U0001F64F"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U0001F1F2"
                               u"\U0001F1F4"
                               u"\U0001F620"
                               u"\u200d"
                               u"\u2640-\u2642"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def remove_emoji2(data):
    """
    去除表情
    :param data:
    :return:
    """
    if not data:
        return data
    if not isinstance(data, str):
        return data
    try:
    # UCS-4
        patt = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
    except re.error:
    # UCS-2
        patt = re.compile(u'([\\u2600-\\u27BF])|([\\uD83C][\\uDF00-\\uDFFF])|([\\uD83D][\\uDC00-\\uDE4F])|([\\uD83D][\\uDE80-\\uDEFF])')
    return patt.sub('', data)


def cleanData(text, dict):
    for i, j in dict.items():
        text = text.replace(i, j)
    return text



x=0


while 1:
    file = open('data.txt', 'a')
    time.sleep(1)
    r = requests.get(url)
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, "html.parser", from_encoding='utf-8')

    text = cleanData(str(soup), dict)
    text = str(soup)[9:]
    result = text.partition("insult")[-1]
    result = result[3:]
    result = result[:1]
    text = text.partition("insult")[0]
    text = text[:-3]
    text = cleanData(text, dict)
    text = remove_emoji2(text)

    print('LIGNE NUMERO ' + str(x))
    print('TEXT')
    print(text)
    print('RESULT')
    print(result)
    print('\n')

    file.write(text)
    file.write(',')
    file.write(result)
    file.write('\n')

    file.close()
    x+=1


