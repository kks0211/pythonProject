import os
import subprocess

import pytube

yt = pytube.YouTube("https://www.youtube.com/watch?v=v2lqhMb7YT8")  # 다운받을 동영상 URL 지정
# yt = pytube.YouTube("https://class101.net/classes/5e2556a44ba7b950bbd46bb4/contents/5e840848c0802a51e24bdd1c")  # 다운받을 동영상 URL 지정

vids = yt.streams.all()

# 영상 형식 리스트 확인
for i in range(len(vids)):
    print(i, '. ', vids[i])

# vnum = int(input("다운 받을 화질은? "))

parent_dir = "C:/Users/Kwan/Documents/pythonTest/"
# vids[vnum].download(parent_dir)  # 다운로드 수행
vids[0].download(parent_dir)  # 다운로드 수행

# new_filename = input("변환 할 mp3 파일명은?")
#
default_filename = vids[0].default_filename
subprocess.call(['C:/Users/Kwan/Documents/pythonTest/ffmpeg', '-i',  # cmd 명령어 수행
                 os.path.join(parent_dir, default_filename),
                 os.path.join(parent_dir, "test.mp3")
                 ])

print('동영상 다운로드 및 mp3 변환 완료!')
