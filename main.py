from lxml import html
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

# Parse koronavirus.gov.hu for data


def getdata():
    page = requests.get('https://koronavirus.gov.hu/')
    tree = html.fromstring(page.content)
    timestamp = [datetime.datetime.fromtimestamp(datetime.datetime.now().timestamp()).isoformat()]
    fertozott = tree.xpath('//*[@id="block-system-main"]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/span/div/span[1]/text()')
    gyogyult = tree.xpath('//*[@id="block-system-main"]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/span/div/span[1]/text()')
    elhunyt = tree.xpath('//*[@id="block-system-main"]/div/div[1]/div[2]/div[1]/div[2]/div[3]/div/span/div/span[1]/text()')
    karantenban = tree.xpath('//*[@id="block-system-main"]/div/div[1]/div[2]/div[1]/div[2]/div[4]/div/span/div/span[1]/text()')
    mintavetel = tree.xpath('//*[@id="block-system-main"]/div/div[1]/div[2]/div[1]/div[2]/div[5]/div/span/div/span[1]/text()')

# Add data to google sheet

    row = timestamp + fertozott + gyogyult + elhunyt + karantenban + mintavetel
    sheet.insert_row(row, 2)


if __name__ == "__main__":
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('COVID-19_HU').sheet1
    getdata()
