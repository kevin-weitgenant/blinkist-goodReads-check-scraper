from playwright.sync_api import sync_playwright
import os
from lxml import html
import json
import pandas as pd

user_dir = '/tmp/playwright'

if not os.path.exists(user_dir):
  os.makedirs(user_dir)

with sync_playwright() as p:
  browser = p.chromium.launch_persistent_context(user_dir, headless=False, slow_mo=1)
  page = browser.new_page()
  page.goto('https://www.blinkist.com/sitemap', wait_until='domcontentloaded')


  tree = html.fromstring(page.content())

base = '//section[@class="sitemap__section sitemap__section--books"]'
    
livros = tree.xpath(f'{base}//a[@class = "sitemap-links__link"]/text()')
links = tree.xpath(f'{base}//a[@class = "sitemap-links__link"]/@href')
links = ["www.blinkist.com"+x for x in links]

dictionary = { 'books' : livros, 'urls': links }

print(dictionary)

dataframe = pd.DataFrame.from_dict(dictionary )
dataframe.to_csv('blinkist_book_db.csv') 





