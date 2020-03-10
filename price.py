import bs4, requests

def getThePrice(ProductURL):
    res = requests.get(ProductURL)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elements = soup.select('#container > div > div.t-0M7P._3GgMx1._2doH3V > div._3e7xtJ > div._1HmYoV.hCUpcT > div._1HmYoV._35HD7C.col-8-12 > div:nth-child(2) > div > div._3iZgFn > div._2i1QSc > div > div._1vC4OE._3qQ9m1')
    return elements[0].text

Price = getThePrice('https://www.flipkart.com/power-your-subconscious-mind/p/itmfawz5jdrcvuba?pid=9780143442974&lid=LSTBOK97801434429741DUWFB&marketplace=FLIPKART&fm=productRecommendation%2Fattach&iid=R%3Aa%3Bp%3A9789351772071%3Bl%3ALSTBOK97893517720710CDYJK%3Bpt%3App%3Buid%3A630dcb4a-89bc-09ad-e8d1-5879f66a063b%3B.9780143442974.LSTBOK97801434429741DUWFB&ssid=109qmfrcbk0000001574838333888&otracker=pp_reco_Frequently%2BBought%2BTogether_1_Frequently%2BBought%2BTogether_9780143442974.LSTBOK97801434429741DUWFB_productRecommendation%2Fattach_1&otracker1=pp_reco_PINNED_productRecommendation%2Fattach_Frequently%2BBought%2BTogether_NA_productCard_cc_1_NA_view-all&cid=9780143442974.LSTBOK97801434429741DUWFB')
print('The Price is ' + Price)
