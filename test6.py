'''
斐波那契数列

又称黄金分割数列，指的是这样一个数列：1、1、2、3、5、8、13、21、34、
'''

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

def fib2(n):
    if n == 1 or n == 2:
        return 1
    return fib2(n-1)+fib(n-2)

def fib3(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1,1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
#根据输入、输出斐波那契数列
def main():
    i = int(input('输出数列的第几位：'))
    #fib(i)
    #print(fib(i))
    #print(fib2(i))
    print(fib3(i))

if __name__ == '__main__':
    main()