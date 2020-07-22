from plyer import notification
from bs4 import BeautifulSoup
import requests
import time
def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="f:\web Scrapping Project\icon.ico",
        timeout=5
    )
def getData(url):
    r=requests.get(url)
    return r.text

if __name__=='__main__':
    while True:
        myHTMLdata=getData('https://www.mohfw.gov.in/')
        soup=BeautifulSoup(myHTMLdata,'html.parser')
        mydatastr=''
        for table in soup.find_all('table'):
            mydatastr +=table.get_text()
        mydatastr=mydatastr[1:]

        itemList=mydatastr.split('\n\n')
        itemList=itemList[3:38]
        states=['Delhi','West Bengal','Uttar Pradesh']
        for item in itemList:
            
            dataList=item.split('\n')
            if dataList[2] in states:
                print(dataList)
                ntitle='cases of covid-19'
                ntext="STATE:{} \n active cases:{} \n cured:{} \n Deaths:{}  total cases:{}".format(dataList[2],dataList[3],dataList[4],dataList[5],dataList[6])
                notifyMe(ntitle,ntext)
                time.sleep(5)
        time.sleep(10)




























