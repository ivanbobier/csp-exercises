import pickle

mylist = [1, 2, 3, 4]
# the pickle.dumps serializes the array mylist
ser = pickle.dumps(mylist)
print(ser)