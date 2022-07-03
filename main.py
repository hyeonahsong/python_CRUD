# __name__=__main__
# main안에서 호출 되는 건 파일 자체를 실행 했을 때만 호출된다
# ctrl + shift + f10 -> 현재 py파일 실행
# def -> js의 function과 비슷한 역할

def cat(who, many):
    print("{}의 고양이는 {}마리입니다!".format(who, many))

if __name__ == '__main__':
    cat('염정아', 82)