import os
import pandas as pd

if __name__ == '__main__':
    abs_path = os.getcwd()
    for f_path, dirs, fs in os.walk(abs_path + "\\csv"):
        for file in fs:
            if file[0] != '.' and os.path.splitext(file)[1] == '.csv':
                with open(f_path + "\\" + file, encoding="utf16") as f:
                    [next(f) for _ in range(6)]
                    data = pd.read_csv(f, sep=';', skiprows=[1], index_col="Time (Note)")
                    data = data.replace(["-", "c"], [0, 0])
                    data = data.replace('\?', '', regex=True).astype(float)
                    result, new_column = {}, []
                    [new_column.append(column) for column in data.columns if
                     'IA' in column or 'IB' in column or 'IC' in column]
                    time_index = [i for i in range(0, 100, 4)]
                    for row_name in [new_column[i:i + 3] for i in range(0, len(new_column), 3)]:
                        result_array = []
                        [result_array.append(round(round(
                            data[row_name].iloc[time_index[index]:time_index[index + 1], 0:3].sum(axis=1) * 380 * 0.85,
                            2).sum() / 1000, 2))
                         for index in range(0, len(time_index)) if index < len(time_index) - 1]
                        result[data[row_name].columns.values[0].split(' ')[0]] = result_array
                    save_path = abs_path + "\\hour_csv\\" + os.path.split(os.path.split(f_path)[0])[1] + "\\" +os.path.split(f_path)[1]
                    if not os.path.exists(save_path):
                        os.makedirs(save_path)
                    pd.DataFrame(result).to_csv(save_path + "\\" + file)
