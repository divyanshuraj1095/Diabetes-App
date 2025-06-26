# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
loaded_model = pickle.load(open('E:/ML-DL projects/Deploying model/trained_model.sav', 'rb'))
loaded_scalar = pickle.load(open('E:/ML-DL projects/Deploying model/scalar.sav', 'rb'))

#scalar = StandardScaler()

input_data = (1,85,66,29,0,26.6,0.351,31)

#changing to numpy array

input_data_as_numpy = np.asarray(input_data)

#reshape the array as we are predicting the one instance

input_data_reshaped = input_data_as_numpy.reshape(1,-1)

# standarize the input data
std_data = loaded_scalar.transform(input_data_reshaped)
# print(std_data)

prediction = loaded_model.predict(std_data)#the output we get from the classifier is a list not an integer
print(prediction)

if(prediction[0] == 0): ## we are taking the first value of the list (prediction[0])
    print("The person is non-diabetic !")

else :
    print("The person is diabetic !")

