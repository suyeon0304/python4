import random
import time

songs = ["a노래", "b노래", "c노래", "d노래"]
print(songs)
print(songs[0])
print(songs[1])
print(songs[2])
print(songs[3])

for song in songs:
    print(song)   

print("AI야 노래 한곡만 추천해줘") 
print("""
알겠습니다. 
제가 열심히 분석해서 
고객님께 노래를 한곡 
추천합니다
      """) 

# AI가 노래를 추천하는 부분
ai_song = random.choice(songs)
dd = ["두", "두", "두", "두둥"]
for d in dd:
    print(d)
    time.sleep(1)

print(f"제가 추천한 곡은 {ai_song}입니다.") 
