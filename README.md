# Week 22 homework
 This repository holds my week22  homework assignment.
 
## Week22 Homework Assignment Question 1 and 2
#### Q.1 Create a python function to scrape Yelp data for 50 restaurants close to you. Think about what data you want to scrape aside from the restaurant name and location. You must pick at least three other fields. You can use beautiful soup, selenium, scrapy, and/or splinter.
#### Q.2 Create an API that calls your scrape function and stores the data when you call /scrape endpoint. The data you scrape should be viewable when you go to /all .
 - Home page
    * !['Screenshot1'](./week22_screenshot_1.PNG?raw=true "Home page")
 - A /all endpoint that displays all scraped data
	* !['Screenshot2'](./week22_screenshot_2.PNG?raw=true "all endpoint")
	- Notice that this has not captured phone number, address and price range. When I tried it earlier it did capture it, below is screen shot od .csv file for that.I am not sure why sometimes the data is not captured.
	- !['Screenshot4'](./week22_screenshot_4.PNG?raw=true "all endpoint")
 - A /scrape endpoint scrapes yelp restaurants 
    * !['Screenshot3'](./week22_screenshot_3.PNG?raw=true "scrape endpoint")

## Week21 Homework Assignment Question 3
#### Q.3 What is web scraping? Why is it helpful? Why is it sometimes in a legal grey area or just plain illegal?
   - Web scraping is the process of gathering information/extracting data from the Internet. It usually refer to a process that involves automation. Some websites don’t like it when automatic scrapers gather their data, while others don’t mind. 
   - Web scraping can be useful for 
	- Price Monitoring : Web Scraping can be used by companies to scrap the price of products to compare their prices and optimizie thier prices. 
	- Market Research : Web scraping can be helpful for companies in analyzing consumer trends and understand which direction the company should move in the future. 
	- Sentiment Analysis : To get the idea of how thier product is doing in the market by extracting reviews and analysing the sentiment.
	- Email Marketing : Collect Email ID’s from various sites using web scraping and then send bulk promotional and marketing Emails to all the people owning these Email ID’s.
   - The legality of web scraping depends on the terms and conditions of the the website and what you will do with that data. If conditions say you can not use scrapers and still doing so can result in ban in using that website. Search engines like google and bing scrape the website to bring those search results and that in turn brings traffic to thier website. if web scrapres acces the sites that require authentication and based on that provide secure data which is captured in we scraping then release it to outside world this could be illegal. The illegal action here is not that you scraped the content you have already access to but shaing it with the rest of the world. This could be comparable to buying a movie on DVD/Blueray, ripping it on your PC and uploading a pirated version for everyone to see.