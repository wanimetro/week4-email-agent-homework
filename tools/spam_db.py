import json

def save_spam(email):

    try:
        with open(
            "data/spam_db.json",
            "r",
            encoding="utf-8"
        ) as f:
            spam_list = json.load(f)

    except:
        spam_list = []

    spam_list.append(email)

    with open(
        "data/spam_db.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            spam_list,
            f,
            ensure_ascii=False,
            indent=4
        )

    print(f"[SPAM 저장] {email['subject']}")