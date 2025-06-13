from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
import time

def get_weather(city):
    # Chrome 옵션 설정 (headless 모드)
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # GUI 없이 실행
    chrome_options.add_argument('--no-sandbox')  # 샌드박스 비활성화
    chrome_options.add_argument('--disable-dev-shm-usage')  # 메모리 최적화
    chrome_options.add_argument('--disable-gpu')  # GPU 비활성화
    chrome_options.add_argument('--remote-debugging-port=9222')  # 디버깅 포트
    chrome_options.add_argument('--user-data-dir=/tmp/chrome_user_data')  # 사용자 데이터 디렉토리 지정
    
    try:
        # 크롬 드라이버 실행
        driver = webdriver.Chrome(options=chrome_options)
        
        # 네이버 날씨 검색 URL
        url = f"https://search.naver.com/search.naver?query={city}+날씨"
        driver.get(url)
        
        # 페이지 로딩 대기
        time.sleep(3)
        
        # 날씨 정보 가져오기 (여러 셀렉터 시도)
        temperature = "정보 없음"
        
        # 다양한 셀렉터로 시도
        selectors = [
            ".temperature_text",
            ".current .temperature",
            ".today_weather .temperature",
            ".weather_temperature",
            "[class*='temperature']"
        ]
        
        for selector in selectors:
            try:
                temp_element = driver.find_element(By.CSS_SELECTOR, selector)
                temperature = temp_element.text.strip()
                if temperature:
                    break
            except:
                continue
                
        driver.quit()
        return temperature
        
    except Exception as e:
        print(f"날씨 정보를 가져오는 중 오류 발생: {e}")
        return "날씨 정보를 가져올 수 없습니다"

