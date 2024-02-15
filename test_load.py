import pickle
with open (r'C:\Users\yusuf\airo\data\combined_data_100.pkl','rb') as file:
    data = pickle.load(file)
print(data.info())