import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import csv

def data_fetch(query):
    try:
        # Page access
        searchString = query
        flipkart_url = "https://www.flipkart.com/search?q=" + searchString
        uClient = uReq(flipkart_url)
        flipkartPage = uClient.read()
        uClient.close()
        flipkart_html = bs(flipkartPage, "html.parser")
        bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})
        del bigboxes[0:3]
        reviews = []
        product_name=flipkart_html.findAll("div", {"class": "_4rR01T"})

        #writing into csv file 
        with open(f"{searchString}.csv",'w',encoding="utf-8",newline='') as csv_file:
            writer_=csv.writer(csv_file)
            headers = ["Product", "Customer Name", "Rating","Heading", "Comment" ]
            writer_.writerow(headers)

            #Product Access
            for i in range(len(bigboxes)):
                box = bigboxes[i]
                productLink = "https://www.flipkart.com" + box.div.div.div.a['href']
                prodRes = requests.get(productLink)
                prodRes.encoding='utf-8'
                prod_html = bs(prodRes.text, "html.parser")
                commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})
                
                for commentbox in commentboxes:
                    try:

                        #Comment Access
                        name = commentbox.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text                    
                        rating = commentbox.div.div.div.div.text
                        commentHead = commentbox.div.div.div.p.text
                        comtag = commentbox.div.div.find_all('div', {'class': ''})
                        custComment = comtag[0].div.text
                        csv_data=[product_name[i+1].string,name,rating,commentHead,custComment,productLink]
                        writer_.writerow(csv_data)
                        print("Done")
                    except Exception as e:
                        print("c-",e)
        return searchString         
    except Exception as e:
        print("P-",e)
        return searchString 

