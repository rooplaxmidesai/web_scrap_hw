#!/usr/bin/env python

#import necessary libraries
#pip install flask
from flask import Flask, json,render_template,redirect,url_for
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

app  = Flask(__name__)


#decorator
@app.route("/")
def echo_hello():
    return_text = """<p>Web Scraping 50 restaurant near me from yelp!</p>
                     <p>/scrape endpoint will call the function to scrape yelp and store data in CSV file</p>
                     <p>/all endpoint will display scrapped data</p>
                      """
    return return_text

@app.route("/scrape")
def web_scrape():
    #Call function
    scrape_restaurant_details()
    return redirect(url_for("show_data"))


# Scrape 50 yelp restaurants near you
def scrape_restaurant_details():
    i=0
    restaurant_list = []
    #each page has 10 restaurants. To get 50 restaurants loop thourgh 5 times
    while i<=40:
        yurl = f'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Ballwin%2C+MO+63021&start={i}'
        response = requests.get(yurl)
        print(yurl)
        page_soup = bs(response.text, 'html.parser')
        
        #Get all the restaurant names in each page. One page has 10 restaurants
        business = page_soup.find_all("div",class_="container__09f24__sxa9- hoverable__09f24__3HkY2 margin-t3__09f24__hHZsm margin-b3__09f24__3h89A padding-t3__09f24__1VTAn padding-r3__09f24__11Xv2 padding-b3__09f24__2I83c padding-l3__09f24__1JEx9 border--top__09f24__37VAs border--right__09f24__Z9jGU border--bottom__09f24__3lElq border--left__09f24__akfOa border-color--default__09f24__3Epto")
        try:
            for b in business:
                #Restaurant Name
                rest_name = b.find("div",class_="businessName__09f24__3Ml2X display--inline-block__09f24__3SvIn border-color--default__09f24__3Epto").find("a").text
                
                #Price range
                price = b.find("span",class_="priceRange__09f24__2GspP css-xtpg8e")
                if price!=None:
                    price = price.text
                else:
                    price = "Not Specified"
                
                #Facilities like - takeout, dinein, delivery etc
                #facility = b.find_all("span",class_="raw__09f24__3Azrj")
                #f_list=[]
                #if facility!=None:
                #    for f in facility:
                #        f_list.append(f.text)
                #else:
                #    f_list.append("Not Specified")
                
                #Facilities like - takeout, dinein, delivery etc
                facility =  b.find_all("ul",class_="undefined list__09f24__36n6_") 
                #print(len(facility))
                f_list=[]
                if facility!=None:
                    for f in facility:
                        f_list.append(f.find("span",class_="raw__09f24__3Azrj").text)
                else:
                    f_list.append("Not Specified")
                
                #First review
                first_review = b.find("p",class_="css-e81eai").text
                
                #rating
                ratings = b.find("span", class_="display--inline__09f24__nqZ_W border-color--default__09f24__3Epto").div.get('aria-label')

                #Review Count
                review_count = b.find("span",class_="reviewCount__09f24__3GsGY css-e81eai")
                if review_count!=None:
                    review_count = review_count.text
                else:
                    review_count = "Not specified"
        
            
                #Get list of food category
                food_category = b.find_all("p",class_="css-1j7sdmt")
                #print(len(food_category))
                fc_list=[]
                if food_category!=None:
                    for fc in food_category:
                        #Find text for each food category
                        fcat = fc.find_all("p",class_="text__09f24__2NHRu css-1hx6l2b")
                        if(fcat!=None):
                            for c in fcat:
                                if(c!=None):
                                    fc_list.append(c.text)
                                else:
                                    fc_list.append("Not Specified")
                        else:
                            fc_list.append("Not Specified")
                else:
                    fc_list.append("Not Specified")
                
                
                #Phone number and address:
                address = b.find_all("p" ,class_="css-8jxw1i")
                cnt = 0
                phone_number="Not Specified"
                addr="Not Specified"
                if address!=None:
                    for a in address:
                        if cnt==0:
                            phone_number = a.text
                        if cnt==1:
                            addr = a.find("span",class_="raw__09f24__3Azrj").text
                        cnt = cnt + 1
                    #print("Phone and address",phone_number,addr)
            
                #Dictionary of restaurant name, rating etc.    
                rest_dict = {"Name":rest_name,
                            "Phone Number":phone_number,
                            "Address":addr,
                            "Price range":price,
                            "Facility":f_list,
                            "1st Review": first_review,
                            "Ratings":ratings,
                            "Review Count":review_count,
                            "Food Category":fc_list
                            }

                restaurant_list.append(rest_dict)
        except AttributeError as e:
                print(e)
            
        #Go to next 10 restaurants
        i= i + 10
        
    rest_df = pd.DataFrame(restaurant_list)
    rest_df.to_csv("./static/yelp_ballwin_rest.csv")
    #return render_template('index.html',  tables=[rest_df.to_html(classes='data', header="true")])
    #render template is always looking in tempate folder
    #return "<p>Web Scraping 50 restaurants near me from yelp and storing them in CSV file!</p>"
    #return redirect(url_for("show_data"))


@app.route("/all")
def show_data():
    rest_df = pd.read_csv("./static/yelp_ballwin_rest.csv")
    #render template is always looking in tempate folder
    return render_template('index.html',  tables=[rest_df.to_html(classes='data', header="true")])

if __name__ == "__main__":
    app.run(debug=True)


