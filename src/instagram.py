from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, urllib.request
import requests

c = webdriver.ChromeOptions()
c.add_argument("--incognito")
driver = webdriver.Chrome(executable_path="/Users/joshbrown/Downloads/chromedriver 3",options=c)

driver.get("https://www.instagram.com/")

#login
time.sleep(5)
username = driver.find_element_by_css_selector("input[name='username']")
password = driver.find_element_by_css_selector("input[name='password']")
username.clear()
password.clear()
username.send_keys("xxxxxx")
password.send_keys("123456")
login = driver.find_element_by_css_selector("button[type='submit']").click()

#save your login info?
time.sleep(10)
notnow = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
#turn on notif
time.sleep(10)
notnow2 = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

#searchbox
time.sleep(5)
searchbox = driver.find_element_by_css_selector("input[placeholder='Search']")
searchbox.clear()
searchbox.send_keys("host.py")
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)


#scroll
scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
match=False
while(match==False):
    last_count = scrolldown
    time.sleep(3)
    scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
    if last_count==scrolldown:
        match=True

#posts
posts = []
links = driver.find_elements_by_tag_name('a')
for link in links:
    post = link.get_attribute('href')
    if '/p/' in post:
      posts.append(post)

print(posts)


#get videos and images
download_url = ''
for post in posts:	
	driver.get(post)
	shortcode = driver.current_url.split("/")[-2]
	time.sleep(7)
	if driver.find_element_by_css_selector("img[style='object-fit: cover;']") is not None:
		download_url = driver.find_element_by_css_selector("img[style='object-fit: cover;']").get_attribute('src')
		urllib.request.urlretrieve( download_url, '{}.jpg'.format(shortcode))
	else:
		download_url = driver.find_element_by_css_selector("video[type='video/mp4']").get_attribute('src')
		urllib.request.urlretrieve( download_url, '{}.mp4'.format(shortcode))
	time.sleep(5)


# import hashlib
# import json
# import requests
# import sys

# from .constants import (CHROME_WIN_UA, BASE_URL, QUERY_HASHTAG,
#                         QUERY_HASHTAG_VARS, MEDIA_URL)


# class IGScraper:
#     def __init__(self):
#         self.items = []
#         self.session = requests.Session()
#         self.session.headers = {'user-agent': CHROME_WIN_UA}
#         self.session.cookies.set('ig_pr', '1')
#         self.rhx_gis = None

#     def scrape_hashtag(self, hashtag, end_cursor='', maximum=10, first=10,
#                        initial=True, detail=False):
#         if initial:
#             self.items = []

#         try:
#             params = QUERY_HASHTAG_VARS.format(hashtag, 10, end_cursor)
#             response = self.session.get(QUERY_HASHTAG.format(params)).json()
#             data = response['data']['hashtag']
#         except Exception:
#             self.session.close()
#             return []

#         if data:
#             for item in data['edge_hashtag_to_media']['edges']:
#                 node = item['node']
#                 caption = None
#                 if node['edge_media_to_caption']['edges']:
#                     caption = node[
#                         'edge_media_to_caption']['edges'][0]['node']['text']

#                 if any([detail, node['is_video']]):
#                     try:
#                         r = requests.get(MEDIA_URL.format(
#                             node['shortcode'])).json()
#                     except Exception:
#                         continue

#                 if node['is_video']:
#                     display_url = r['graphql']['shortcode_media']['video_url']
#                 else:
#                     display_url = node['display_url']

#                 item = {
#                     'is_video': node['is_video'],
#                     'caption': caption,
#                     'display_url': display_url,
#                     'thumbnail_src': node['thumbnail_src'],
#                     'owner_id': node['owner']['id'],
#                     'id': node['id'],
#                     'shortcode': node['shortcode'],
#                     'taken_at_timestamp': node['taken_at_timestamp']
#                 }

#                 if detail:
#                     owner = r['graphql']['shortcode_media']['owner']
#                     item['profile_picture'] = owner['profile_pic_url']
#                     item['username'] = owner['username']

#                 if item not in self.items and len(self.items) < maximum:
#                     self.items.append(item)

#             end_cursor = data[
#                 'edge_hashtag_to_media']['page_info']['end_cursor']
#             if end_cursor and len(self.items) < maximum:
#                 self.scrape_hashtag(hashtag, detail=detail, initial=False,
#                                     end_cursor=end_cursor, maximum=maximum)
#         self.session.close()
#         return self.items


# scraper = IGScraper()

# # Will return maximum 10 data
# scraper.scrape_hashtag('indonesia')

# # Will return maximum 2 data
# arr = scraper.scrape_hashtag('indonesia', maximum=2)

# print(arr[0])