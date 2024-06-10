from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_gold_info():
    # 브라우저 옵션 설정
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 브라우저를 화면에 띄우지 않음
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # 크롬드라이버 설정
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # 페이지 로드
    url = "https://www.koreagoldx.co.kr/main/html.php?agencyCode=&htmid=goods/gold_list.html"
    driver.get(url)

    # 페이지가 완전히 로드될 때까지 잠시 대기
    time.sleep(5)  # 필요에 따라 조정

    # 클래스가 'tabulator-row tabulator-selectable'인 모든 객체 수집
    elements = driver.find_elements(By.CLASS_NAME, 'tabulator-row.tabulator-selectable')

    # 결과 출력
    for element in elements:
        # print(element.get_attribute('outerHTML'))
        writeday_element = element.find_element(By.XPATH, './/div[@tabulator-field="writeday"]')
        spure_element = element.find_element(By.XPATH, './/div[@tabulator-field="spure"]')
        ppure_element = element.find_element(By.XPATH, './/div[@tabulator-field="ppure"]')
        p18k_element = element.find_element(By.XPATH, './/div[@tabulator-field="p18k"]')
        p14k_element = element.find_element(By.XPATH, './/div[@tabulator-field="p14k"]')
        
        writeday = writeday_element.get_attribute('innerHTML')
        spure = spure_element.get_attribute('innerHTML')
        ppure = ppure_element.get_attribute('innerHTML')
        p18k = p18k_element.get_attribute('innerHTML')
        p14k = p14k_element.get_attribute('innerHTML')

        print(writeday, spure, ppure, p18k, p14k)

    # 브라우저 닫기
    driver.quit()


if __name__ == "__main__":
    get_gold_info()