import pandas as pd

# Load NSL-KDD training dataset
train_data = pd.read_csv(
    "data/KDDTrain+.txt",
    header=None
)

# Display dataset information
print("Dataset Shape:")
print(train_data.shape)

print("\nFirst 5 Rows:")
print(train_data.head())