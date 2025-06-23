import pandas as pd

# data = [1,2,3,4,5]
# series = pd.Series(data)
# print(series)


# data = {
#     'name' : ['alice', 'bob','roma','anna'],
#     'age' : [23,45,17,24],
#     'city' : ['new york','la','chicago','moscow']
# }
#
# df = pd.DataFrame(data)
# print(df)


df = pd.read_csv('World-happiness-report-2024.csv')
print(df.loc[56])