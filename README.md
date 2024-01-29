# udemy-sale-check
program to check whether udemy is on sale


the .py program is the the python file that has been turned into an executable using pyinstaller
executable can be found in dist/udemySaleCheck


Uses requests and beautifulsoup for fetching udemy webpage and web scraping. 
This program relies on html structure of the file and thus may not work if udemy refactors it's website.
Only works for desktop version of the site


Check for 'sale' / '₹4' in fetched content as the discounted courses are usually for ₹450 / ₹499


if match found, win11toast sends a windows notification


limitations:
depends on website structure
works only for windows
needs active net connection



can schedule the executable using windows Task Scheduler
