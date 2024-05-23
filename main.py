import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------------
# -             GENERAL DATA PATHS              -
# -----------------------------------------------
file_path = 'data/General_MI/S&P_linear.csv'

# -----------------------------------------------
# -             GENERAL DATA PATHS LEGEND       -
# -----------------------------------------------

with open(file_path, 'r') as file:
    title = file.readline().strip()

# -----------------------------------------------
# -         READ/FORMAT GENERAL CSV's DATA      -
# -----------------------------------------------
df = pd.read_csv(file_path, skiprows=1)
df.columns = df.columns.str.strip()
df = df.dropna(subset=['Date'])

print("Column names:", df.columns)

df['Date'] = pd.to_datetime(df['Date'], format='%m/%Y', errors='coerce')

# -----------------------------------------------
# -             WATCH DATA PATHS              -
# -----------------------------------------------

# ...

# -----------------------------------------------
# -         READ/FORMAT WATCH CSV's DATA      -
# -----------------------------------------------

# ...


# -----------------------------------------------
# -         PLOT DATA                           -
# -----------------------------------------------
plt.figure(figsize=(15, 9))
plt.plot(df['Date'], df['Value'], marker='o', linestyle='-', color='b', label=title)

# Add titles and labels
plt.title('S&P 500 Value Over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()