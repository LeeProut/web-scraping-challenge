#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd
from pprint import pprint


# ### Step 1 - Scraping

# In[2]:

def scrape():

    #set path and browser variables for chromedriver
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[5]:


    # URL of page to be scraped
    url_text = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"


    # In[6]:


    #open chromedriver browser
    browser.visit(url_text)


    # In[4]:


    #create a Beautiful Soup object 
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # ### NASA Mars News

    # In[55]:


    # results = soup.find("div", class_="content_title").get_text(strip=True)
    # results


    # In[61]:


    #find the div class with the headline and article text 
    results = soup.find("div", class_="list_text")


    # In[75]:


    #separate out the latest headline
    news_title = results.find("div", class_="content_title").text
    news_title


    # In[76]:


    #separate out the latest article text 
    news_p = results.find("div", class_="article_teaser_body").text
    news_p


    # ### JPL Mars Space Images - Featured Image

    # In[7]:


    #url for finding featured image to scrape
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"


    # In[29]:


    #open chromedriver browser
    browser.visit(image_url)


    # In[30]:


    #navigate to large size image using splinter
    browser.links.find_by_partial_text("FULL IMAGE").click()


    # In[31]:


    #click on "more info" to get to large size image
    browser.links.find_by_partial_text("more info").click()


    # In[32]:


    #retrieve the image url for the full-size image
    img_results = soup.find("figure", class_="lede") 
    img_jpg = img_results.find("a")
    img_link = img_jpg["href"]
    #check results for img_link
    #print(img_link)

    #create complete link 
    featured_image_url = f"https:www.jpl.nasa.gov{img_link}"
    featured_image_url


    # ### Mars Facts

    # In[33]:


    #url for mars facts table data to scrape
    table_url = "https://space-facts.com/mars/"


    # In[34]:


    #open chromedriver browser
    browser.visit(table_url)


    # In[71]:


    #read_html for bringing in table with Mars Facts
    mars_facts = pd.read_html(table_url)[0]
    mars_facts


    # In[73]:


    #export DataFrame to html
    html_mars_table = mars_facts.to_html()
    html_mars_table
    pprint(html_mars_table)


    # ### Mars Hemispheres

    # In[45]:


    #url for hemisphere images to scrape
    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"


    # In[56]:


    #open chromedriver browser
    browser.visit(hemi_url)


    # In[57]:


    browser.find_by_tag("h3").click()


    # In[58]:


    #create a Beautiful Soup object 
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #scrape the title
    title = soup.select_one("div.content h2").text
    print(title)

    #scrape the image url
    image_url = soup.select_one("div.downloads a")["href"]
    print(image_url)


    # In[59]:


    #return to base url
    browser.visit(hemi_url)

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


    # In[60]:


    print(hemisphere_urls)

    mars_news = {

    }

    return mars_news
    