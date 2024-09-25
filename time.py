import time
import random
import datetime

# print(time.time()) # выводит время с начала эпохи (01.01.1970) (текущая дата в миллисекундах)
# seconds = time.time()
# print(time.ctime(seconds)) # (текущая дата в датах)
# # time.sleep(n) - задержка работы программы на n секунд
# # for i in range(5):
# #     print(i)
# #     time.sleep(1)
# print(time.asctime()) # текущая дата (работает также как ctime)
# print(time.localtime(seconds)) # текущее время, разбитое на аргументы
# year = time.localtime(seconds).tm_year
# print(year)
# print(time.strftime('%m/%d/%Y, %H:%M:%S')) # дата в необходимом формате

# time.sleep(5)
# print('Готово')

# for i in range(10):
#     print(time.asctime())
#     time.sleep(1)

# print(time.strftime('%Y-%m-%d %H:%M:%S'))


# time.sleep(random.randint(1, 10))
# print('Готово')

date1 = datetime.datetime(2024, 9, 11)
date2 = datetime.datetime(2023, 3, 25)
print(date1)
print(date2)
print(date1 - date2)
t = datetime.datetime.now() - date2
print(t.days)