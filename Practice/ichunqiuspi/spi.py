import requests
import re
import bs4

url = 'http://www.ichunqiu.com/courses/all-all-0-0-0-2-1'

def spider(url):
    header = {
                'Host': 'www.ichunqiu.com',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Referer': 'http://www.ichunqiu.com/courses/all-all-0-0-0-2-2',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
                'Cookie': '__jsluid=971fc528137546b77301760c5f14c792; chkphone=acWxNpxhQpDiAchhNuSnEqyiQuDIO0O0O; Hm_lvt_9104989ce242a8e03049eaceca950328=1491376119,1491458381,1492044760,1492345152; pgv_pvi=761049088; browse=CFlcQFQKAE9cUlxFW0oaT1haUldcQVhCRFNcWF9JSUdYWV1AVENfV1IKUkBZSVBCUhBSRFdLS0dZUl9YXkVERF9DWExURVFPWVVKTgdLXENcU11OHUtYTFNBWkVfRkRFXU5ZQ05BUE9dW1JEXlNSHFNWXUJbRFIGU1JRT0xDWUReTlhBQ0BfVVlaUkBeS1lFS1gBT1tCWUVQWBtPX0hTV1tTWUJDQV1YWFVIRVdLXEVTUFtXVRhTQFpXW0JVAlNEUFlKR15AXlhZV0VEV1FbRFNRXk9cR0tOAFldQl1EWE4aWVlMVFNbRVhURUVaXFhDSVNRT1tDU0RZQVMcVEReQl9WUwZUQFBPS1FYRFlcWUFEUl5VXkhTQFtZXEVMSgBPXFVZRFdKGk9YWlJXXEFYQkRTXFhfR0lFUFldR1REW1dSClJAWUVQRlIQUkRXS0tHWVJfWF5FRERfQ1hMVERaT1haSk4HS1xDUVNfTh1LWExTQVpFX0ZERV1OWUNOQVBPXFBSRl5TUhxTVl9BXkRSBlNSUU9MQ1lEXk5YQUNAX1VZWlJAXUtdR0tYAU9bR1FEUFgbT19IU1dbU1lCQ0FdWFhVSEVXS1xBU1NZV1UYU0BfW1xCVQJTRFBZSkdeQF5YWVdFRFhRWUxTVlxPX0JLTgBZXUNZRFBOGllZTFRTW0VYVEVFWlxYQ0lTUU9bRVNGWkFTHFREX0JbVlMGVEBQT0tRWERZXFlBRFJeVV5IU0BdWVxBTEoAT1xUXUJbShpPWFpSV1xBWEJEU1xYX0dJRVBZXUFURFtXUgpSQF9AXEJSEFJEV0tLR1lSX1heRUREX0NYTFREXE9ZVkpOB0tcQ1FUXU4dS1hMU0FaRV9GREVdTllDTkFQT1xWUkddU1IcU1ZeQV5CUgZTUlFPTENZRF5OWEFDQF9VWVpSQFtLWkNLWAFPW0RcQV5YG09fSFNXW1NZQkNBXVhYVUhFV0tcQ1NTWVdVGFNAW1VRTFUCU0RQWUpHXkBeWFlXRURYUVlMU1ZeT19DS04AWV1GXUNeThpZWUxUU1tFWFRFRVpcWENJU1FPW0dTR1xBUxxURF1NXVJTBlRAUE9LUVhEWVxZQURSXlVeSFNAX1lcQ0xKAE9cV1lDV0oaT1haUldcQVhCRFNcWF9HSUVQWV1DVERQV1IKUkBdSF5EUhBSRFdLS0dZUl9YXkVERF9DWExURF5PWFFKTgdLXEZQVF9OHUtYTFNBWkVfRkRFXU5ZQ05BUE9cVFJHXlNSHFNWWE1cQlIGU1JRT0xDWUReTlhBQ0BfVVlaUkBZS1pDS1gBT11BWk4aWVlMVFNbRVhURUVaXFhDSVNRT1tGU0FRQVMcVEBdQVIQUkRXS0tHWVJfWF5FRERfQ1hMVEReT1xUSk4HS1hBXFgbT19IU1dbU1lCQ0FdWFhVSEVXS1xNU1NaV1UYU0BbUV9GVQJTRFBZSkdeQF5YWVdFRFhRWUxTVlBPXEZLTgBZXUVYRFpOGllZTFRTW0VYVEVFWlxYQ0lTUU9bSVNAWkFTHFREW0VeVlMGVEBQT0tRWERZXFlBRFJeVV5IU0BQWVhMTEoAT1xTUUddShpPWFpSV1xBWEJEU1xYX0dJRVBZXUxUQ1tXUgpSQF9CXERSEFJEV0tLR1lSX1heRUREX0NYTFREUE9dUUpOB0tcR1hUX04dS1hMU0FaRV9GREVdTllDTkFQT1xaUkBbU1IcU1ZZQl1IUgZTUlFPTENZRF5OWEFDQF9VWFNSRV5LWEZLWAFPW0FRRVhYG09fSFNXW1NZQkNBXVhYVUhEXktZRVNRWldVGFNAWFdeRFUCU0RQWUpHXkBeWFlXRURYUVhFU1NYT11JS04AWV1EWkNQThpZWUxUU1tFWFRFRVpcWENJUlhPXkFTQFpBUxxURFlHXlpTBlRAUE9LUVhEWVxZQURSXlVfQVNFWVldTExKAE9cU1BAWUoaT1haUldcQVhCRFNcWF9HSURZWVhEVEBRV1IKUkRbR1BOGllZTFRTW0VYVEVFWlxYQ0lSWE9eQ1NBWUFTHFRAWkBaWBtPX0hTV1tTWUJDQV1YWFpIR19LXEVTVlxXVQw; __jsl_clearance=1492576246.97|0|NO29QIoSieX1q6l0wZTDnH6wXuY%3D; Hm_lvt_1a32f7c660491887db0960e9c314b022=1491963619,1492259491,1492476884,1492569698; Hm_lpvt_1a32f7c660491887db0960e9c314b022=1492576259; ci_session=68aef31b175dc907ee4f83ef5a94ee054b2bc3e3',

    }
    r = requests.request('get',url=url,headers=header,timeout=100)
    print(r.status_code)
    soup = bs4.BeautifulSoup(r.content,'lxml')
    names = soup.find_all(name='div',attrs={'class':'coursename'})
    return(names)

def main():
    for i in range(14):
        url = 'http://www.ichunqiu.com/courses/all-all-0-0-0-2-'+str(i)
        names = spider(url)
        for name in names:
            file.write(name.string+'\n')
        

if __name__ == '__main__':
    file = open('names.txt','w')
    main()
    file.close()

