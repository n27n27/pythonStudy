from selenium import webdriver
import time
browser = webdriver.Chrome()
# 창 최대화
browser.maximize_window()

url = "https://beta-flight.naver.com/"
browser.get(url)


# 가는 날 선택
browser.find_element_by_xpath("//*[@id=\"__next\"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

# 이번 달 27일, 28일 선택
browser.find_element_by_link_text("29").click()


# browser.find_elements_by_link_text("28")[0].click()

