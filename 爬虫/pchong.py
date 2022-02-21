from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(executable_path=r"C:\Users\31502\PycharmProjects\pythonPractice\chromedriver.exe" )

browser = webdriver.Chrome(service=s)
browser.get("https://www.baidu.com")


# browser.quit()
