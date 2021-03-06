import os
import re

import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

if __name__ == '__main__':
    abs_path = os.getcwd()
    # point_json = {}
    # for f_path, dirs, fs in os.walk(abs_path + "\\csv"):
    #     for file in fs:
    #         if file[0] != '.' and os.path.splitext(file)[1] == '.csv':
    #             with open(f_path + "\\" + file, encoding="utf16") as f:
    #                 [next(f) for _ in range(6)]
    #                 data = pd.read_csv(f, sep=';', skiprows=[1], index_col="Time (Note)")
    #                 data = data.replace(["-", "c"], [0, 0])
    #                 data = data.replace('\?', '', regex=True).astype(float)
    #                 result, new_column = {}, []
    #                 [new_column.append(column) for column in data.columns if
    #                  'IA' in column or 'IB' in column or 'IC' in column]
    #                 time_index = [i for i in range(0, 100, 4)]
    #                 for row_name in [new_column[i:i + 3] for i in range(0, len(new_column), 3)]:
    #                     result_array = []
    #                     [result_array.append(
    #                         round((data[row_name].iloc[time_index[index]:time_index[index + 1], 0:3].sum(axis=1) * 380 * 0.85).sum() / 1000, 2))
    #                      for index in range(0, len(time_index)) if index < len(time_index) - 1]
    #                     result[data[row_name].columns.values[0].split(' ')[0]] = result_array
    #
    #                 if file.split("_")[0]+file.split("_")[1] in point_json:
    #                     point_json[file.split("_")[0]+file.split("_")[1]].update(
    #                         {file.split("_")[2]: sum(list(np.array(list(result.values())).flat))})
    #                 else:
    #                     point_json[file.split("_")[0]+file.split("_")[1]] = {}
    #                     point_json[file.split("_")[0]+file.split("_")[1]].update(
    #                         {file.split("_")[2]: sum(list(np.array(list(result.values())).flat))})
    #
    #                 save_path = abs_path + "\\hour_csv\\" + os.path.split(os.path.split(f_path)[0])[1] + "\\" + \
    #                             os.path.split(f_path)[1]
    #                 if not os.path.exists(save_path):
    #                     os.makedirs(save_path)
    #                 pd.DataFrame(result).to_csv(save_path + "\\" + file)
    # with open(abs_path + '\\point_data.json', 'w') as j:
    #     j.write(json.dumps(point_json))


    with open(abs_path + '\\point_data.json', encoding='UTF-8') as load_json:
        point_datas = json.load(load_json)
        fig = plt.figure(num=1, figsize=(60, 20))
        ax = fig.add_subplot(111)
        for point_data in point_datas.items():
            key_list = list(dict(point_data[1]).keys())
            # if str(point_data[0]) == "A1":
            hv_list = key_list[0:int(len(key_list) / 2)]
            lv_list = key_list[int(len(key_list) / 2) + 1:]
            ax.plot([datetime.strptime("".join(re.findall(r"-?[1-9]\d*", d)), '%Y%m%d').date() for d in hv_list], list(dict(point_data[1]).values())[0:int(len(key_list) / 2)], label=str(point_data[0]))
            ax.plot([datetime.strptime("".join(re.findall(r"-?[1-9]\d*", d)), '%Y%m%d').date() for d in lv_list], list(dict(point_data[1]).values())[int(len(key_list) / 2) + 1:], label=str(point_data[0]))
            # else:
            #     t_data = [datetime.strptime("".join(re.findall(r"-?[1-9]\d*", d)), '%Y%m%d').date() for d in key_list]
            #     ax.plot(t_data, list(dict(point_data[1]).values()), label=str(point_data[0]))
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        plt.gcf().autofmt_xdate()
        plt.legend()
        plt.show()
