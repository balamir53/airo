import pickle
import pandas
with open (r'C:\Users\yusuf\airo\data\groupby-all0.pkl','rb') as file:
    # data = pickle.load(file)
    data = pandas.read_pickle(file)
print(data.tail())