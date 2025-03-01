import pandas as pd
import numpy as np
import keras
from keras import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df= pd.read_csv(r'C:\Users\allwe\Downloads\concrete_data.csv')
df.describe()

## Regression Using Keras

#seperate the target variable from the predicted variable
y= df.iloc[:,8].values
x=df.drop(['Strength'],axis=1)
x
y

# Initialize an empty list to store the MSE values
mse_list = []

# Define the model function (with input_shape as a parameter)
def kerasmod(input_shape):
    model = Sequential()
    model.add(Dense(10, activation='relu', input_shape=(input_shape,)))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(1))
    
    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Loop to repeat the process 50 times
for i in range(50):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=i, test_size=0.3)

    # Get input shape from training data
    input_s = X_train.shape[1]

    # Create the model
    model = kerasmod(input_s)  # Pass input_s to the kerasmod function

    # Train the model
    model.fit(X_train, y_train, epochs=50, verbose=0)

    # Make predictions
    ypreds = model.predict(X_test)

    # Calculate mean squared error
    mse = mean_squared_error(y_test, ypreds)

    # Append the MSE to the list
    mse_list.append(mse)

# Calculation of the mean and standard deviation of the MSE list
mean_mse = np.mean(mse_list)
std_mse = np.std(mse_list)

# Report the results
print(f"Mean of MSE: {mean_mse}")
print(f"Standard Deviation of MSE: {std_mse}")
