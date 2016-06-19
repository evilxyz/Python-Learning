#!/usr/bin/env python
#coding=utf-8

L = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 'name', 'sex', 'age']        #列表内可放任意类型的数据

L0 = ['x', 'y', 'z']



print ('合并操作(L+L0) ===> \t' + str(L+L0))                    #合并操作


print ('重复操作(L0 * 3) ===> \t' + str(L0 * 3))                # 重复3次


for x in L: print ('迭代输出' + str(x))                         #迭代, 依次输出list中的元素


print ('成员关系(\'name\' in L) ===> \t' + str('name' in L))    #检测'name'在L中是否存在, 返回逻辑型


L.append('new guy !')                                      #在列表末尾添加一个新元素
print ('添加元素(L.append(\'new guy !\') ===> \t' + str(L))

L.extend(['pig0', 'pig1', 'pig2'])                              #在列表末尾批量添加多个元素, same as  L[len(L):] = ['pig', 'dog']
print ('批量在列表末尾添加元素(L.extend([\'pig0\', \'pig1\', \'pig2\']) ===> \t ' + str(L))


L.insert(10, 'insert test')
print ('任意位置插入元素(L.insert(10, \'insert test\') ===> \t ' + str(L)) #在列表指定位置添加元素


print ('索引操作(L.index(\'name\') ===> \t' + str(L.index('name')))  #索引, 查找'name'的偏移位置


print ('统计出现次数(L.count(6)) ===> \t' + str(L.count(6)))            #统计, 统计6出现的次数

L.pop()                                                                 #出栈,后列表末端删除一个元素
print ('删除元素(L.pop()) ===> \t' + str(L))

L.remove('name')                                                        #删除指定元素
print ('删除元素(L.remove(\'name\') ===> \t' + str(L))


del L[L.index(6)]                                                       #删除语句, 根据索引删除元素
print ('删除元素(L.index(6)) ===> \t' + str(L))


del L[L.index('insert test'):]                                           #批量删除, 原型是del L[i:j]
print ('批量删除(del L[L.index(\'insert test\'):]) ===> \t' + str(L))


L.sort(key=None, reverse=True)
print ('逆序排序(L.sort(key=None, reverse=True)) ===> \t' + str(L))
#排序, 因为列表内包含字符串,故返回错误.(但如果在交互模式下, 是会排序前面数字部分)


L[len(L):] = ['a', 'b', 'c', 'd']                                           #在末尾插入多个数据,和extend作用相同,但extend要好
print (L)


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print ("矩阵 ==> " + str(matrix))

print ("连续整数 ==> " + str(list(range(-4, 4))))
