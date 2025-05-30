from openai import OpenAI
import os
from dotenv import load_dotenv
from pathlib import Path
import json 

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def load_feeling () :
    data = json.loads(Path('data.json').read_text())
    return data

def save_feeling (date, feeling) :
    data = json.loads(Path('data.json').read_text())
    data.append({date: feeling})
    with Path('data.json').oepn('w+t', encoding='utf8') as fp: json.dump(data, fp, indent=4, ensure_ascii=False)
    print("감정이 저장되었습니다!")
    

def load_ai (diary_text) : # 참고: https://wikidocs.net/217882
    system_prompt = """
    당신은 감정 분석기입니다.
    입력된 일기를 읽고 6가지 감정의 점수를 0.0부터 1.0 사이 실수로 평가하세요.
    형식은 반드시 다음과 같아야 합니다 (절대 변경하지 마세요):
    기쁨: 0.x
    두려움: 0.x
    슬픔: 0.x
    지침: 0.x
    짜증: 0.x
    혐오: 0.x

    규칙:
    - 최대값이 2개 이상 겹치지 않도록 합니다.
    - 점수의 총합은 맞출 필요 없습니다.
    - 분석만 수행하고 설명이나 다른 출력은 하지 마세요.
        """
    
    client = OpenAI(api_key=api_key)
    try :
        response = client.chat.completions.create(
            model="gpt-4o",
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": diary_text}
            ],
            temperature = 0.3
        )
    except Exception as e:
        print(f"에러 발생: {e}")
        return "⚠️ 감정 분석에 실패했습니다. API 제한을 확인해주세요."
    
    return response.choices[0].message.content

def chat () :
    while True :
        input_msg = input("일기를 작성할 날짜를 입력해주세요 (YYYYMMDD, ex: 20250530) ")
        if len(input_msg) != 8 :
            print("잘못입력하셨습니다.")
            continue 
        
        try :
            date = int(input_msg)
        except Exception as e:
            print(e, "\n 제대로 다시 입력하세요")
            continue
        
        feeling_msg = input("오늘 어떤 일이 있었나요? \n")
        print(load_ai(feeling_msg))
        
        
        
        
        
            

