import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

imgUrl = "http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg"
htmlURL = "http://google.com"

savePath1 = "C:/Users/Kwan/Documents/pythonTest/test1.jpg"
savePath2 = "C:/Users/Kwan/Documents/pythonTest/index.html"

# 저장 -> open('r') -> 변수에 할당 -> 파싱 -> 저장
# for문 돌려서 데이터 가져올때 좋음
dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savePath2)


print("다운로드 완료!")
