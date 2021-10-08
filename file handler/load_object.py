import pickle
from person import Person

with open('object.bin', 'rb') as f:
    data = pickle.load(f)
print(data)

with open('object.bin', 'rb') as f:
    data = pickle.load(f)
    for d in data:
        print(d)
