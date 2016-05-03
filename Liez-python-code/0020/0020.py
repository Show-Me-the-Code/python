import xlrd
import re
from pylab import *


def get_xls_data(filename):

     # 读取xls数据
     book = xlrd.open_workbook(filename)
     sheet = book.sheet_by_index(0)
     content = {}
     for i in range(sheet.nrows):
         content[i+1] = sheet.row_values(i)[1:]
         #print(content[i+1])

     print("Liez的3月话费单：")

     # 统计话费
     cost = 0
     for i in range(sheet.nrows-1):
         cost += float(content[i+2][7])
     print("通话费:", round(cost, 2),"元")

     # 统计被叫主叫次数
     call = 0
     becall = 0
     for i in range(sheet.nrows-1):
         if(content[i+2][3] == "主叫"):
             call += 1
         else:
             becall += 1
     total = call + becall
     print("主叫",call,"次，被叫",becall,"次，共计",total,"次通话")

     # 统计通话时间
     time = {}
     for i in range(sheet.nrows-1):
         time[i] = content[i+2][1]
     day = {}
     for i in range(31):
        day[i+1] = 0
     rday = re.compile('-(\d+?) ')
     for i in range(sheet.nrows-1):
        daycompile = rday.findall(content[i+2][1])
        t = int(daycompile[0])
        day[t] += 1
     daytimes = (list(day.values()))
     dates = (list(day.keys()))

     # 统计通话时长
     sec = 0
     min = 0
     for i in range(sheet.nrows-1):
          rsec = re.compile('(\d+)秒')
          rmin = re.compile('(\d+)分')
          seci = rsec.findall(content[i+2][2])
          mini = rmin.findall(content[i+2][2])
          sec += int(seci[0])
          if(len(mini)==1):
               min += int(mini[0])
     if(sec >= 60):
         t = sec / 60
         sec = sec % 60
         min = min + t
     print("通话时长:%d分%d秒"%(min,sec))

     #三月日通话次数统计图
     plt.plot(dates, daytimes)
     grid(True)
     title("Call Times Every Day")
     plt.show()

     #根据被叫主叫次数作饼状图
     figure(2, figsize=(6,6))
     fracs = [call/total, becall/total]   # 饼状图按被叫和主叫分成两部分的比例
     labels = 'Call', 'Becall'
     pie(fracs, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors = ("b", "y"))
     title("Call & Becall")
     show()


get_xls_data("comu.xls")
