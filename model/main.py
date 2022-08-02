import pickle

# load the model from disk
loaded_model = pickle.load(open("finalized_model.sav", 'rb'))
x=[[1,2]]
p = loaded_model.predict(x)
print(p)