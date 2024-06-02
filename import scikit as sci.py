# Import the necessary module from scikit-learn
from sklearn.linear_model import LinearRegression

# Sample data
data = {
    'Name': ['NICK', 'Emmaphill', 'Lana', 'Olivia', 'simon'],
    'Marks': [80, 95, 74, 92, 70],
    'CGPA': [8.9, 8.0, 8.7, 9.4, 8.8],
    'Percentage': [88.0, 91.0, 77.0, 92.0, 80.0]
}
df=sci.Dataframe(data)
x=df[["CGPA", "Marks"]]
y=df["percentage"]


# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(x, y)

# Make predictions
predictions = model.predict([[3.7], [87]])

# Print the predictions
print(predictions)
