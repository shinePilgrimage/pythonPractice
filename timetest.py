import time
import calendar

localtime = time.asctime(time.localtime((time.time())))
print("本地时间为为：", localtime)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%Y %A %B %d %H:%M:%S ", time.localtime()))

cal = calendar.calendar(2022)
print("以下输出2016年1月份的日历:")
print(cal)
