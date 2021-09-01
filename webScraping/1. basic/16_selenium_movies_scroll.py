from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 스크롤 내리기
browser.execute_script("windows.scrollTo(0, 1080") # 해상도 1920 x 1080
