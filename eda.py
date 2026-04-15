import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Style for better visuals
sns.set(style="whitegrid")

# =========================
# LOAD DATA (PUT HERE)
# =========================
df = pd.read_csv("Walmart.csv")

print("First 5 rows:\n", df.head())
print("\nDataset Info:\n")
print(df.info())
print("\nMissing Values:\n", df.isnull().sum())

# Remove missing values
df = df.dropna()

print("\nStatistical Summary:\n", df.describe())

# =========================
# 1. Total Sales by Store
# =========================
store_sales = df.groupby("Store")["Weekly_Sales"].sum()
print("\nStore Sales:\n", store_sales)

plt.figure()
store_sales.plot(kind="bar")
plt.title("Total Sales by Store")
plt.xlabel("Store")
plt.ylabel("Weekly Sales")
plt.tight_layout()
plt.show()

# =========================
# 2. Monthly Sales Trend
# =========================
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year

monthly_sales = df.groupby("Month")["Weekly_Sales"].sum()
print("\nMonthly Sales:\n", monthly_sales)

plt.figure()
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Weekly Sales")
plt.tight_layout()
plt.show()

# =========================
# 3. Yearly Sales
# =========================
yearly_sales = df.groupby("Year")["Weekly_Sales"].sum()
print("\nYearly Sales:\n", yearly_sales)

plt.figure()
yearly_sales.plot(kind="bar")
plt.title("Yearly Sales")
plt.xlabel("Year")
plt.ylabel("Weekly Sales")
plt.tight_layout()
plt.show()

# =========================
# 4. Holiday vs Non-Holiday
# =========================
holiday_sales = df.groupby("Holiday_Flag")["Weekly_Sales"].mean()
print("\nHoliday Sales:\n", holiday_sales)

plt.figure()
holiday_sales.plot(kind="bar")
plt.title("Holiday vs Non-Holiday Sales")
plt.xlabel("Holiday Flag (0 = No, 1 = Yes)")
plt.ylabel("Average Weekly Sales")
plt.tight_layout()
plt.show()

# =========================
# 5. Scatter Plots
# =========================
plt.figure()
sns.scatterplot(x="Temperature", y="Weekly_Sales", data=df)
plt.title("Temperature vs Weekly Sales")
plt.show()

plt.figure()
sns.scatterplot(x="Fuel_Price", y="Weekly_Sales", data=df)
plt.title("Fuel Price vs Weekly Sales")
plt.show()

plt.figure()
sns.scatterplot(x="Unemployment", y="Weekly_Sales", data=df)
plt.title("Unemployment vs Weekly Sales")
plt.show()

print("\n✅ ALL GRAPHS COMPLETED")