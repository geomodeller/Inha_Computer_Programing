import pickle

with open('fruit_price.pkl', 'rb') as f:
    my_dictionary = pickle.load(f)
    
print(my_dictionary)