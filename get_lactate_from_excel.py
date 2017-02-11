
# coding: utf-8

# In[187]:

def get_lactate_from_excel(file_path, sport_type):

    from openpyxl import Workbook
    from openpyxl import load_workbook
    import numpy as np
    import pandas as pd
    from pandas import DataFrame
    from itertools import islice

    wb = load_workbook(filename = file_path)
    
    if sport_type == 'swim': # 选择要读取的运动类型
        ws = wb['游泳']
        switch = False # 根据运动类型来选择升序还是降序排列强度
    elif sport_type == 'bike':
        ws = wb['自行车']
        switch = True # 根据运动类型来选择升序还是降序排列强度
    elif sport_type == 'run':
        ws = wb['跑步']
        switch = False # 根据运动类型来选择升序还是降序排列强度

    data = ws.values
    cols = next(data)[1:]
    data = list(data)
    idx = [r[0] for r in data]
    data = (islice(r, 1, None) for r in data)
    df = DataFrame(data, index=idx, columns=cols)

    df_ascend = df #.sort_values(by='Intensity', ascending=switch) # 按照强度从低到高排序

    df_ascend['Intensity'] = df_ascend['Intensity'].astype('str') # 把强度数据转成字符串
    df_ascend['Lactate'] = df_ascend['Lactate'].astype('float') # 把乳酸数据转成浮点数

    ae_intensity_list = []
    ae_lactate_list = []

    for i, l in zip(df_ascend['Intensity'][:4], df_ascend['Lactate'][:4]): # 取前4组，即有氧测试结果
        #print(i) # Debug
        l = round(l, 1)
        if l != 0.0: # 去掉空值（通常是第四组）
            ae_intensity_list.append(i) # 建立有氧测试强度列表（从低到高）
            ae_lactate_list.append(l) # 建立有氧测试乳酸值列表（对应强度）

    an_intensity_list = []
    an_lactate_list = []

    for i, l in zip(df_ascend['Intensity'][-4:], df_ascend['Lactate'][-4:]): # 取后4组，即无氧测试结果
        l = round(l, 1)
        if i != '0': # 去掉空值（通常是第四组）
            an_intensity_list.append(i) # 建立有氧测试强度列表（从低到高）
            an_lactate_list.append(l) # 建立有氧测试乳酸值列表（对应强度）

    def get_peak_lact_min():
        m = an_lactate_list.index(peak_lactate)
        if m == 0:
            return(3)
        elif m == 1:
            return(5)
        elif m == 2:
            return(7)
        elif m == 3:
            return(20)
    
    an_peak_intensity = max(an_intensity_list)
    peak_lactate = max(an_lactate_list) # 获取无氧测试的乳酸峰值
    peak_lact_min = get_peak_lact_min() # 获取乳酸峰值出现的分钟
    recovery_lact = min(an_lactate_list[-1:]) # 获取恢复20分钟后的乳酸值

    return [ae_lactate_list,#0 有氧乳酸值，浮点数
          ae_intensity_list, #1 有氧强度列表，字符串
          an_peak_intensity, #2 无氧测试强度，字符串
          peak_lactate, #3 无氧峰值乳酸值，浮点数
          peak_lact_min, #4 无氧峰值乳酸出现的分钟数，整数
          recovery_lact #5 恢复20分钟后的乳酸值，浮点数
          ]

    '''
    # 检查数据类型
    print(type(peak_lactate), type(peak_lact_min), type(recovery_lact))        
    for aa, bb in zip(ae_intensity_list, ae_lactate_list):
        print(type(aa), type(bb))
    '''
'''lactate = get_lactate_from_excel('D:/test_dataframe.xlsx', 'run')
print(lactate[4],lactate[3],lactate[2],lactate[5])'''


# In[ ]:



