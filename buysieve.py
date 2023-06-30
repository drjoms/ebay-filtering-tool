import requests,sys,re
#sleep is only used for debuging
from time import sleep
from  selenium import webdriver
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0'}
def downloadpage(custom_url):
    #print (sys.argv[1:])
    #print (type(sys.argv))
    user_input = str(sys.argv[1:])
    #print ('userinput type is:', type (user_input))
    user_input=user_input[:-2]
    user_input=user_input[2:]
    #print ("user input is:", str(user_input))
    request = requests.get(user_input, headers=headers)
    ebay_page_content = str(request.content)
    return ebay_page_content

custom_url = sys.argv[1:]
custom_url = custom_url[:-2]
custom_url = custom_url[2:]



ebay_page_content = downloadpage(sys.argv[1:])
relevant_content = ebay_page_content
#<span class="BOLD">Results matching fewer words</span>
relevant_content = re.split('(>Results matching fewer words</span>)', ebay_page_content )
#relevant_content = re.split('Results matching fewer words', ebay_page_content )
#print (relevant_content[0])
#print (relevant_content[1])
relevant_content = str(relevant_content[0])

list_of_products = re.findall('<li data-viewport=.*?</div></li>' , relevant_content )

#print (list_of_products[0])

def catch_between( beginstring ,  endstring, product, extracut):
    #print("incoming type" ,type (beginstring))
    #print("what is extracut: ",type(extracut), extracut)
    searchstring = beginstring + ".*?"  + endstring
    cutout = beginstring + "|" + endstring + extracut
    result_needs_cut = re.findall(searchstring , product   )
   #print(type (result_needs_cut))
    #print (re.sub(cutout, "", str(result_needs_cut[0])))
    #print("whats wrong there: ",result_needs_cut[0], type (result_needs_cut[0] ))
    return(re.sub(cutout, "", str(result_needs_cut[0])))
    #print (type(response))
    #print (response)

user_site = sys.argv[1:]
user_site = str(user_site[0])
user_site =  re.split("https://", user_site, maxsplit=1)
user_site =  re.split("/", user_site[1], maxsplit=1)
user_site = user_site[0]
print ("user site type is: ", user_site )
    
for product in list_of_products:
    #print (product)
    if re.findall("Shop on eBay", product):
        pass
    else:
        #print(product)
        #print( product)
        #print ("\n")
        #<div class="s-item__title"><span role="heading" aria-level="3"><!--F#f_0-->XFX Speedster SWFT 319 AMD Radeon™ RX 6900 XT CORE Gaming Graphics Card<!--F/--></span></div>
        #product_name = str(re.findall('<span role=heading aria-level=3><\!--F#f_0-->.*?<\!--F/--></span></div>' , product ))
        #product_name = re.sub('<span role=heading aria-level=3><\!--F#f_0-->|<\!--F/--></span></div>|<span class=LIGHT_HIGHLIGHT>New listing</span><\!--F/--><\!--F#f_0-->',"" , str(product_name))
        #print (str(product_name)[2:-2])
        print("\n")
        product_name = catch_between('<span role=heading aria-level=3><\!--F#f_0-->' ,'<\!--F/--></span></div>', product, '|<span class=LIGHT_HIGHLIGHT>|New listing</span><\!--F/--><\!--F#f_0-->' )
        item_number=catch_between('/itm/', '\?hash=item', product, "" )
        product_url=str(user_site+"/itm/"+item_number)
        print ( product_name, item_number, product_url )


        #product_price = catch_between('<span class=s-item__price>' ,'</span>', product, '|<span class=ITALIC>')
        product_price = catch_between('<div class="s-item__detail s-item__detail--primary"><span class=s-item__price><\!--F#f_0--><\!--F#f_0-->' ,'</span>', product, '|<span class=ITALIC|<\!--F/-->|>')
        print(product_price)
        seller_name = catch_between('<span class=s-item__seller-info><span class=s-item__seller-info-text>' ,'</span></span>', product, '' )
        print(seller_name)
        seller_name = seller_name.split()
        seller_name = seller_name[0]
        #https://www.ebay.ie/usr/verity2003
        seller_url = "https://"+user_site+"/fdbk/feedback_profile/"+seller_name+"?filter=feedback_page%3ARECEIVED_AS_SELLER"
        print ("seller URL is: ", seller_url)
        sleep(3)
        #ebay catches my attempts to see history of seller and CAPTCHAs me, so i had to use selenium, not decision I made lightly. WGET, CURL, did not work for same reason, CAPTCHA.
        seller = webdriver.Chrome()
        seller.get(seller_url)
        seller_feedback = str(seller.page_source)
        #print (seller_feedback)
        #<span data-test-id="fdbk-price-15">US $7.00</span>
        priceline = re.findall("<span data-test-id=\"fdbk-price-.+?\">US .+?</span>", seller_feedback)
        for individual_item_price in priceline:
            individual_price = re.split("<span data-test-id=\"fdbk-price-.+?\">", individual_item_price, maxsplit=0, flags=0)
            individual_price = re.split("</span>", individual_price[1], maxsplit=0, flags=0)
            print (individual_price[0]," ", end='')
            #print("product's URL:", product)
        if not priceline:
            print("ACHTUNG: no sales history or sales are hidden, either way - I would pass on this seller.")
        else:
            pass
            #print("product's URL:", product_name)
        #print (str(priceline))
        #quit()


    
