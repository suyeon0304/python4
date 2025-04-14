import requests
from bs4 import BeautifulSoup
import random
import time

def fetch_genie_chart():
    """지니차트 웹사이트에서 차트 정보를 가져옵니다."""
    url = 'https://www.genie.co.kr/chart/top200'
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"웹 페이지 요청 실패 - 상태 코드: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    songs = soup.select('table.list-wrap tbody tr')

    chart = []
    for song in songs:
        title_tag = song.select_one('a.title')
        artist_tag = song.select_one('a.artist')
        rank_tag = song.select_one('td.number')

        if title_tag and artist_tag and rank_tag:
            title = title_tag.text.strip()
            artist = artist_tag.text.strip()
            rank = rank_tag.text.strip().split()[0]
            chart.append((rank, title, artist))
    return chart


def display_chart(chart, count):
    """지정된 수 만큼 차트 출력"""
    print("\n🎶 지니 TOP {} 곡 목록 🎶".format(count))
    print("-" * 40)
    for song in chart[:count]:
        print(f"{song[0]}위 | {song[1]} - {song[2]}")
    print("-" * 40)


def recommend_song(chart):
    """차트에서 랜덤 추천곡 출력"""
    print("\n🎧 AI 추천곡을 찾는 중입니다...")
    time.sleep(1)
    song = random.choice(chart)
    print(f"\n✨ 추천곡: {song[1]} - {song[2]} ({song[0]}위)")  


def show_menu():
    """메뉴 출력"""
    print("\n===============================")
    print("|         🎵 지니 차트 🎵        |")
    print("|-----------------------------|")
    print("| 1. TOP 100 보기             |")
    print("| 2. TOP 50 보기              |")
    print("| 3. TOP 10 보기              |")
    print("| 4. AI 추천곡                |")
    print("| 0. 종료하기                 |")
    print("===============================")


def main():
    """메인 프로그램 함수"""
    print("🌟 지니 차트 프로그램에 오신 걸 환영합니다 🌟")
    chart_data = fetch_genie_chart()

    if not chart_data:
        return  # 차트 가져오기 실패시 종료

    while True:
        show_menu()
        choice = input("👉 원하시는 메뉴 번호를 입력하세요: ")

        if choice == "1":
            display_chart(chart_data, 100)
        elif choice == "2":
            display_chart(chart_data, 50)
        elif choice == "3":
            display_chart(chart_data, 10)
        elif choice == "4":
            recommend_song(chart_data)
        elif choice == "0":
            print("👋 프로그램을 종료합니다. 감사합니다!")
            break
        else:
            print("❗ 유효한 메뉴 번호를 입력해주세요 (0~4)")

if __name__ == "__main__":
    main()
