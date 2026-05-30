# Email Agent Assignment

## 프로젝트 소개

LLM을 활용하여 이메일을 자동으로 분류하고 적절한 액션을 수행하는 이메일 에이전트 시스템입니다.

실제 Gmail 대신 Dummy Mail 데이터를 사용하였으며, Function Calling과 병렬 처리 기능을 구현하였습니다.

---

## 주요 기능

### 1. 이메일 분류

이메일을 다음 5가지 카테고리로 분류합니다.

* spam
* no_reply
* need_decision
* no_decision
* auto_reply

---

### 2. Function Calling

OpenAI Tool Calling(Function Calling)을 사용하여 이메일 유형에 따라 적절한 함수를 호출합니다.

| Tool            | 설명       |
| --------------- | -------- |
| save_spam       | 스팸 메일 저장 |
| notify_user     | 사용자 알림   |
| send_auto_reply | 자동 답장    |

---

### 3. 병렬 처리

ThreadPoolExecutor를 활용하여 여러 이메일을 동시에 처리합니다.

```python
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(process_email, mails)
```

---

## 프로젝트 구조

```text
email-agent/

├── agents/
│   ├── classifier.py
│   ├── decision_agent.py
│   └── reply_agent.py
│
├── tools/
│   ├── spam_db.py
│   ├── notify.py
│   └── mail_sender.py
│
├── data/
│   ├── mails.json
│   └── spam_db.json
│
└── main.py
```

---

## 실행 방법

```bash
pip install -r requirements.txt
python main.py
```

---
