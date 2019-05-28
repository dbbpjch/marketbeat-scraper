"""
-------------------------------------------------------------------------
                            BROKERAGE ACTIONS
-------------------------------------------------------------------------

This script gathers analyst actions (upgrades, downgrades, etc.)
of major brokerage houses from www.marketbeat.com.

|
| Input parameter(s):   Date
|                       eg. "2019-02-20"
|

Date:   Date of the requested analyst actions from 2019-01-01
        to the current day, eg. format: "2019-02-20"

-------------------------------------------------------------------------
"""

import requests
from bs4 import BeautifulSoup as bs
import re
from datetime import datetime
import user_defined_exceptions as ude

def check_date(date):
    date_dt = datetime.strptime(date, "%Y-%m-%d").date()
    last_date = datetime.now().date()
    start_date = datetime(2019, 1, 1).date()
    if date_dt > last_date:
        raise ude.DateLaterError()
    elif date_dt < start_date:
        raise ude.DateEarlierError()
    return date

def get_soup(date):
    url = "https://www.marketbeat.com/ratings/USA/{}".format(date)
    FEED_TIMEOUT = 10
    req = requests.get(url, timeout=FEED_TIMEOUT)

    if req.status_code != 200:
        raise ude.URLRequestError()
    soup = bs(req.text, "html.parser")
    return soup

def check_table(soup):
    table_soup = soup.find_all("table")
    if len(table_soup) == 0:
        raise ude.EmptyTableError()
    return table_soup

def get_table(table_soup):
    for table in table_soup:
        return table

def get_data(date, table):
    res_list = []
    for tr in table.find_all("tr"):
        td_list = [i.text.encode("utf-8") for i in tr]

        # If company name (ticker) found and we are not in header
        if len(td_list[2]) > 0 and td_list[0] != b"Brokerage":
            # Ticker Symbol
            symbol_list = re.findall(b"\(\w+\)|\(\w+\.\w+\)", td_list[2])
            symbol = re.findall(b"\w+|\w+\.\w+", symbol_list[0])[0]
            symbol = symbol.decode("utf-8")

            # Company Name
            company = re.sub(b"\s\(\w+\)", b"", td_list[2])
            company = company.replace(b",", b"")
            company = company.decode("utf-8")

            # Brokerage Firm
            brokerage = td_list[0].replace(b",", b"")
            brokerage = brokerage.decode("utf-8")

            # Actions
            action = re.sub(b"^\s", b"", td_list[1])
            action = action.decode("utf-8")

            # Price Targets
            target = re.sub(b"^\s", b"", td_list[4])
            # To replace the invalid '\u279D' (->) character
            decoded_target = target.decode("utf-8", "replace")
            target = decoded_target.replace(" \u279D ", "/")
            after_target = re.sub("\d+\/|\d+\.\d+\/", "", target)
            after_target = after_target.replace("$", "")

            # Ratings
            rating = td_list[5]

            # To replace the invalid '\u279D' (->) character
            decoded_rating = rating.decode("utf-8", "replace")
            rating = decoded_rating.replace(" \u279D ", "/")
            after_rating = re.sub("\w+\/|\w+\s\w+\/", "", rating)

            # Collect Results
            res_dict = dict(Date=date, Action=action, Ticker=symbol, Company=company,
                            Brokerage=brokerage, Rating=after_rating, Target=after_target)
            res_list.append(res_dict)
    return res_list

def run(date):
    res_list = []
    try:
        date = check_date(date)
        soup = get_soup(date)
        table_soup = check_table(soup)
        table = get_table(table_soup)
        res_list = get_data(date, table)
    except ude.DateLaterError:
        print("[Error] Invalid date: date can not be later than today")
    except ude.DateEarlierError:
        print("[Error] Invalid date: date can not be earlier than '2019-01-01'")
    except (requests.exceptions.Timeout, ude.URLRequestError):
        print("[Error] Connection problem: please try again later or try an other date")
    except (ude.EmptyTableError, ValueError):
        print(f"[Error] No data found, please check the date")
    return res_list
