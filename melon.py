
import requests
from bs4 import BeautifulSoup

# 멜론 차트 URL
url = 'https://www.melon.com/chart/index.htm'

# 헤더 설정 (멜론은 User-Agent를 확인하기 때문에 필요)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 웹 페이지 요청
response = requests.get(url, headers=headers)

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 순위, 곡명, 아티스트 가져오기
songs = soup.select('tr.lst50, tr.lst100')  # 1~100위 데이터

for rank, song in enumerate(songs, start=1):
    title = song.select_one('div.ellipsis.rank01 a').text  # 곡명
    artist = song.select_one('div.ellipsis.rank02 a').text  # 아티스트
    print(f"{rank}위: {title} - {artist}")
