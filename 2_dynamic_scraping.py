import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 1. 크롬 드라이버 실행
URL = "https://www.kurly.com/shop/goods/goods_list.php?category=908"
chromedriver = './chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get(url = URL)
driver.implicitly_wait(10)
print("loading is done")

# 2. 데이터 수집(제품명, 가격)
# 컨테이너 : .inner_listgoods .list
# 제품명 : .name
# 가격 : .cost


page_btn = driver.find_elements_by_css_selector(".layout-pagination-number")
data_list = []
cnt = 0

for btn in page_btn:
    btn.click()
    time.sleep(3)

    container = driver.find_elements_by_css_selector(".inner_listgoods li")
    print(len(container))

    for item in container:
        data_dict = {}
        
        cnt += 1
        name = item.find_element_by_css_selector(".name").text
        price = item.find_element_by_css_selector(".cost .price").text

        print("%s : %s" % (name, price))
        data_dict["no"] = cnt
        data_dict["name"] = name
        data_dict["price"] = price
        data_list.append(data_dict)

import csv
csv_columns = ['no', 'name', 'price']
csv_file = 'kurly.csv'
try:
    with open(csv_file, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=csv_columns)
        writer.writeheader()
        for data in data_list:
            writer.writerow(data)
except:
    print("I/O Error")