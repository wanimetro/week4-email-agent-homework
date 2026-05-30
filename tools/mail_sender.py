def send_auto_reply(email):

    print()
    print("===== 자동 답장 =====")
    print("받는 사람 :", email["from"])
    print("제목 :", email["subject"])
    print("답장 : 요청 감사합니다. 확인 후 전달드리겠습니다.")
    print("====================")
    print()