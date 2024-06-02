import pandas as pd

# Step 1: Data Collection
data = {
    'Name': ['NICK', 'Emmaphill', 'Lana', 'Olivia', 'simon'],
    'Marks': [80, 95, 74, 92, 70],
    'CGPA': [8.9, 8.0, 8.7, 9.4, 8.8],
    'Percentage': [88.0, 91.0, 77.0, 92.0, 80.0]
}

students_df = pd.DataFrame(data)

# Step 2: Data Preprocessing (No preprocessing required in this example)

# Step 3: Exploratory Data Analysis
# Summary statistics
print("Summary Statistics:")
print(students_df.describe())

# Data Visualization (example: histogram of Marks)
import matplotlib.pyplot as plt
plt.hist(students_df['Marks'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()
from sklearn.linear_model import LinearRegression

# Sample data
data = {
    'Name': ['NICK', 'Emmaphill', 'Lana', 'Olivia', 'simon'],
    'Marks': [80, 95, 74, 92, 70],
    'CGPA': [8.9, 8.0, 8.7, 9.4, 8.8],
    'Percentage': [88.0, 91.0, 77.0, 92.0, 80.0]
}
df=pd.DataFrame(data)
x=df[["CGPA","Marks"]]
y=df["percentage"]

# Create a linear regression model
model = LinearRegression()
# Fit the model to the data
model.fit(x, y)

# Make predictions
predictions = model.predict([[3.7], [87]])

# Print the predictions
print(predictions)


