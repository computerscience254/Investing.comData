import sys
sys.path.append("..")
from Utilis import webscrapper
postData = {
    "curr_id": "941230",
    "smlID": "1509052",
    "header": "BBK+Historical+Data",
    "st_date": "07/22/2009",
    "end_date": '08/22/2019',
    "interval_sec": "Daily",
    "sort_col": "date",
    "sort_ord": "DESC",
    "action": "historical_data"
}
urlHeader = {
    "Host": "www.investing.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
    "Accept": "text/plain, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Length": "172",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.investing.com/equities/barclays-kenya-historical-data",
    "Cookie": "PHPSESSID=d8gd4j3pg1ejqasrbjcsoaiesu; adBlockerNewUserDomains=1566306981; StickySession=id.23934873569.846_www.investing.com; adbBLk=1; billboardCounter_1=0; G_ENABLED_IDPS=google; r_p_s_n=1; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A4%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A6%3A%22941230%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A24%3A%22%2Fequities%2Fbarclays-kenya%22%3B%7Di%3A1%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A6%3A%22941227%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fequities%2Fsafaricom%22%3B%7Di%3A2%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A1%3A%221%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A14%3A%22Euro+US+Dollar%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A19%3A%22%2Fcurrencies%2Feur-usd%22%3B%7Di%3A3%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%228839%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A27%3A%22%2Findices%2Fus-spx-500-futures%22%3B%7D%7D%7D%7D; sideBlockTimeframe=max; geoC=KE; gtmFired=OK; nyxDorf=YGQwZmU3P303Zm1hYC03NzRlZiMyN2Bl"
}

url = "https://www.investing.com/instruments/HistoricalDataAjax"


def get_data():
    data = webscrapper.get_data(url=url, header=urlHeader, data=postData)
    A, B, C, D, E, F, G = webscrapper.parse_data(data)
    webscrapper.generate_csv(A, B, C, D, E, F, G, header=urlHeader)
    webscrapper.push_to_db(A=A, B=B, C=C, D=D, E=E, F=F, G=G, header=urlHeader)
    
if __name__ == "__main__":
    get_data()
