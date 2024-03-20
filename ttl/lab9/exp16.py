import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("people_dataset.csv")

# Split the data into features (age) and target (IQ)
X = df['Age'].values.reshape(-1, 1) 
y = df['IQ'].values 

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define the neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
history = model.fit(X_train_scaled, y_train, epochs=100, batch_size=32, validation_split=0.2)

# Evaluate the model
loss = model.evaluate(X_test_scaled, y_test)
print("Test Loss:", loss)

# Save the model
model.save("iq_prediction_model.keras")

# Load the model
loaded_model = tf.keras.models.load_model("iq_prediction_model.keras")
# Compile the loaded model with appropriate loss and metrics
loaded_model.compile(loss='mean_squared_error', optimizer='adam')

# Evaluate the performance of the loaded model
test_loss = loaded_model.evaluate(X_test_scaled, y_test)
print("Test Loss:", test_loss)

loaded_model.summary()


