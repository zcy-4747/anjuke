# coding=utf-8
import os
import xlwt
import xlrd
file_path = 'C:\\Users\\Administrator\\Desktop\\安居客.xlsx'#要写入的文件
f = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = f.add_sheet('sheet1')
pathDir = os.listdir("C:\\Users\\Administrator\\Desktop\\安居客.txt")#txt文件放置在sub文件夹中，用来获取sub文件夹内所有文件目录
i = 0
for s in pathDir:
    newDir = os.path.join("C:\\Users\\Administrator\\Desktop安居客.txt", s)#把获取的文件路径整合
    f1 = open(newDir, 'r')
    lines = f1.readlines()
    for line in lines:
        sheet.write(i, 0, line)
        i = i+1
print(i)
f.save(file_path)