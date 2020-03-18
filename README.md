# koronavirus.gov.hu-scraper
## A script to scrape data from the official COVID-19 infosite of the Hungarian government
Data is collected in a user-defined Google Sheet. 
The scraper collects the number of people 
1. timestamp
2. infected
3. cured
4. dead
5. quarantined
6. tested

# Setup
Prerequisites are listed in requirements.txt
The gspread modul needs a complex setup but it's well-documented here: https://gspread.readthedocs.io/en/latest/
Name the columns in the first row according to your preference. Data columns are defined above. 
