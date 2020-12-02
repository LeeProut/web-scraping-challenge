#!/usr/bin/env python
# coding: utf-8


# import dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd
from pprint import pprint
import time


# ### Step 1 - Scraping

def scrape():

    #set path and browser variables for chromedriver
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped
    url_text = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"


    #open chromedriver browser
    browser.visit(url_text)

    time.sleep(1)


    #create a Beautiful Soup object 
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


# ### NASA Mars News


    #find the div class with the headline and article text 
    results = soup.find("div", class_="list_text")


    #separate out the latest headline
    news_title = results.find("div", class_="content_title").text
    news_title


    #separate out the latest article text 
    news_p = results.find("div", class_="article_teaser_body").text
    news_p


# ### JPL Mars Space Images - Featured Image


    #url for finding featured image to scrape
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"


    #open chromedriver browser
    browser.visit(image_url)

    time.sleep(1)


    #navigate to large size image using splinter
    browser.links.find_by_partial_text("FULL IMAGE").click()


    #click on "more info" to get to large size image
    browser.links.find_by_partial_text("more info").click()

    #create a Beautiful Soup object 
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    #retrieve the image url for the full-size image
    img_results = soup.find("figure", class_="lede") 
    #img_jpg = img_results.find("a")
    img_jpg = img_results.select_one("a")
    img_link = img_jpg["href"]
    #check results for img_link
    #print(img_link)

    #create complete link 
    featured_image_url = f"https:www.jpl.nasa.gov{img_link}"
    featured_image_url


# ### Mars Facts

    #url for mars facts table data to scrape
    table_url = "https://space-facts.com/mars/"


    #open chromedriver browser
    browser.visit(table_url)

    time.sleep(1)


    #read_html for bringing in table with Mars Facts
    mars_facts = pd.read_html(table_url)[0]
    mars_facts

    #change column names and set index
    mars_facts.columns = ["Description", "Mars"]
    mars_facts.set_index("Description", inplace=True)


    #export DataFrame to html
    html_mars_table = mars_facts.to_html()
    html_mars_table
    #pprint(html_mars_table)


# ### Mars Hemispheres


    #url for hemisphere images to scrape
    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"


    #return to base url
    browser.visit(hemi_url)

    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemisphere_urls=[]

    hemis = browser.find_by_tag("h3")


    for items in range(len(hemis)):
        hemispheres = {}
        
        browser.find_by_css("h3")[items].click()
        
        hemispheres['title'] = browser.find_by_css("h2.title").text
        image = browser.links.find_by_text('Sample').first
        hemispheres['image_url'] = image["href"]
        
        hemisphere_urls.append(hemispheres)
        browser.back()           

    #print(hemisphere_urls)

    mars_news = {
        "news_title" : news_title, 
        "news_p" : news_p, 
        "featured_image_url" : featured_image_url,
        "html_mars_table" : html_mars_table,
        "hemisphere_urls": hemisphere_urls    
    }

    #Close the browser after scraping
    browser.quit()

    #return results
    return mars_news
    