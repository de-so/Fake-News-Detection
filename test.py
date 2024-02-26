import requests
import json
import pandas as pd
from wordcloud import WordCloud


def scrap(text):
    wordcloud = WordCloud().generate(text)
    # Access the words and their attributes
    words = wordcloud.words_
    keys = list(words.keys())
    result = ' '.join(keys)
    # print(result)

    requestToNewsAPI = requests.get('https://newsapi.org/v2/everything?q=' + result +
                                    '&pageSize=100&apiKey=a33ae10d7b944ea7955342f5c9d68289')
    # print(requestToNewsAPI.status_code)
    # print(requestToNewsAPI.text)
    data = requestToNewsAPI.text
    # print(data)

    parseData = json.loads(data)
    # print(parseData)

    newsName = []
    newsAuthor = []
    newsTitle = []
    newsDescription = []
    newsUrl = []
    newsImageUrl = []
    newsPublishedAt = []
    newsContent = []

    total_result = parseData['totalResults']
    newsArticle = parseData['articles']
    for i in range(len(newsArticle)):
        newsName.append(newsArticle[i]['source']['name'])
        newsAuthor.append(newsArticle[i]['author'])
        newsTitle.append(newsArticle[i]['title'])
        newsDescription.append(newsArticle[i]['description'])
        newsUrl.append(newsArticle[i]['url'])
        newsImageUrl.append(newsArticle[i]['urlToImage'])
        newsPublishedAt.append(newsArticle[i]['publishedAt'])
        newsContent.append(newsArticle[i]['content'])

        df = pd.DataFrame({'News Name': newsName, 'Author Name': newsAuthor, 'News Title': newsTitle,
                           'News Description': newsDescription, 'News URL': newsUrl, 'News Image': newsImageUrl,
                           'PublishedAt': newsPublishedAt, 'News Content': newsContent})
        df.to_csv('ScrapedNews.csv', index=False)
    return total_result
