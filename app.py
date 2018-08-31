import os
import random
import requests
from flask import Flask, jsonify, request
#jsonify : 딕셔너리 -> JSON으로 변환해주는 모듈

app = Flask(__name__)

@app.route('/')
def hello():
    return "여기는 챗봇 페이지입니다!"

# 참고페이지(카카오톡 자동응답기능) : https://github.com/plusfriend/auto_reply

        
@app.route('/keyboard')
def keyboard(): #딕셔너리 형태(key와 value), 웹에서는 JSON타입, 자바에서는 MAP
    keyboard = {
    "type" : "buttons",
    "buttons" : ["메뉴", "로또", "고양이","영화"]
    }
    
    return jsonify(keyboard) #딕셔너리->JSON 변환

@app.route('/message', methods=['POST'])
def message():
    user_msg = request.json['content'] #content 요청해서 user_msg에 담기
    img_bool = False
    
    if user_msg == "메뉴":
        menu = ["20층", "멀캠식당", "보쌈집","김치찌개집"]
        return_msg = random.choice(menu)
    elif user_msg == "로또":
        numbers = list(range(1,46)) # 1~45까지 넣기 앞 숫자 이상, 뒷 숫자 미만. 그리고 리스트화.
        pick = random.sample(numbers, 6)
        return_msg = str(sorted(pick)) #여기서 message는 string값이기 때문에 바꿔줘야한다. 그리고 정렬까지. 대신 원본은 놔두고 정렬해서 리턴
    elif user_msg == "고양이":
        img_bool = True
        url = "https://api.thecatapi.com/v1/images/search?mime_types=jpg"
        req = requests.get(url).json()
        return_img = req[0]['url']
        return_msg = "나만 고양이 없어 :("
    elif user_msg == "영화":
        
        
            
    else:    
        return_msg = "메뉴만 사용 가능!!!"
    
    if img_bool == True:
        return_json = { #딕셔너리 안에 또 딕셔너리 구조. 헷갈리지않게 들여쓰기 잘하기. 그리고 type자체를 주의하자.
            "message": {
                "text": return_msg,
                "photo": { #url이 아닌 사진을 넘겨줘야한다.
                    "url":return_img, #같은 레벨의 항목들은 ,로 구분
                    "width":720,
                    "height": 630
                    
                }
            },
            "keyboard": {
                "type" : "buttons",
                "buttons" : ["메뉴", "로또", "고양이","영화"]
            }
        }
    
    else:
        return_json = { 
            "message": {
                "text": return_msg
            },
            "keyboard": {
                "type" : "buttons",
                "buttons" : ["메뉴", "로또", "고양이","영화"]
            }
        }
        
    return jsonify(return_json)
    
    


app.run(host=os.getenv('IP','0.0.0.0'), port=int(os.getenv('PORT',8080)))