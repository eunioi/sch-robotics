# 내용 작성 예시
#if __name__ == "__main__":
#    print("hello python, hi ros.")

#다음엔 기존에 있던 anything.py를 변경한다. (gedit anything.py)

from add_lists import add_lists

if __name__ == "__main__":
    result = add_lists(['wel', 't', 'r'], ['come', 'o', 'os'])
    print(result)
