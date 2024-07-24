import requests

api_key = "7dd4541b873c4df4853d279dd12b6e20"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-06-24&sortBy=publishedAt&apiKey=7dd4541b873c4df4853d279dd12b6e20"


get_req = requests.get(url)
content = get_req.json()
for article in content['articles']:
    print(article['title'])