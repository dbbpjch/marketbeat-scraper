#!/usr/bin/python3


"""
-------------------------------------------------------------------------
                            BROKERAGE ACTIONS
-------------------------------------------------------------------------
This script gathers today's analyst actions (upgrades, downgrades, etc.)
of major brokerage houses for US companies (including OTC markets).

Source: www.marketbeat.com
-------------------------------------------------------------------------
"""


__author__  = 'Zsolt Forray'
__license__ = 'MIT'
__version__ = '0.0.1'
__date__    = '29/11/2019'
__status__  = 'Development'


import requests
from bs4 import BeautifulSoup as bs
import re


class MarketBeatScraper:
    def __init__(self):
        self.url = "https://www.marketbeat.com/ratings"

    def get_soup(self):
        # Get BeautifulSoup object
        CONNECT_TIMEOUT = 10
        READ_TIMEOUT = 10
        self.req = requests.get(url=self.url, timeout=(CONNECT_TIMEOUT, READ_TIMEOUT))
        self.soup = bs(self.req.content, "lxml")

    def get_raw_table(self):
        # Get raw data table
        self.table_soup = self.soup.find_all("table")

    @staticmethod
    def get_table(table_soup):
        for table in table_soup:
            return table

    @staticmethod
    def actions():
        return ("Downgraded", "Upgraded", "Target Raised", "Target Lowered", \
                "Target Set", "Reiterated", "Initiated")

    @staticmethod
    def get_company(ticker, cols, index):
        if not MarketBeatScraper.check_empty_col(cols[index]):
            return cols[index].replace(ticker, "")

    @staticmethod
    def get_action(cols, index):
        if not MarketBeatScraper.check_empty_col(cols[index]):
            return cols[index].replace("by", "")

    @staticmethod
    def get_brokerage(cols, index):
        if not MarketBeatScraper.check_empty_col(cols[index]):
            return cols[index]

    @staticmethod
    def get_prices(cols, index):
        if not MarketBeatScraper.check_empty_col(cols[index]):
            price = cols[index].replace(" \u279D ", "/") # change (->)
            price = re.sub("^[$]\d+\/|^[$]\d+\.\d+\/", "", price)
            pattern = "\d+\.\d+|\d+"
            return float(re.findall(pattern, price)[0])

    @staticmethod
    def get_rating(cols, index):
        if not MarketBeatScraper.check_empty_col(cols[index]):
            rating = cols[index].replace(" \u279D ", "/") # change (->)
            return re.sub("\w+\/|\w+\s\w+\/", "", rating)

    @staticmethod
    def check_empty_col(cell):
        if cell == "":
            return True

    def get_rows(self):
        table = MarketBeatScraper.get_table(self.table_soup)
        actions = MarketBeatScraper.actions()

        self.result_list = []
        for row in table.find_all("tr")[1:]: # header excluded
            if any(i in row.text for i in actions) \
               and "C$" not in row.text and "$" in row.text:
                self.ticker = row.find_all("div", class_="ticker-area")[0].text
                cols = [i.text for i in row]
                self.company = MarketBeatScraper.get_company(self.ticker, cols, 0)
                self.action = MarketBeatScraper.get_action(cols, 1)
                self.brokerage = MarketBeatScraper.get_brokerage(cols, 2)
                self.current_price = MarketBeatScraper.get_prices(cols, 3)
                self.target_price = MarketBeatScraper.get_prices(cols, 4)
                self.rating = MarketBeatScraper.get_rating(cols, 5)

                result_dict = self.collect_result()
                self.result_list.append(result_dict)

    def collect_result(self):
        return dict(ticker=self.ticker, company=self.company, action=self.action,\
                    brokerage=self.brokerage, current_price=self.current_price,\
                    target_price=self.target_price, rating=self.rating)

    def run_app(self):
        self.get_soup()
        self.get_raw_table()
        self.get_rows()
        return self.result_list


if __name__ == "__main__":
    mbs = MarketBeatScraper()
    mbs.run_app()
