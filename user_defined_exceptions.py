"""
User Defined Exceptions for MarketBeat Scraper
"""

# MarketBeat
class DateLaterError(Exception):
    pass

class DateEarlierError(Exception):
    pass

class EmptyTableError(Exception):
    pass

class URLRequestError(Exception):
    pass
