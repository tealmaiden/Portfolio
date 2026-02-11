# Precise CSV Export from TradeSmith Portfolios

TradeSmith's built-in CSV export of user's own portfolio data cuts off precision, often leaving only a single significant digit for large or small numbers. This leads to inaccuracies when using the downloaded data for independent calculations. 

The full-precision of the data is present but not easily accessible. It can be exported by accessing parts of the website not directly exposed to users while logged in, or tediously by copying and pasting from individual edit pages.


## Original Version (2025)
In the past, all data in a portfolio was hidden in the static html, which could be exported in full by saving the web page html locally. tradesmith_scraper.py could be used to parse values numbers from fields like "sortvalue". After updates, these details are no longer in the same html files.

## Scraping with Playwright (not recommended)
Precise numbers are also available in the edit pages of each trade. So in theory, a user can navigate to each edit page and copy and paste the data from there. tradesmith_scraper_play.py helps automate this process. When run, it opens a browser where you can login to the website and select your portfolio and filters. After a time, it automatically navigates to each edit page of the portfolio in the browser and collects the desired info. This is very slow. It also relies on all datasets being present in the DOM before it starts the loop. This is not possible for large datasets.

## Latest version (2026)
Thankfully, the data is present in a response visible on inspection following specific steps. On chrome, in your portfolio:
   * Inspect
   * Open DevTools → Network tab
   * Reload the page
   * Filter by fetch or xhr
   * Find GetPositionsGridData
   * Copy the JSON response in full and paste into a txt file.
     
tradesmith_scraper_response.py can be used to parse this into a csv file.

This is not proprietary data from tradesmith that is being hidden/extracted in this description. It is the raw data entered by a given user such as number of shares and prices, from their own account. After requesting many times that tradesmith simply export the full precision in their own csv export option (2025 and pre), they obfuscated the data further (2026).
