from selenium import webdriver
import time

browser = webdriver.Chrome("./chromedriver.exe") # 같은 경로면 생략가능

# 1. 네이버 이동
browser.get("http://www.naver.com")

# 2. 로그인 버튼 클릭
el = browser.find_element_by_class_name("link_login")
el.click()
  
# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("skfdkfkalsn")
browser.find_element_by_id("pw").send_keys("Whfh2731@@")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()
time.sleep(3)

# 5. id 를 새로 입력
# browser.find_element_by_id("id").send_keys("skfdkfkn")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("skfdkfkn")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
browser.close()
browser.quit()