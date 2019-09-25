
def binary_search(list, item):#list为测试的列表数据，item为测试列表中需要找到的值
    low = 0                 #low 和 high 用于追踪要在其中查找的列表部分
    high = len(list)-1

    while low <= high:          #逐渐缩小到中包含一个元素
        mid = int((low + high)/2)       #每次都取列表中的最大和最小的中间元素
        # mid = (low + high)
        guess = list[mid]           #判断该中间元素在列表中的位置
        if guess == item :          #相等及找到，返回找寻结果
            return mid
        if guess > item:            #中间元素大于目标值，即把中间值变成最大值。继续判断
            high = mid -1
        else:
            low = mid + 1           #中间元素小于目标值，即把中间值设置成最小值。继续判断
    return None                     #全部判断完成，未找到结果，返回None


#测试

my_list = [1,3,5,7,9]
print(binary_search(my_list,3))
print(binary_search(my_list,-8))