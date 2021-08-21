# 네이버 주식 - 검색상위 종목 30개 현재가 수집

import requests as rq
from bs4 import BeautifulSoup as bs

URL = "https://finance.naver.com/sise/lastsearch2.nhn"
res = rq.get(URL)
res.encoding = 'euc-kr'

# 응답코드 확인
# print(res)

# 응답코드가 4XX 이거나 5XX 인 경우 코드 실행을 멈춤
# res.raise_for_status()

# body 확인
# with open('static_page.html', 'w') as file:
#     file.write(res.text)

# 1. BeautifulSoup를 사용해서 HTML 태그 안에 있는 정보 추출

# 패킷으로 전송된 원본 데이터를 확인 (필수X)
# print(res.content)

# 사람이 읽을 수 있는 형태로 가공(parsing)
# soup = bs(res.content, "html.parser")
# 글자가 깨지는 경우 아래의 코드를 사용
soup = bs(res.content.decode('euc-kr', 'replace'), 'html.parser')

# print(soup)

# 2. 태그 탐색하기
# print(soup.title)

# 가장 첫 번째로 탐색하는 태그를 가져옴
# print(soup.p)

# 텍스트만 추출하여 가져옴
# print(soup.p.text)

# 해당하는 태그를 리스트 형태로 전부 가져옴
# print(soup.find_all('tr'))
# print(soup.find_all('p'))

# 3. find_all로 가져온 리스트에서 데이터 추출
table = soup.find("table", attrs={'class':'type_5'})
# print(table)

# 테이블 첫 번째 열 제거
rows = table.find_all('tr')[1:]
data_list = []

# 종목명, 현재가 데이터 추출
for row in rows:
    if len(row) > 1 :
        # print(row.get_text().replace(" ", "").split())
        data_dict = {}

        row = row.get_text().replace(" ", "").split()
        num = row[0]
        name = row[1]
        price = row[3]
        
        data_dict["no"] = num
        data_dict["name"] = name
        data_dict["price"] = price

        data_list.append(data_dict)

print(data_list)

# 4. csv 파일로 저장

import csv
csv_columns = ['no','name', 'price']
csv_file = 'naver_stock.csv'
try:
    with open(csv_file, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=csv_columns)
        writer.writeheader()
        for data in data_list:
            writer.writerow(data)
except:
    print("I/O Error")