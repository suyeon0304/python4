import requests
from bs4 import BeautifulSoup

# 지니뮤직 차트 순위를 알 수 있는 URL (지니뮤직 차트 페이지 URL로 수정 필요)
url = 'https://www.genie.co.kr/chart/top200'

# 웹 페이지 요청을 위한 헤더 추가 (User-Agent는 일반적인 브라우저처럼 요청을 보내기 위해 추가)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 웹 페이지 요청 보내기
response = requests.get(url, headers=headers)

# 응답 코드 확인
print(f"응답 코드: {response.status_code}")

# 요청이 성공했으면 웹 페이지 파싱
if response.status_code == 200:
    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 웹 페이지 구조 확인 (HTML 구조 보기)
    # soup.prettify()를 사용하여 HTML을 보기 쉽게 출력할 수 있습니다. 
    # 이렇게 출력하면 페이지의 구조를 확인할 수 있습니다.
    # print(soup.prettify())  # 이 줄을 활성화하면 HTML 구조를 확인할 수 있습니다.

    # 'tr' 또는 다른 태그에서 차트 순위를 포함하는 요소를 찾습니다.
    # 지니뮤직에서 실제 HTML 구조를 확인하고, 순위를 가져올 수 있는 태그를 찾아야 합니다.
    # 예를 들어, 'tr' 태그와 'class' 이름을 바탕으로 곡 정보를 추출합니다.

    # 예시: 차트 순위의 곡 제목을 추출 (여기서는 실제 HTML 구조에 맞춰서 수정해야 합니다)
    # 예시로 'class'가 'title'인 'tr' 태그를 찾는 방식
    songs = soup.find_all('tr', class_='list')  # 실제 클래스명을 사용해야 합니다.

    # 차트 순위 출력
    if songs:
        for idx, song in enumerate(songs, start=1):
            title = song.find('a', class_='title').text.strip()  # 곡 제목 추출
            artist = song.find('a', class_='artist').text.strip()  # 아티스트 이름 추출
            print(f"순위 {idx}: {title} - {artist}")
    else:
        print("차트 순위를 찾을 수 없습니다.")
else:
    print("웹 페이지를 불러오는 데 실패했습니다.")
