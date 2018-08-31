import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.nhn"
req = requests.get(url).text
doc = BeautifulSoup(req, 'html.parser') #번역작업 정도... 

title_tag = doc.select('dt.tit > a') #copy - selector도 있지만, 구조를 보고 직접 찾아간 방식도 있다.
star_tag = doc.select('div.star_t1 > a > span.num')
reserve_tag = doc.select('div.star_t1.b_star > span.num') #이 경우에는 div가 2개 있는데 띄어쓰기를 .으로 대신 써주면 된다.
img_tag = doc.select('div.thumb > a > img')

# 트리구조. ex)폴더 디렉토리
# 해당 항목이 있는 디렉토리를 찾아주자. 제일 깊은데서 시작해서 왼쪽으로 가자.

#print(type(text)) #list구조

# title_list = [] #영화제목 빈 배열 만들기
# star_list = [] #별점
# reserve_list = [] #예약

# 상위 10개만 담는 for문 작성

# for i in range(0,10):
#     title_list.append(title_tag[i].text)

# 다른 방법 : 딕셔너리에 넣어보기
movie_dict = {}

for i in range(0,10):
    movie_dict[i] = {
        "title":title_tag[i].text,
        "star":star_tag[i].text,
        "reserve":reserve_tag[i].text,
        "img":img_tag[i]['src'] #대괄호 대신 .get('src')도 가능
    }

#len으로 길이를 측정해봐도 좋다.
#print(len(title_tag))
# print(len(star_tag))
# print(len(reserve_tag))

print(movie_dict)
