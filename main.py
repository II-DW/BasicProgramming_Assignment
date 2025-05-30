from dotenv import load_dotenv
import os

# .env 파일 불러오기
load_dotenv()

# 환경변수에서 불러오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