def recommend(category, weather):
    # 날씨에서 온도 추출 시도
    temp = 20  # 기본값
    try:
        import re
        temp_match = re.search(r'(-?\d+)°?[C℃]', weather)
        if temp_match:
            temp = int(temp_match.group(1))
    except:
        pass

    if category == "의상":
        recommendations = []
        
        # 온도별 기본 의상
        if temp < 0:
            tops = ["두꺼운 패딩", "롱 코트", "퍼 코트", "울 코트"]
            bottoms = ["기모 바지", "두꺼운 청바지", "레깅스+스커트"]
            accessories = ["목도리", "장갑", "털모자", "부츠", "핫팩"]
        elif temp < 10:
            tops = ["패딩 조끼", "바람막이", "두꺼운 니트", "후드집업"]
            bottoms = ["청바지", "면바지", "긴 치마+스타킹"]
            accessories = ["가벼운 머플러", "운동화", "앵클부츠"]
        elif temp < 20:
            tops = ["가디건", "얇은 니트", "긴팔 셔츠", "후드티"]
            bottoms = ["청바지", "면바지", "긴 치마", "슬랙스"]
            accessories = ["스니커즈", "로퍼", "가벼운 재킷"]
        elif temp < 28:
            tops = ["반팔 티셔츠", "얇은 블라우스", "린넨 셔츠", "민소매"]
            bottoms = ["면바지", "치노 팬츠", "짧은 치마", "원피스"]
            accessories = ["샌들", "운동화", "선글라스"]
        else:
            tops = ["민소매", "나시", "크롭탑", "시원한 블라우스"]
            bottoms = ["반바지", "미니스커트", "원피스", "린넨 팬츠"]
            accessories = ["샌들", "모자", "선글라스", "부채"]
        
        # 날씨별 추가 아이템
        if "비" in weather or "우" in weather:
            accessories.extend(["우산", "레인부츠", "우비", "방수 재킷"])
        if "바람" in weather or "강풍" in weather:
            accessories.extend(["바람막이", "머리끈", "가벼운 스카프"])
        if "눈" in weather:
            accessories.extend(["방한부츠", "장갑", "목도리"])
            
        # 추천 조합 생성
        recommendations.append(f"👕 상의: {random.choice(tops)}")
        recommendations.append(f"👖 하의: {random.choice(bottoms)}")
        recommendations.append(f"👟 액세서리: {', '.join(random.sample(accessories, min(2, len(accessories))))}")
        
        return recommendations

    elif category == "음악":
        recommendations = []
        
        # 날씨와 온도에 따른 감성적 첫 문장과 노래 추천
        if "비" in weather:
            rainy_songs = [
                "폴킴 - 비", "헤이즈 - 비도 오고 그래서", "다비치 - 비가 오는 날엔", 
                "아이유 - 가을 아침", "볼빨간사춘기 - 나만 안되는 연애", "멜로망스 - 선물",
                "성시경 - 거리에서", "윤하 - 비밀번호 486", "브라운 아이드 걸스 - 한 여름밤의 꿈",
                "장범준 - 비가 내리는 날에는", "정승환 - 비가 온다", "백지영 - 총 맞은 것처럼"
            ]
            song_list = random.sample(rainy_songs, 4)
            recommendations.append(f"🌧️ 비 오는 감성엔 역시 잔잔한 발라드가 제격이죠! 빗소리와 함께 듣기 좋은 노래들을 추천해드릴게요:")
            
        elif "맑음" in weather or "화창" in weather:
            if temp > 25:
                sunny_songs = [
                    "BTS - Dynamite", "뉴진스 - Hype Boy", "아이유 - 좋은 날", 
                    "트와이스 - What Is Love?", "비투비 - 봄날의 기억", "마마무 - 고고베베",
                    "선미 - 가시나", "세븐틴 - 아낀다", "레드벨벳 - 빨간 맛",
                    "에스파 - Next Level", "잔나비 - 꿈과 책과 힘과 벽", "악뮤 - 낙하"
                ]
                song_list = random.sample(sunny_songs, 4)
                recommendations.append(f"☀️ 이런 화창하고 더운 날엔 시원하고 상큼한 여름 감성의 노래들이 딱이에요!")
            else:
                sunny_songs = [
                    "BTS - Dynamite", "뉴진스 - Hype Boy", "아이유 - 좋은 날", 
                    "트와이스 - What Is Love?", "비투비 - 봄날의 기억", "마마무 - 고고베베",
                    "선미 - 가시나", "세븐틴 - 아낀다", "레드벨벳 - 빨간 맛",
                    "에스파 - Next Level", "잔나비 - 꿈과 책과 힘과 벽", "악뮤 - 낙하"
                ]
                song_list = random.sample(sunny_songs, 4)
                recommendations.append(f"☀️ 맑고 상쾌한 날씨네요! 기분 좋게 신나는 노래들로 하루를 시작해보세요:")
            
        elif "흐림" in weather:
            if temp < 10:
                cloudy_songs = [
                    "아이유 - 밤편지", "김광석 - 서른 즈음에", "이소라 - 바람이 분다",
                    "윤종신 - 좋니", "장기하와 얼굴들 - 그렇고 그런 사이", "허각 - 헬로",
                    "볼빨간사춘기 - 우주를 줄게", "악뮤 - 어떻게 이별까지 사랑하겠어", "10cm - 폰서트",
                    "자우림 - 25, 21", "페퍼톤스 - 맨발의 청춘", "시실 - 이 밤이 지나면"
                ]
                song_list = random.sample(cloudy_songs, 4)
                recommendations.append(f"☁️ 흐리고 쌀쌀한 날씨네요. 따뜻한 차 한 잔과 함께 감성적인 노래들을 들어보세요:")
            else:
                cloudy_songs = [
                    "아이유 - 밤편지", "김광석 - 서른 즈음에", "이소라 - 바람이 분다",
                    "윤종신 - 좋니", "장기하와 얼굴들 - 그렇고 그런 사이", "허각 - 헬로",
                    "볼빨간사춘기 - 우주를 줄게", "악뮤 - 어떻게 이별까지 사랑하겠어", "10cm - 폰서트",
                    "자우림 - 25, 21", "페퍼톤스 - 맨발의 청춘", "시실 - 이 밤이 지나면"
                ]
                song_list = random.sample(cloudy_songs, 4)
                recommendations.append(f"☁️ 흐린 날씨엔 차분하고 감성적인 노래가 잘 어울려요. 여유로운 시간을 보내보세요:")
            
        elif "눈" in weather:
            snowy_songs = [
                "아이유 - 겨울잠", "태연 - I", "볼빨간사춘기 - 썸 탈꺼야",
                "정승환 - 눈사람", "케이윌 - 이러지마 제발", "버스커 버스커 - 겨울밤",
                "성시경 - 내게 오는 길", "백아연 - 느린 노래", "에일리 - 첫눈처럼 너에게 가겠다",
                "선미 - 보라빛 밤", "멜로망스 - 선물", "임창정 - 그때 또 다시"
            ]
            song_list = random.sample(snowy_songs, 4)
            recommendations.append(f"❄️ 눈이 내리는 겨울 날씨네요! 따뜻한 실내에서 로맨틱한 겨울 감성을 만끽해보세요:")
            
        elif "바람" in weather or "강풍" in weather:
            if temp < 10:
                windy_songs = [
                    "이소라 - 바람이 분다", "김동률 - 기억의 습작", "윤종신 - 오르막길",
                    "성시경 - 두 사람", "이문세 - 광화문 연가", "서태지 - 시대유감",
                    "잔나비 - 주저하는 연인들을 위해", "혁오 - 위잉위잉", "검정치마 - 모든 말들"
                ]
                song_list = random.sample(windy_songs, 3)
                recommendations.append(f"💨 차가운 바람이 많이 부는 날씨네요! 마음까지 시원해지는 감성적인 노래들을 들어보세요:")
            else:
                windy_songs = [
                    "이소라 - 바람이 분다", "김동률 - 기억의 습작", "윤종신 - 오르막길",
                    "성시경 - 두 사람", "이문세 - 광화문 연가", "서태지 - 시대유감",
                    "잔나비 - 주저하는 연인들을 위해", "혁오 - 위잉위잉", "검정치마 - 모든 말들"
                ]
                song_list = random.sample(windy_songs, 3)
                recommendations.append(f"💨 시원한 바람이 부는 날씨네요! 상쾌한 바람처럼 청량한 노래들을 들어보세요:")
        else:
            # 온도별 기본 추천
            if temp < 5:
                popular_songs = [
                    "NewJeans - Get Up", "아이브 - 러브 다이브", "세븐틴 - 신", 
                    "르세라핌 - UNFORGIVEN", "스트레이 키즈 - 특", "에스파 - Spicy",
                    "지코 - 새삥", "키드 밀리 - 불타는 태양", "빅뱅 - 봄여름가을겨울",
                    "블랙핑크 - 마지막처럼", "레드벨벳 - 피카부", "엔시티 드림 - ISTJ"
                ]
                song_list = random.sample(popular_songs, 4)
                recommendations.append(f"🥶 정말 추운 날씨네요! 몸은 춥지만 마음만은 따뜻해질 수 있는 인기곡들을 추천해드릴게요:")
            elif temp > 30:
                popular_songs = [
                    "NewJeans - Get Up", "아이브 - 러브 다이브", "세븐틴 - 신", 
                    "르세라핌 - UNFORGIVEN", "스트레이 키즈 - 특", "에스파 - Spicy",
                    "지코 - 새삥", "키드 밀리 - 불타는 태양", "빅뱅 - 봄여름가을겨울",
                    "블랙핑크 - 마지막처럼", "레드벨벳 - 피카부", "엔시티 드림 - ISTJ"
                ]
                song_list = random.sample(popular_songs, 4)
                recommendations.append(f"🔥 정말 더운 날씨네요! 시원한 감성을 느낄 수 있는 상큼한 노래들로 더위를 날려보세요:")
            else:
                popular_songs = [
                    "NewJeans - Get Up", "아이브 - 러브 다이브", "세븐틴 - 신", 
                    "르세라핌 - UNFORGIVEN", "스트레이 키즈 - 특", "에스파 - Spicy",
                    "지코 - 새삥", "키드 밀리 - 불타는 태양", "빅뱅 - 봄여름가을겨울",
                    "블랙핑크 - 마지막처럼", "레드벨벳 - 피카부", "엔시티 드림 - ISTJ"
                ]
                song_list = random.sample(popular_songs, 4)
                recommendations.append(f"🎵 적당한 날씨네요! 언제 들어도 좋은 인기 차트곡들을 추천해드릴게요:")
            
        for i, song in enumerate(song_list, 1):
            recommendations.append(f"   {i}. {song}")
        recommendations.append(f"📱 멜론/지니/스포티파이에서 검색해서 들어보세요!")
        
        return recommendations

    elif category == "여가":
        recommendations = []
        
        # 날씨별 여가활동
        if "비" in weather or "눈" in weather:
            indoor = ["영화관", "카페", "도서관", "쇼핑몰", "박물관", "미술관", "찜질방", "노래방"]
            home = ["넷플릭스 시청", "독서", "요리", "게임", "온라인 쇼핑", "홈 트레이닝"]
            recommendations.append(f"🏠 실내활동: {', '.join(random.sample(indoor, 3))}")
            recommendations.append(f"🏡 집에서: {', '.join(random.sample(home, 2))}")
        elif "맑음" in weather and temp > 15:
            outdoor = ["공원 산책", "한강 나들이", "자전거", "등산", "피크닉", "야외 카페"]
            active = ["테니스", "배드민턴", "조깅", "인라인 스케이트", "축구"]
            recommendations.append(f"🌳 야외활동: {', '.join(random.sample(outdoor, 3))}")
            recommendations.append(f"⚽ 운동: {', '.join(random.sample(active, 2))}")
        else:
            mixed = ["쇼핑", "카페 투어", "전시회", "데이트", "친구 만나기", "맛집 탐방"]
            cultural = ["영화관", "연극", "콘서트", "뮤지컬", "갤러리"]
            recommendations.append(f"🎭 문화활동: {', '.join(random.sample(cultural, 2))}")
            recommendations.append(f"👥 사회활동: {', '.join(random.sample(mixed, 3))}")
            
        return recommendations
    
    return ["추천 불가"]

if __name__ == "__main__":
    print("=" * 50)
    print("🌤️  날씨 기반 추천 시스템  🌤️")
    print("=" * 50)
    
    city = input("도시를 입력하세요: ")
    print(f"\n📍 {city}의 날씨 정보를 가져오는 중...")
    
    weather = get_weather(city)
    print(f"🌡️  {city} 현재 날씨: {weather}\n")

    category = input("추천받을 항목을 선택하세요 (의상/음악/여가): ")
    results = recommend(category, weather)
    
    print(f"\n✨ {category} 추천 결과:")
    print("-" * 30)
    for result in results:
        print(f"  {result}")
    print("\n" + "=" * 50)