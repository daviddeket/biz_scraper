#!/usr/bin/env python3
import requests
import time
from selenium import webdriver

starting_site = 70000
driver = webdriver.Firefox()

def get_ids_we_want(site_numb):
    
    site_url = "https://yuki.la/biz/page/#"
    driver.get(site_url + site_numb)
    time.sleep(3)

    # manage html
    all_posts = driver.find_elements_by_class_name("file")
    all_replys = driver.find_elements_by_class_name("replylink")

    all_post_ids = []
    all_post_ids_many_replys = []

    # get all posts
    for elem in all_posts:
        all_post_ids.append(elem.get_attribute("id")[1:])

    # get all post links with many replys
    for elem in all_replys:
        aa = elem.get_attribute("href")
        aa = aa[len(aa)-8:]
        all_post_ids_many_replys.append(aa)

    #print(all_post_ids)
    #print(all_post_ids_many_replys)

    post_ids_we_want = []
    # get all ids we want
    for ida in all_post_ids:
        if ida not in all_post_ids_many_replys:
            post_ids_we_want.append(ida)

    #print(post_ids_we_want)
    return post_ids_we_want

# make loop
# also add date
# create dataframe
# export to csv

driver.close()
