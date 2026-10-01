import pandas as pd

# Read tips.csv dataset
df = pd.read_csv("tips.csv")

# Display the first 10 rows
print("--- First 10 Rows of tips.csv ---")
print(df.head(10))
