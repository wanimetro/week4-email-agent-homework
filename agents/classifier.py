from openai import OpenAI

class EmailClassifier:

    def __init__(self, client, model):
        self.client = client
        self.model = model

    def classify(self, email):

        prompt = f"""
        From: {email['from']}
        Subject: {email['subject']}
        Body: {email['body']}
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": """
당신은 이메일 분류기입니다.

아래 다섯 개 중 하나만 출력하세요.

spam
no_reply
need_decision
no_decision
auto_reply

설명하지 말고 단어 하나만 출력하세요.
"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content.strip()