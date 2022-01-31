import os
import pandas as pd
import json


def goodreads():  #goodreadsList as argument


    #os.system("scrapy crawl GoodReads -o c.json")

  
    file = open("c.json")

    data = json.load(file) #data is a list of dictionaries, where key=url, values = list of other versions name for the book

    dataframe = pd.DataFrame(data)

    #----------------
    #Clean Data: 
    #-------------------------------

    #end of line things between parantheses like (Kindle Edition) or (Hardcover)



    #join duplicate urls 



    #-----------------------
    #-----------------------------------


    

    


    

def unite():
    pass



goodreads()