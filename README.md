# koronavirus.gov.hu-scraper
## A script to scrape data from the official COVID-19 infosite of the Hungarian government
Data is collected in a user-defined Google Sheet. 
The scraper collects the number of people 
1. infected
2. cured
3. dead
4. quarantined
5. tested
A timestamp is added to the first column each time the script runs. 

# Setup
Prerequisites are listed in requirements.txt
The gspread modul needs a complex setup but it's well-documented here: https://gspread.readthedocs.io/en/latest/
