import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load CSV
df = pd.read_csv("sample_data.csv")

# Make sure Month is ordered properly
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
df["Month"] = pd.Categorical(df["Month"], categories=month_order, ordered=True)

# Group by Month & Product
pivot = df.pivot(index="Month", columns="Product", values="Revenue")

# Plot Revenue by Month for each Product
pivot.plot(kind="line", marker="o", figsize=(8,5))
plt.title("Revenue by Month")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.legend(title="Product")
plt.grid(True)
plt.show()


# frame = pd.read_csv("sample_data.csv")

# print(frame.head())

