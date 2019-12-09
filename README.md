# Marketbeat Scraper

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0b0d6c99353e4d3d91ac2385c9ae17e3)](https://www.codacy.com/app/forray.zsolt/marketbeat-scraper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Zsolt-Forray/marketbeat-scraper&amp;utm_campaign=Badge_Grade)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

## Description
This tool collects today's analyst actions (upgrades, downgrades, etc.) of major brokerage houses for US companies (including OTC markets).

## Usage
`Data Source: https://www.marketbeat.com/`

![Screenshot](/png/input.png)

### Usage Example
Collect all available today's analyst actions.

```python
#!/usr/bin/python3

import marketbeat_scraper as mbs

sc = mbs.MarketBeatScraper()
res = sc.run_app()

print(res)
```

### Output
List/Dictionary of analyst actions.

![Screenshot](/png/output.png)

## LICENSE
MIT

## Contributions
Contributions to this repository are always welcome.
This repo is maintained by Zsolt Forray (forray.zsolt@gmail.com).
