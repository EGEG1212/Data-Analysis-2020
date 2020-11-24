import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()  # 주석처리하면.. 페이지가 안나와서 못눌러;; 그래서 꼭 해줘야함
driver.get('http://200.1.220.254:3000/login')
time.sleep(1)

driver.find_element_by_id('uid').send_keys("djy")  # 똑같은경우1
driver.find_element_by_css_selector('#pwd').send_keys("1234")  # 똑같은경우2
driver.find_element_by_class_name('btn.btn-primary').click()  # 클래스네임으로찾아 클릭
# bbs에 자동로그인됨>_<

# 글들을 처음부터 끝까지 가져와보자(뷰티풀숩을쓰면 쉽게가져올 수 있지만, 셀레니움으로 하려면 제일먼저 페이지알아야함)
# 뷰티풀숩에서는 <span>[]댓글수 없으면 널로 넣어서 상관없었는데, 여기서는 문제생김; (아랫줄이 문제)
# reply_count = span.string[1:-1] if span else '0' #없는것도있고 있는것도 있으니, []없으면 스트링'0'으로 아님 int해야함
# 페이지갯수찾기: ul-li 6개 (앞뒤 빼면 4페이지)
ul = driver.find_element_by_css_selector('.pagination')
lis = ul.find_elements_by_tag_name('li')
# print(len(lis))   #python 돌려보니 6나옴
total_pages = len(lis) - 2  # 토탈페이지를 알고있으니

bids = []
titles = []
names = []
times = []
view_counts = []
reply_counts = []

for page in range(total_pages):  # 토탈페이지 아니까 여기를 추가
    trs = driver.find_elements_by_tag_name('tr')  # 01.bbs4와 다르게 변경
    for tr in trs[1:]:
        tds = tr.find_elements_by_tag_name('td')  # 01.bbs4와 다르게 변경
        title = ''
        try:
            span = tds[1].find_element_by_tag_name(
                'span')  # 여기는 element /문제가생겨서try에넣음
            reply_count = span.text[1:-1]  # 여기수정
            # 타이틀 string=대조영[1] 에서 앞에만 가져와야해서 find('[')찾고 아래[:index]슬라이싱을 해줌
            index = tds[1].text.find('[')
            title = tds[1].text[:index]
            #print(reply_count, title)
        except:
            reply_count = 0
            title = tds[1].text
        bids.append(tds[0].text)
        titles.append(title)
        names.append(tds[2].text)
        times.append(tds[3].text)
        view_counts.append(tds[4].text)
        reply_counts.append(reply_count)

# 끝나고 나면 넥스트페이지 누르는 기능
    ul = driver.find_element_by_css_selector('.pagination')
    lis = ul.find_elements_by_tag_name('li')
    lis[page+2].click()  # li의 <<,1,2,3,4,>> 2째의 2p누르려고 +2 두칸씩 뒤로가야함
    time.sleep(2)

print(len(titles))  # 32개 나옴
