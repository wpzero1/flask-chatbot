import requests

url = "https://api.thecatapi.com/v1/images/search?mime_types=jpg"
req = requests.get(url).json()

print(req[0]['url']) #위 url을 들어가보면 리스트로 json을 넘겨주고있다. 그래서 찾아줘야한다.
# print(type(req)) #typeerror떴을 때 확인해보기