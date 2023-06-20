from TikTokApi import TikTokApi
# from datetime import datetime

with TikTokApi() as api:
    tag = api.hashtag(name="nosabo")
    num = 0
    for video in tag.videos():
        num += 1
        print("curr")
    print(num)


