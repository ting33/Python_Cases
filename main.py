# https://www.cnblogs.com/wanghuixi/p/11345438.html
#https://blog.csdn.net/u013205877/article/details/77542837


#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
total=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if((i!=j)&(j!=k)&(i!=k)):
                print(i,j,k)
                total+=1
print(total)



#如何反向迭代一个序列，如果是一个list,最快的方法使用reverse
tempList = [1,2,3,4]
tempList.reverse()
for x in tempList:
    print x
#如果是元组需要手动遍历
tempList=(1,2,3,4)
for i in range(len(tempList)-1,-1,-1):
    print(tempList[i])


#替换文本中的串，除了replace，还可以使用正则,有个sub()
tempstr = "hello you hello python are you ok"
import re
rex = r'(hello|Use)'
print(re.sub(rex,"Bye",tempstr))

# list 对象 alist [{“name”:”a”,”age”:20},{“name”:”b”,”age”:30},{“name”:”c”,”age”:25}]按照 age 从大到小排序
alist = [{"name":"a","age":20},{"name":"b","age":30},{"name":"c","age":25}]
alist.sort(key=lambda x:-x['age'])#sort改变本身，且只对list
test=sorted(alist,key=lambda x:x['age'],reverse=True)    #sorted对所有对象都可以，不会改变本省,reverse表示升序还是降序，默认是升序,true为降序
print(test)
print(alist)
#https://www.cnblogs.com/wjw2018/p/10613242.html

#确定字符串是否包含唯一字符,包含返回true
s='1223'
print(not len(set(s))==len(s))

# 实现一个算法来实现反转字符数组的功能。反转的要求如下：
# 将字符数组的字符进行反转，例如 ['b', ' ', 'a', 'r'] 变成 ['r', 'a', ' ', 'b']