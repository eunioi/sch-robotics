# 내용 작성 예시
#if __name__ == "__main__":
#    print("hello python, hi ros.")

## enfwnddp anjfh wjwkdgkfrjsi head == loacl gkrrydptj tnwjdgksrj 
## ==>> dkfoqnqnsdms wlqdptj tnwjdgks qnqns
#<<<<<<< HEAD
## rltgjqmdp dhffuTejs sodyd
# 수정 예시
#if __name__ == "__main__":
#    print("hello python, hi ros.")
#    print("Python is the best language for ros")
#=======


# main.py
import list_ops as lo
import dict_ops as do

if __name__ == "__main__":
    foo = [1,2,3]
    bar = [4,5,6]
    print(f"foo: {foo}, bar: {bar}")
    print("foo+bar=", lo.add(foo, bar))
    print("foo-bar=", lo.subtract(foo, bar))
    print("foo*bar=", lo.multiply(foo, bar))
    print("foo/bar=", lo.divide(foo, bar))
    
    foo = {"Java": 79, "Cpp": 45, "Python": 99}
    bar = {"Java": 36, "Python": 56, "Ruby": 63}
    print(f"foo: {foo}, bar: {bar}")
    print("foo+bar=", do.add(foo, bar))
    print("foo-bar=", do.subtract(foo, bar))
    print("foo*bar=", do.multiply(foo, bar))
    print("foo/bar=", do.divide(foo, bar))
