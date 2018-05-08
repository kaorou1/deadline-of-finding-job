import get_time
import datetime

# print(time.time())
#
# nowTime = time.localtime(time.time())
# print(nowTime)
def get_dead_line():
    nowTime = datetime.datetime.now()

    workTime = datetime.datetime(2019, 7, 1, 0, 00, 00,)

    deadLine = workTime - nowTime
    #print(deadLine)
    return str(deadLine)
