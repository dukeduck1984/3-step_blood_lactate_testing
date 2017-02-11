
# coding: utf-8

# In[43]:

import re

def pace_convertion(pace, sport_type):
    pace = re.sub(" +", "", pace) # 去掉空格
    if sport_type.lower() == 'run': # 跑步
        paceReg = re.compile(r'(\d+):(\d+):*\d*\w*/*\w*') # 正则表达式过滤字符，去掉单位，只取第一个冒号左右的数值
        pace = paceReg.search(pace)
        minute = pace.group(1)
        second = pace.group(2)
        total_sec = int(minute) * 60 + int(second) # 算成总秒数
        pace = round(1000 / int(total_sec), 2) # m/s
        return pace
    elif sport_type.lower() == 'bike': # 自行车
        paceReg = re.compile(r'(\d+)\w*')
        pace = paceReg.search(pace)
        pace = float(pace.group(1))
        return pace
    elif sport_type.lower() == 'swim': # 游泳
        paceReg = re.compile(r'(\d+):(\d+):*\d*\w*/*\d*\w*') # 正则表达式过滤字符，去掉单位，只取第一个冒号左右的数值
        pace = paceReg.search(pace)
        minute = pace.group(1)
        second = pace.group(2)
        total_sec = int(minute) * 60 + int(second) # 算成总秒数
        pace = round(100 / int(total_sec), 2) # m/s
        return pace

'''
    else:
        #print(str(pace) + " m/s")
        m_per_min = float(pace) * 60
        km_per_min = 1000 / m_per_min
        min2sec = int(km_per_min * 60 % 60)
        #print(str(int(km_per_min)) + ":" + str(min2sec) + " min/km")
        min_per_km = str(int(km_per_min)) + ":" + str(min2sec)
        return min_per_km
'''
#pace_convertion('01:30:10 min/100m')


# In[ ]:



