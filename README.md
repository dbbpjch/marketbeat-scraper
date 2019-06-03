# marketbeat-scraper

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0b0d6c99353e4d3d91ac2385c9ae17e3)](https://www.codacy.com/app/forray.zsolt/marketbeat-scraper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Zsolt-Forray/marketbeat-scraper&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/0b0d6c99353e4d3d91ac2385c9ae17e3)](https://www.codacy.com/app/forray.zsolt/marketbeat-scraper?utm_source=github.com&utm_medium=referral&utm_content=Zsolt-Forray/marketbeat-scraper&utm_campaign=Badge_Coverage)
[![Build Status](https://travis-ci.com/Zsolt-Forray/marketbeat-scraper.svg?branch=master)](https://travis-ci.com/Zsolt-Forray/marketbeat-scraper)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

## Description
This tool collects analyst actions (upgrades, downgrades, etc.) of major brokerage houses happened on a given day from the `MarketBeat` website.

## Usage
1.  Create a new directory somewhere.
2.  Open the Start Menu, type `cmd` in the search field, and then press Enter.
3.  Clone the project by running (make sure that you are in the newly created directory first!):
```txt
git clone https://github.com/Zsolt-Forray/marketbeat-scraper.git
```
4.  Scraper is found in the `marketbeat-scraper` folder.
5.  Import the scraper.

`Data Source: https://www.marketbeat.com/`

![Screenshot](/png/input.png)

### Usage Example
Collect all available analyst actions happened on 2019-02-21.

```python
import marketbeat_scraper as mb
import pprint

pp = pprint.PrettyPrinter(indent=4)

res = mb.run("2019-02-21")

# Get all actions
pp.pprint(res)

# From the 'res' list you can select 'action' you want to know
# Receive Upgrades
upgrades = [i for i in res if i["Action"]=="Upgrades"]
pp.pprint(upgrades)
```

### Output
List/Dictionary of analyst actions.

![Screenshot](/png/output.png)

## LICENSE
MIT

## Contributions
Contributions to MarketBeat Scraper are always welcome.  
If you have questions, suggestions or want to improve this repository, please create an [issue](https://github.com/Zsolt-Forray/marketbeat-scraper/issues) or [pull requests](https://github.com/Zsolt-Forray/marketbeat-scraper/pulls).  
This repo is maintained by Zsolt Forray (forray.zsolt@gmail.com).
