while True:
    try:
        print(input())
    except EOFError: #EOFError = 파일의 끝(end of file)
        break