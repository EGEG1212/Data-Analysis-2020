#오피넷 유가정보 셀레니움으로 크롤링하기(python방식)
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window() #주석처리하면.. 페이지가 안나와서 못눌러;; 그래서 꼭 해줘야함
driver.get('http://www.opinet.co.kr/searRgSelect.do')
time.sleep(1) 

#싼주유소찾기 페이지주소를 넣었는데도 안간다;; 그래서 퀵메뉴에서 클릭해보는걸로
#quick 원하는 포인트 찾아서 클릭만해주면 됨 (변수에넣을필요없다)
driver.find_element_by_css_selector('.ic_m1').click()
time.sleep(2)       #안넣으면 너무 빨라서 또 에러나는 경우가있으니 2초정도 넣어준다;

region = driver.find_element_by_xpath('//*[@id="SIGUNGU_NM0"]')
#region = driver.find_element_by_id("SIGUNGU_NM") #이것과 같다 
gu_list = region.find_elements_by_tag_name('option')
#옵션의 구리스트를 구네임즈로 만듦 gu_names = []

gu_names = [gu.get_attribute('value') for gu in gu_list]  #파이썬다운코드(한줄로줄임)
''' gu_names = []
for gu in gu_list:
    name = gu.get_attribute('value')
    gu_names.append(name) '''
del gu_names[0] # 첫줄에 내용없는것 삭제 
print(gu_names)

#엑셀버튼찾아 클릭하는것까지
''' region = driver.find_element_by_id('SIGUNGU_NM0')
region.send_keys(gu_names[0])
time.sleep(1)

driver.find_element_by_xpath('//*[@id="glopopd_excel"]/span').click()  '''#엑셀버튼찾아 클릭하는것까지
#엑셀다운로드 됨 확인완/ 주석처리하고 아래 루핑만들기

# 25개 자치구에 대해서 엑셀다운로드(루핑) 위복붙
for gu in gu_names:
    region = driver.find_element_by_id('SIGUNGU_NM0')
    region.send_keys(gu)
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="glopopd_excel"]/span').click()
    time.sleep(2)
    #엑셀 0~24까지 25개 저장 확인완

    ##ipynb파일로 옮겨봄 

    