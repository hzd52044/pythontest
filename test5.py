'''
输入三个整数x,y,z，请把这三个数由小到大输出。

我们想办法把最小的数放到x上，先将x与y进行比较，
如果x>y则将x与y的值进行交换，然后再用x与z进行比较，
如果x>z则将x与z的值进行交换，这样能使x最小。
'''

l = []
for i in range(3):
    x = int(input('integer:\n'))
    l.append(x) #在数组末尾添加新的对象
l.sort()    #对原列表进行排序 
print(l)

