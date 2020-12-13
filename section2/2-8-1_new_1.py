import errno

from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("연애인")
url = base + quote

res = req.urlopen(url)
# savePath = "C:\\imagedown\\"  # C:\imagedown\
savePath = "C:/Users/Kwan/Documents/pythonTest/img1/"

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        raise

soup = BeautifulSoup(res, "html.parser")
img_list = soup.select("div.img_area > a.thumb._thumb > img")

# enumerate 란
# 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있습니다. 이때 사용합니다.
# 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환
# tuple은 리스트와 비슷 지만 값을 바꿀수 없음.
for i, img_list in enumerate(img_list, 1):
    # print(img_list['data-source'])
    fullFileName = os.path.join(savePath, savePath + str(i) + '.jpg')
    req.urlretrieve(img_list['data-source'], fullFileName)

print("다운로드 완료")
