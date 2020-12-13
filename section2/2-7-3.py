from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Fake Header 정보
ua = UserAgent()

# 헤더 선언
headers = {
    'User-Agent': ua.ie,
    'referer': 'https://finance.daum.net/'
}

base = "https://www.inflearn.com/"
# base = "https://www.inflearn.com/courses/it-programming/"
# quote = rep.quote_plus("추천-강좌") # 유니코드로 변환
# url = base + quote
# res = req.urlopen(url).read()

# res = req.urlopen(req.Request(base)).read().decode('utf-8')
res = req.urlopen(req.Request(base, headers=headers)).read().decode('utf-8')
soup = BeautifulSoup(res, "html.parser")

print(soup)

recommand = soup.select("ul.slides")[0]

# for i, e in enumerate(recommand, 1):
#     print(i, e.select_one("h4.block_title > a").string)
