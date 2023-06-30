# ebay-filtering-tool
python app that take url of ebay search, goes through every product one by one and gives better result than native page.

Minimal requirements:
Python environment
Selenium library for python.
Google Chromium/Chrome with Selenium compatibility.

I did not test it on anything else but my trusty Linux Gentoo.

How it works:
Search for something you need.
Once search is done, copy paste whole URL into command line, so it will looks smth like this:
python buysieve.py "$URL_from_ebay_search_result"

Example below from real life use:
python buysieve.py "https://www.ebay.ie/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=amd+rx+(%2216gb%22%2C+%2212gb%22)+-computer+-pc+-motherboard+(%22GPU%22%2C+%22Graphics+Card%22)+-8gb&_sacat=0&LH_TitleDesc=0&_udlo=120&_odkw=amd+rx+16gb+-computer+-pc+-motherboard+(%22GPU%22%2C+%22Graphics+Card%22)+-8gb+12gb&_osacat=0&_sop=1&LH_PrefLoc=2&_ipg=240&_udhi=300"

Now app will load a page, and cut out advertising section together with less relevant results.
Once it does it - it checks for every product, and will provide you with info on product name, price, iten number, URL of product, its seller, seller's reputation and some information on ammount of money earned from sold products.

The main reason why I created this script - I was sick and tired of irrelevant results/advertising and scammy traders on Ebay, when comes to computer parts.

If people will be interested in this, I will improve it with sniping tool URL's and other bells and whistles.(more strict checks of reseller come to mind)

Known issues:
Ebay does not like people collecting data on their sellers. Because of that i had to fool ebay a little. Basically I noticed that my automated scrapping attempts were killed off by Ebay's captcha. So I implemented Selenium. And even then, once every so often captcha shows up in my requests.
Take note of reseller, in whose requests captcha appears(selenium will trigger web browser to open up for 2-3 seconds) and try to open up their page in anonymous page of web browser. If captcha appears - solve it. And this script will work properly once more.
Curl + cookies did not cut it. I am opened to suggestions.


Example output may looks something like(be advised, github does some weird formatting of stuff below, so result may warry):

 python buysieve.py "https://www.ebay.ie/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=amd+rx+(%2216gb%22%2C+%2212gb%22)+-computer+-pc+-motherboard+(%22GPU%22%2C+%22Graphics+Card%22)+-8gb&_sacat=0&LH_TitleDesc=0&_udlo=120&_odkw=amd+rx+16gb+-computer+-pc+-motherboard+(%22GPU%22%2C+%22Graphics+Card%22)+-8gb+12gb&_osacat=0&_sop=1&LH_PrefLoc=2&_ipg=240&_udhi=300" 
user site type is:  www.ebay.ie


PowerColor Red Dragon AMD Radeon RX 6800 OC 16GB GDDR6 Graphics Card 155626030119 www.ebay.ie/itm/155626030119
EUR 298.48
dancingmemoriesqueen (1,315) 100%
seller URL is:  https://www.ebay.ie/fdbk/feedback_profile/dancingmemoriesqueen?filter=feedback_page%3ARECEIVED_AS_SELLER
US $10.00  US $60.00  US $3.00  US $3.49  US $5.50  US $4.00  US $19.00  US $7.00  US $55.00  US $112.50  US $22.00  US $57.00  US $39.00  US $24.00  US $7.00  US $45.00  US $5.00  US $4.00  US $5.00  US $10.00  US $4.00  US $5.00  US $9.00  US $7.00  US $4.00  

AMD Radeon RX 6700 XT 12GB GDDR6 Graphics Card GPU Reference 6700xt -Excellent 2350651255 www.ebay.ie/itm/2350651255
EUR 204.34
oat*eclan (558) 100%
seller URL is:  https://www.ebay.ie/fdbk/feedback_profile/oaturtleclan?filter=feedback_page%3ARECEIVED_AS_SELLER
ACHTUNG: no sales history or sales are hidden, either way - I would pass on this seller.

