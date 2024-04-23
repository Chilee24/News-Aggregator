from ntscraper import Nitter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# scraper = Nitter(log_level=1, skip_instance_check=False)


def crawl_tweet(name, mode, amount, file_name):
    list_tweet = scraper.get_tweets(
        name, mode=mode, number=amount, max_retries=100)

    with open(file=f'news-aggregator\\\\recourse\\\\data\\\\{file_name}.json', mode='w') as file_json:
        json.dump(list_tweet['tweets'], file_json)