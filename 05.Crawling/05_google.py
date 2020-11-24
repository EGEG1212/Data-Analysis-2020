import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
# driver.maximize_window()
driver.get('http://www.google.com/')
time.sleep(1)  # 1초동안쉬어라

search_box = driver.find_element_by_name('q')
# search_box = driver.find_element_by_css_selector('#input')
search_box.send_keys('ChromeDriver')  # 크롬드라이버키워드입력
search_box.submit()
time.sleep(2)  # 이번엔 뷰티풀숩에게 소스를 넘기기

''' html = driver.page_source
soup = BeautifulSoup(html, 'html.parser') #이제부터 내가원하는대로 되는거야 크하하하
divs = soup.select('.g') #F12에서 확인한 rcnt-bcenter-med-g*10개있음
#print(len(divs))  #아나콘다프롬프트에 돌리니 10이라는 숫자확인
title_list=[]; content_list=[]
for div in divs:    #제목과 글내용 10개를 가져와보자
    title = div.select_one('.LC20lb DKV0Md').get_text()
    content = div.select_one('.aCOpRe').get_text()
    title_list.append(title)
    content_list.append(content)

df = pd.DataFrame({
    'title': title_list, 'content': content_list
})
df.to_csv('google.csv', sep='|') '''

# 셀레니움으로 하려면 아래처럼
# 위에 3줄이 아래한줄로 간소화됨
divs = driver.find_elements_by_css_selector('.g')  # elements는 리스트
title_list = []
content_list = []
for div in divs:  # 제목과 글내용 10개를 가져와보자
    title = div.find_element_by_css_selector(
        '.LC20lb DKV0Md').text  # 여기는 element
    content = div.find_element_by_css_selector('.aCOpRe').text
    # title_list.append(title)
    # cotent_list.append(content)
    print(title)
    print(content)
