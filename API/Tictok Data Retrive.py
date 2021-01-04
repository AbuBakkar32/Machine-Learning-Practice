from TikTokApi import TikTokApi
import pprint
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

api = TikTokApi.get_instance(use_selenium=True)

# get trending video infos
pprint.pprint(api.trending(count=4))


# retrieve data by user name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
pprint.pprint(api.byUsername("therock"))


# retrieve data by hashtag
pprint.pprint(api.byHashtag('love'))