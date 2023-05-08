# GoodReads Web Scraper
I absolutely hate the UI for GoodReads. Like why do they only allow you to rate with full stars. What if I want to rate something 4.5???
And don't even get me started on how the some of these divs were set up for the html. THEY WEREN'T EVEN FULLY CONSISTENT.  
Anwyays, let me stop hating on the app since I still find it convenient. 

## Project Description
This webscraper allows you to scrape your personal "Read" shelf.  
I personally only needed the following attributes from the shelf:
title, author, rating, review, dateStart, and dateFinish.  
If you would like to change shelves, or even change attributes, you could
easily alter those options. 

The library also includes an api, that will return the json structure of all the information I mentioned above.   
I plan on creating a website that will also include the books that I read; which is why I created this project!

## Dependencies
The application requires the following packages:
- selenium 
- webdriver-manager
- flask

You can install these using pip or pip3

Selenium requires a chrome driver.  
This is necessary so we don't constantly flood the goodreads server with our requests.  
Go to your Chrome browser --> press the 3 ellipses button --> Help --> About Google Chrome  
You will then see your current Chrome version.  
Go to this website: https://sites.google.com/chromium.org/driver/downloads?authuser=0  
Find the driver that is the closest to your current Chrome version and download the .exe file into this project directory

## Changes To Make Before Running
In the webScraper.py file, make the following changes:
- fill in the username and password variables with your own credentials
- On line 25, insert the url for your accounts "Read" shelf. It should look something like: https://www.goodreads.com/review/list/your_username?ref=nav_mybooks&shelf=read

## How to Run 
If you would just like to run the webScraper application, uncomment the last print statement and the last line. Then just run "./webScraper.py"  

If you would like to run the full API, just run "./goodreadsAPI.py".  
Your console will display "Running on https://_________".  
Copy that url into your browser and add "/api/reviews" to the end of it.  
Give it a few seconds and it should display the full json. 

### Contributions
If you also hate the goodreads UI and would like to make any changes, please feel free to fork and add your own changes :)
