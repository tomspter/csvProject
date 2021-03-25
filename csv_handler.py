import os
import pandas as pd

if __name__ == '__main__':
    abs_path = os.getcwd()
    for f_path, dirs, fs in os.walk('./csv'):
        for file in fs:
            if file[0] != '.' and os.path.splitext(file)[1] == '.csv':
                with open(abs_path + f_path + file, encoding="utf16") as f:
                    [next(f) for _ in range(6)]
                    data = pd.read_csv(f, sep=';', skiprows=[1], index_col="Time (Note)")
                    print(data)
                    print(data.columns)
                    result, new_column = {}, []
                    [new_column.append(column) for column in data.columns if 'IA' in column or 'IB' in column or 'IC' in column]
                    print(new_column)
                    time_index = [i for i in range(0, 100, 4)]
                    for row_name in [new_column[i:i + 3] for i in range(0, len(new_column), 3)]:
                        print(row_name)
                        result_array = []
                        [result_array.append(round(round(data[row_name].iloc[time_index[index]:time_index[index + 1], 0:3].sum(axis=1) * 380 * 0.85,2).sum() / 1000, 2))
                         for index in range(0, len(time_index)) if index < len(time_index) - 1]
                        result[data[row_name].columns.values[0].split(' ')[0]] = result_array
                    pd.DataFrame(result).to_csv(abs_path + "\\hour_csv\\" + month_dir)
