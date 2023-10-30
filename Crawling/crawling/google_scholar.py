# selenium 만으로는 chrome driver를 조정하기 어렵기 때문에 chromedriver를 같이 사용
from selenium import webdriver
import time
import requests
import json
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# chrome driver 자동 다운 및 설정
ChromeDriverManager().install()
driver = webdriver.Chrome() # 우리가 컨트롤 할 수 있는 브라우저가 실행이 된다.


# Google Scholar 페이지로 이동
url = "https://scholar.google.com"
driver.get(url)

# 검색어 입력
search_box = driver.find_element("name", "q")
search_box.send_keys("hbv hiv coinfection")
search_box.submit()


time.sleep(2)

hbvhiv_coinfec = []

# 논문 정보 가져오기
papers = driver.find_elements("class name", "gs_ri")

for paper in papers:
    title = paper.find_element("class name", "gs_rt").text
    authors = paper.find_element("class name", "gs_a").text
    citations = paper.find_element("class name", "gs_fl").text
    
    print("제목:", title)
    print("저자:", authors)
    print("인용자수:", citations)
    
    # PDF 링크가 있는 경우
    try:
        pdf_link = paper.find_element("class name", "gs_or_moreresults")
        pdf_url = pdf_link.get_attribute("href")
        print("PDF 다운로드 링크:", pdf_url)
    except:
        print("PDF 다운로드 링크가 없습니다.")

    print("\n")

    data = {
        "title" : title,
        "authors" : authors,
        "citations" : citations
    }
    hbvhiv_coinfec.append(data)
    

df = pd.DataFrame(hbvhiv_coinfec) # df = excel
print(df)

df.to_csv("hbvhiv_coinfec.csv", encoding='utf-8-sig', index=False)


# Slack Incoming Webhook URL
slack_url = 'https://hooks.slack.com/services/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'

# Slack에 보낼 메시지
msg = "\n".join([f"{i + 1}. {row['title']} - {row['authors']}\n{row['citations']}" for i, row in df.iterrows()])

# JSON 형식으로 메시지 작성
payload = {
    "text": msg
}

# Slack으로 POST 요청 전송
response = requests.post(slack_url, data=json.dumps(payload), headers={"Content-Type": "application/json"})

# 요청이 성공적으로 전송되었는지 확인
if response.status_code == 200:
    print("논문 정보가 Slack에 성공적으로 전송되었습니다.")
else:
    print("Slack으로 논문 정보 전송에 실패했습니다.")



# 브라우저 닫기
driver.quit()



