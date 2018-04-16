import urllib.request
import urllib.parse
import urllib
import json
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

###################buy-itnow##################################

buy_itnow="https://www.buyitnow.co.kr/product/extractor?shop=amazon.com&item_id=B079P5D9BC&itemonly=false"
answer=Request(buy_itnow,headers={'X-Requested-With': 'XMLHttpRequest'})
text_anwer=urlopen(answer).read()
#print(text_anwer)
json_str=json.loads(text_anwer)
print(json_str["price"])

"""

###################boda- zone ##################################
boda_zone="http://www.bodazone.com/?doc=amazon/itemDetail.php"
data = urllib.parse.urlencode({'ASIN': 'B079P5D9BC'})
data = data.encode('utf-8')

answer=Request(boda_zone,headers={'X-Requested-With': 'XMLHttpRequest'})

text_anwer=urlopen(answer, data).read().decode('utf-8')
soup=BeautifulSoup(text_anwer,'html.parser')
print(soup)
#json_str=json.loads(soup.select('#detail_estimate > form > input[type="hidden"]')[3])
#print(json_str[value])

print(soup.select('#detail_estimate > form > input[type="hidden"]')[3])
item_qty=1
item_price=str(soup.select('#detail_estimate > form > input[type="hidden"]')[3])
item_price=float(item_price[item_price.find("value=\"")+7:item_price.find("\"/>")])
print(item_price)
servicecharge=0
if(item_price > 0 and item_price < 100) :
	servicecharge = 6
		
else :
	servicecharge= (item_price * 7) /100
	


exchange=str(soup.select('#detail_estimate > form > input[type="hidden"]')[18])
print(exchange)
exchange=float(exchange[exchange.find("value=\"")+7:exchange.find("\"/>")])
print(exchange)
weight=0.8

aircost=0
if(weight == 0)  :
	aircost = 0
elif(weight == 0.5) :
	aircost = 15
elif(weight > 0.5)  :
	aircost= ((weight/0.5)*3)+10


kitem_price=item_price*exchange

Ksalestax=0

Kshippingcost=0

Kservicecharge=servicecharge * exchange

Kaircost=aircost * exchange

tot=kitem_price+Ksalestax+Kshippingcost+Kservicecharge

forctm=kitem_price+Kaircost

ctm1=(forctm * 8)/100

ctm2=((forctm + ctm1) * 10)/100

ctm3=5000
print(tot)
print(forctm)
print("fuck")
"""

#########################joy bay#####################################

joy_bay="http://www.joybay.co.kr/amazon.item/B079P5D9BC/"
answer=Request(joy_bay)
text_anwer=urlopen(answer).read()
soup=BeautifulSoup(text_anwer,'html.parser')
value=soup.select('#id_item_amount')
print(value)




############################mallbuy###################################
mallbuy="http://mallbuy.co.kr/deal/detail?url=B079P5D9BC&shop_id=amazon&lo=#null"
answer=Request(mallbuy)
text_anwer=urlopen(answer).read()
soup=BeautifulSoup(text_anwer,'html.parser')
value=str(soup.select("#price"))
value=float(value[value.find("value=\"")+7:value.find("\"/>")])
#print(value)
mallbuy_js="http://mallbuy.co.kr/quick/quick2_us"
data = urllib.parse.urlencode({'price': value})
data = data.encode('utf-8')
answer=Request(mallbuy_js,headers={'X-Requested-With': 'XMLHttpRequest'})
text_anwer=urlopen(answer, data).read().decode('utf-8')
soup=BeautifulSoup(text_anwer,'html.parser')
temp=soup.find_all('table')
count=0
ans=temp[5].find_all('tbody')[2].find('td',{'class':"pinkbgName myTxt_darkred"}).get_text()
print(ans)


#################buyb##############################################
first_buyb="http://www.buyb.co.kr/bb/bbSelfGoodsInfo.php"

data=urllib.parse.urlencode({'fullpath':'https://www.amazon.com/Latest-Apple-9-7-inch-Retina-Display/dp/B079P5D9BC/ref=sr_1_1?ie=UTF8'})
data = data.encode('utf-8')

answer=Request(first_buyb,headers={'X-Requested-With': 'XMLHttpRequest'})

text_anwer=urlopen(answer, data).read().decode('utf-8')
soup=BeautifulSoup(text_anwer,'html.parser')
soup=str(soup.find('input',{'name':'initweight'}))
value=float(soup[soup.find("value=\"")+7:soup.find("\"/>")])
print(value)

second_buyb="http://www.buyb.co.kr/bb/bbCalPrice.php"
data={'pmode':'amazon','submode':'option','initweight':str(value),'site_id':'Amazon','asin':'B079P5D9BC','goods_num':'1','goods_type':'1','amazon_category':'TABLET_COMPUTER'}
data=urllib.parse.urlencode(data)
data = data.encode('utf-8')

answer=Request(second_buyb)
text_anwer=urlopen(answer, data).read().decode('utf-8')
soup=BeautifulSoup(text_anwer,'html.parser')
print(soup)