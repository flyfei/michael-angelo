#! python3
# _*_ coding: utf-8 _*_

# ------------------------------
# 查询节假日
# 2017-07-02 23:31:56
# ------------------------------
# alias py=python3 切换版本
# https://www.zhihu.com/question/21653286

import sys
import requests
import os
import time
import datetime

def getPageSource (url):
    print ('获取网页源码 ' + url)
    response = requests.get(url)

    # 解决乱码1 http://sh3ll.me/2014/06/18/python-requests-encoding/
    # response.encoding =  response.apparent_encoding

    # 解决乱码2 https://segmentfault.com/q/1010000000341014
    page = response.text.encode('latin1').decode('gbk')
    # soup = BeautifulSoup(page, "html.parser")
    print ('获取网页源码 soup ' + page)
    return page


def readAndWrite (filename, data):
    with open('./' + filename,'wb') as jsname:
        jsname.write(bytes(data, 'UTF-8'))

domain = "http://www.easybots.cn/api/holiday.php?d="

# now = datetime.datetime.now()

# 例如： python3 index.py 2017
startYear = sys.argv[1]
print ("start check from "+ startYear)
checkDay = datetime.datetime(int(startYear), 1, 1)


allFilename = checkDay.strftime("%Y")
curYear = checkDay.strftime("%Y")
curMou = checkDay.strftime("%m")
allParms = ""
while (curYear != str(int(startYear) + 1)):
    parms = ""
    filename = checkDay.strftime("%Y%m")
    while (checkDay.strftime("%m") == curMou):

        if len(parms) > 0:
            parms += ","

        parms += checkDay.strftime("%Y%m%d")
        checkDay = checkDay + datetime.timedelta(days=1)

    readAndWrite(filename, getPageSource(domain + parms))
    time.sleep(5)
    curYear = checkDay.strftime("%Y")
    curMou = checkDay.strftime("%m")

    if len(allParms) > 0:
        allParms += ","
    allParms += parms

readAndWrite(allFilename, getPageSource(domain + allParms))
