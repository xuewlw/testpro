import random
'''
def inc(x):
    def incx(y):
        return x + y

    return incx


inc2 = inc(2)
inc5 = inc(5)

print(inc2(5))
print(inc5(5))

def char2num(s):
    digits = {'0': 0, '1' : 1,'2':2,'3':3}
    return digits[s]

print(list(map(char2num  ,  '123')))
'''

'''
result = 0
for i in range(101):
    # result += i
    print(i,end = 'a')
print(result)

a=10
b=6
c=a if a>b else b
print(c)
'''

'''
ver = [123,456,789]
print(ver[-1])
'''

'''
photo = ["三星", "小米", "华力"]
len(photo)

photo.append("大小")

print(photo)

value = "大小"

if photo.count(value):
    photo.remove(value)
print(photo)


r = [random.randint(10,100) for i in range(10)]
print(r)
'''
'''
class Geese:
    def __init__(self):
        self.neck = "脖子长"
        print(self.neck)

    def fly(self,state):
        print(state)


goose1 = Geese()
goose2 = Geese()

goose1.neck = "脖子"

print(goose1.neck)
print(goose2.neck)
#wildGoose.fly('123456')
'''

'''
def division():
    apple = int(input("请输入苹果数"))
    children = int(input("请输入人数"))
    if apple < children:
        raise ValueError("苹果太少，不够分的")
    result = apple // children

    remain = apple - result*children

    if remain>0:
        pass

if __name__ == '__main__':
    try:
        division()
    except ZeroDivisionError:
        print("\n不能是0")
    except ValueError as e:
        print("输入错误:",e)
    else:
        print("苹果分完")
    finally:
        print("再分一次")


# 生成器 generator
def fib(max):
    n, a, b =0, 0, 1
    while n<max:
        yield b
        a, b = b, a+b
        n = n+1
    return 'done'


f = fib(6)
'''

def f(x):
    return x*x
print(map(f,[1,2,3]))