import random
from melon import get_melon_chart  # melon.py에서 get_melon_chart 함수 가져오기

# 멜론 차트에서 노래 목록 가져오기
songs = get_melon_chart()

# 노래 데이터가 있는지 확인
if not songs:
    print("❌ 멜론 차트 데이터를 가져오지 못했습니다.")
    exit()

# 사용자 입력 받기
print("\n🎵 원하는 기능을 선택하세요 🎵")
print("#1. 멜론 100곡 출력")
print("#2. 멜론 50곡 출력")
print("#3. 랜덤으로 한 곡 추천")
choice = input("번호를 입력하세요: ")

# 선택한 번호에 따라 동작
if choice == "1":
    print("\n📢 멜론 TOP 100곡 목록 📢")
    for i, song in enumerate(songs[:100], 1):
        print(f"{i}. {song}")

elif choice == "2":
    print("\n📢 멜론 TOP 50곡 목록 📢")
    for i, song in enumerate(songs[:50], 1):
        print(f"{i}. {song}")

elif choice == "3":
    recommended_song = random.choice(songs)
    print("\n🎶 AI 추천 노래 🎶")
    print(f"👉 {recommended_song}")

else:
    print("❌ 올바른 번호를 입력하세요.")
