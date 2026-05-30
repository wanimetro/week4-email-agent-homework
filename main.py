import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from tools.spam_db import save_spam
from tools.notify import notify_user
from tools.mail_sender import send_auto_reply

from concurrent.futures import ThreadPoolExecutor


load_dotenv()

print("API KEY =", os.getenv("OPENAI_API_KEY"))

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "save_spam",
            "description": "스팸 메일을 spam_db에 저장",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "notify_user",
            "description": "의사결정이 필요한 메일을 사용자에게 알림",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "send_auto_reply",
            "description": "자동 답장이 가능한 메일에 답장",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]



with open("data/mails.json", "r", encoding="utf-8") as f:
    mails = json.load(f)

def process_email(mail):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """
                이메일을 분석하고 필요한 tool을 선택하세요.

                spam -> save_spam
                need_decision -> notify_user
                auto_reply -> send_auto_reply

                나머지는 tool 호출하지 마세요.
                """
            },
            {
                "role": "user",
                "content": f"""
                Subject: {mail['subject']}
                Body: {mail['body']}
                """
            }
        ],
        tools=TOOLS,
        tool_choice="auto"
    )

    tool_calls = response.choices[0].message.tool_calls

    print("=" * 40)
    print(mail["subject"])

    if tool_calls:

        tool_name = tool_calls[0].function.name

        print("선택된 Tool :", tool_name)

        if tool_name == "save_spam":
            save_spam(mail)

        elif tool_name == "notify_user":
            notify_user(mail)

        elif tool_name == "send_auto_reply":
            send_auto_reply(mail)

    else:
        print("선택된 Tool 없음")

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(process_email, mails)