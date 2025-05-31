from openai import OpenAI
import os
from dotenv import load_dotenv
from pathlib import Path
import json 

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
feelings_L = ["기쁨", "두려움", "슬픔", "지침", "짜증", "혐오"]

def load_feeling () :
    data = json.loads(Path('data.json').read_text())
    return data

def save_feeling (date, feeling) :
    data = json.loads(Path('data.json').read_text())
    date = str(date)
    if date in data:
        while True :
            input_msg = input("이미 해당 일자에 저장된 날짜가 있습니다. 대체하시겠습니까? 원래 감정을 유지하겠습니까? (0: 대체, 1: 유지) : ")
            if input_msg == "0" :
                break
            elif input_msg == "1" :
                return
            else :
                print("제대로 다시 입력하십시오")
                continue
    data[date] = feeling
    with Path('data.json').open('w+t', encoding='utf8') as fp: json.dump(data, fp, indent=4, ensure_ascii=False)
    print("감정이 저장되었습니다!")
    

def load_ai (diary_text) :
    system_prompt = """
    You are an emotion analyzer.
    Read the given diary entry and evaluate the scores of six emotions as floating-point numbers between 0.0 and 1.0.
    The format must always be exactly as follows (never change it under any circumstances):
    Joy: 0.x
    Fear: 0.x
    Sadness: 0.x
    Fatigue: 0.x
    Annoyance: 0.x
    Disgust: 0.x

    Rules:
    - No more than one emotion can share the highest score.
    - The total sum of the scores does not need to add up to any specific value.
    - Only provide the analysis. Do not give any explanations or additional output.
    """
    
    # client = OpenAI(
    # base_url="https://openrouter.ai/api/v1",
    # api_key=api_key,
    # )
    # while True :
    #     try :
    #         completion = client.chat.completions.create(
    #         extra_headers={
    #             "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    #             "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    #         },
    #         extra_body={},
    #         model="deepseek/deepseek-r1-0528:free",
    #         messages=[
    #             {
    #                 "role": "system",
    #                 "content": system_prompt
    #             },
    #             {
    #             "role": "user",
    #             "content": diary_text
    #             }
    #         ]
    #         )
    #         try:
    #             response = [float(feelings.split(':')[1]) for feelings in completion.choices[0].message.content.split("\n")]
    #         except Exception as e :
    #             print(f"에러 발생: {e}")
    #             print("⚠️ LLM이 제대로 된 값을 제공하지 않았습니다. 재시도 중입니다.")
    #             continue
    #         if len(response) != 6 :
    #             print("⚠️ LLM이 제대로 된 값을 제공하지 않았습니다. 재시도 중입니다.")
    #             continue
    #         return response
    #     except Exception as e:
    #         print(f"에러 발생: {e}")
    #         return "⚠️ 감정 분석에 실패했습니다. API 제한을 확인해주세요."
    return [0.0, 1.0, 0.0, 0.0, 0.0, 0.0]
    
    

def chat () :
    while True :
        input_msg = input("일기를 작성할 날짜를 입력해주세요 (YYYYMMDD, ex: 20250530), 종료: 0 ")
        if input_msg == "0" :
            break
        if len(input_msg) != 8 :
            print("잘못입력하셨습니다.")
            continue 
        
        try :
            date = int(input_msg)
        except Exception as e:
            print(e, "\n 제대로 다시 입력하세요")
            continue
        
        feeling_msg = input("오늘 어떤 일이 있었나요? \n")
        response = load_ai(feeling_msg)
        
        save_feeling(date, feelings_L[response.index(max(response))])
        
        
        
        
        
            

