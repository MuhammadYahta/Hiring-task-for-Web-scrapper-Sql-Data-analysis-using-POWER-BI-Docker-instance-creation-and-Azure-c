# assesment

The following libraries has been used in the script portion
Flask==1.0.2
pyodbc==4.0.25
json2html==1.2.1
json2table==1.1.5
jsonschema==2.6.0


The flow of scenario is given in the following image and all the necessary files can be access at https://github.com/MuhammadYahta/assesment/ .
 
I choose https://shopee.com.my/ ecommerce website and used a google browser extension based scraper to scrape data fastly instead of using my own scraper.  I first scraped data into MS excel sheet and then export it to azure Cloud sql databased.

I stored the above information into azure cloud SQL.  Database information are given below.
Server=yahyaexpress.database.windows.net
Database=YahyaShoppingCart
UID=myahya87
PWD=System1433

I implemented the above required search function as https://shopy.azurewebsites.net/. 
The python script for this search function can be found at 
 https://github.com/MuhammadYahta/assesment/blob/master/Assesment/server.py


I have used power BI to well visualize the distributions of prices across different categories which can see here 
https://app.powerbi.com/view?r=eyJrIjoiMDFhNTBjNTgtYzQ0ZS00YWMwLWE3MmItODM3ZWViNzk2NGY1IiwidCI6IjU5YzUzOTAyLThiZjktNDBjMC1hNmFmLWZmNjhiYjcwNWVlNSIsImMiOjEwfQ%3D%3D


