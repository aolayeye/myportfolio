# Import Splinter and BeautifulSoup
from pandas.core.indexes.base import Index
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt




def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)


    # Run all scraping functions and store results in dictionary
    data = {
      "news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "hemispheres": hemispheres(browser),
      "facts": mars_facts(),
      "last_modified": dt.datetime.now()
      }
      
    # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):

   # Visit the mars nasa news site
   url = 'https://redplanetscience.com/'
   browser.visit(url)

   # Optional delay for loading the page
   browser.is_element_present_by_css('div.list_text', wait_time=1)

   # Convert the browser html to a soup object and then quit the browser
   html = browser.html
   news_soup = soup(html, 'html.parser')

   try:
       slide_elem = news_soup.select_one('div.list_text')
       # Use the parent element to find the first <a> tag and save it as `news_title`
       news_title = slide_elem.find('div', class_='content_title').get_text()
       # Use the parent element to find the paragraph text
       news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
   except AttributeError:
       return None, None

   return news_title, news_p

def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    #full_image_elem = browser.find_by_tag('button')[1]
    #full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # try:
    #     # Find the relative image url
    #     img_url_rel = img_soup.find('img', class_='headerimage fade-in').get('src')
    # except AttributeError:
    #     return None

    
    try:
        # Find the relative image url
        f_img_soup = img_soup.find('div', class_='multi_teaser')
        images = f_img_soup.findAll('img')[1]
        img_url = images['src']
    except AttributeError:
        return None
    


    # Use the base URL to create an absolute URL
    #img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    
    return img_url

def mars_facts():
    try:
        # use 'read_html" to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
        
    except BaseException:
        return None
    
    # Assign columns and set index of dataframe
    #delete the index name
    df.index.names = [None]

    
    df.columns=['Description', 'Mars', 'Earth']

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(index=False)
    

def hemispheres(browser):
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    html = browser.html
    img_soup = soup(html, 'html.parser')

    img_title_url = img_soup.find_all('div', class_='item')
    hemisphere_image_urls = []
    for img in img_title_url:
        img_title_list = img.find('h3').text
        end_link = img.find("a").get('href')
        image_link = "https://marshemispheres.com/" + end_link
        browser.visit(image_link)
        html = browser.html
        img_soup= soup(html, "html.parser")
        img_downloads = img_soup.find("div", class_="downloads")
        image_url = img_downloads.find('a').get('href')
        img_url_list=f"https://marshemispheres.com/"+image_url
        hemisphere_image_urls.append({"img_url":img_url_list,"title":img_title_list})
    
    browser.quit()
    return hemisphere_image_urls

    
