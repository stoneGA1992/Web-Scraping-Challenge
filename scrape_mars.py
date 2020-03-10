#!/usr/bin/env python
# coding: utf-8

# In[33]:


# Declare Dependencies 
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests


# In[34]:


# Set Executable Path & Initialize Chrome Browser
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[35]:


# Nasa site set up
url = "https://mars.nasa.gov/news/"
browser.visit(url)


# # NASA Mars News 

# In[36]:


# HTML Object
html = browser.html

# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')


# Retrieve the latest element that contains news title and news_paragraph
news_title = soup.find('div', class_='list_text').find('a').text
news_paragraph = soup.find('div', class_='article_teaser_body').text

# Display scrapped data 
print(news_title)
print(news_paragraph)


# # JPL Mars Space Images

# In[37]:


# Visit Mars Space Images through splinter module
image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(image_url_featured)


# In[38]:


# HTML Object 
html_image = browser.html

# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html_image, 'html.parser')

# Retrieve background-image url from style tag 
featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

# Website Url 
main_url = 'https://www.jpl.nasa.gov'

# Concatenate website url with scrapped route
featured_image_url = main_url + featured_image_url

# Display full link to featured image
featured_image_url


# # Mars Weather

# In[39]:


# Visit Mars Weather Twitter through splinter module
weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(weather_url)


# In[40]:



#create an HTML object to parse with Beautiful Soup
twitter_weather= browser.html

#parse object with Beautiful Soup
soup = BeautifulSoup(twitter_weather, 'html.parser')


# In[41]:


#Pull weather tweet
weather_tweet =soup.find('div', class_ = 'css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0').text

weather_tweet


# # Mars Facts

# In[42]:


#Read the website using pandas
facts_url = 'https://space-facts.com/mars/'

tables= pd.read_html(facts_url)

tables


# In[43]:


#Turn the dataframe into a list
type(tables)


# In[44]:


#Create the DataFrame
mars_facts = tables[0]
mars_facts.columns =['metric', 'data']

mars_facts.head()


# In[45]:


#Generate HTML table from DataFrame

html_table = mars_facts.to_html()

html_table


# # Mars Hemispheres

# In[46]:


#Mars Hemispheres
#Grab high resolution images for each Mars Hemisphere
hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemispheres_url)

#create HTML object to be parsed
hemispheres_html = browser.html

#parse HTML with Beautiful Soup
soup = BeautifulSoup(hemispheres_html, 'html.parser')


# In[47]:


#Grab the items that has the hemispheres information
items = soup.find_all('div', class_='item')

#Hemisphere URL list
hemisphere_image_urls = []

#Plase main url in variable to combine later
hemisphere_url = 'https://astrogeology.usgs.gov'

#create a loop  to grab each link and create a dictoinary 
for i in items:
    #grab the title
    title = i.find('h3').text
    
    #website link
    image_url = i.find('a', class_='itemLink product-item')['href']
    
    #Visit the link
    browser.visit(hemisphere_url + img_url)
    
    #make html object
    image_html = browser.html
    
    #use beautiful soup
    soup = BeautifulSoup(img_html, 'html.parser')
    
    #grab the full image data
    image_url = hemisphere_url + soup.find('img', class_='wide-image')['src']
    
    hemisphere_image_urls.append({'title':title, 'img_url':image_url})
    
    
#pring urls
hemisphere_pic_urls


# In[ ]:




