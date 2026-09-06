import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Convert TotalCharges column to numeric numbers (turns blank spaces into NaN)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Fill missing NaN values in TotalCharges with MonthlyCharges
df['TotalCharges'] = df['TotalCharges'].fillna(df['MonthlyCharges'])

# Print confirmation
print("Missing values in dataset:")
print(df.isnull().sum()[df.isnull().sum() > 0])
print("\nDataset dimensions (rows, columns):", df.shape)

# Calculate overall churn rate
churn_rate = (df['Churn'] == 'Yes').mean() * 100

print(f"Overall Churn Rate: {churn_rate:.2f}%")

# Calculate churn rate grouped by Contract type
contract_churn = df.groupby('Contract')['Churn'].apply(lambda x: (x == 'Yes').mean() * 100)

print("\n--- Churn Rate by Contract Type ---")
print(contract_churn.round(2))

# Create tenure range bins
bins = [0, 12, 24, 48, 72]
labels = ['0-1 year', '1-2 years', '2-4 years', '4-6 years']

df['Tenure_Group'] = pd.cut(df['tenure'], bins=bins, labels=labels, include_lowest=True)

# Calculate churn rate per tenure group
tenure_churn = df.groupby('Tenure_Group')['Churn'].apply(lambda x: (x == 'Yes').mean() * 100)

print("\n--- Churn Rate by Tenure Group ---")
print(tenure_churn.round(2))

# Create monthly charge price tiers
charge_bins = [0, 35, 60, 90, 120]
charge_labels = ['Low ($0-$35)', 'Medium ($35-$60)', 'High ($60-$90)', 'Very High ($90+)']

df['Charge_Tier'] = pd.cut(df['MonthlyCharges'], bins=charge_bins, labels=charge_labels)

# Calculate churn rate per charge tier
charge_churn = df.groupby('Charge_Tier')['Churn'].apply(lambda x: (x == 'Yes').mean() * 100)

print("\n--- Churn Rate by Monthly Charge Tier ---")
print(charge_churn.round(2))

import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))

# Create bar plot for Churn Rate by Contract Type
ax = sns.barplot(
    x=contract_churn.index, 
    y=contract_churn.values, 
    palette="Blues_d"
)

# Add titles and labels
plt.title("Churn Rate by Contract Type", fontsize=14, fontweight='bold')
plt.xlabel("Contract Type", fontsize=12)
plt.ylabel("Churn Rate (%)", fontsize=12)
plt.ylim(0, 50)

# Annotate bars with exact percentage values
for p in ax.patches:
    ax.annotate(f'{p.get_height():.2f}%', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='bottom', fontsize=11, xytext=(0, 3), 
                textcoords='offset points')

plt.tight_layout()
plt.show()

# Create bar plot for Churn Rate by Tenure Group
plt.figure(figsize=(8, 5))
ax2 = sns.barplot(
    x=tenure_churn.index, 
    y=tenure_churn.values, 
    palette="Oranges_d"
)

plt.title("Churn Rate by Tenure Group", fontsize=14, fontweight='bold')
plt.xlabel("Tenure Range", fontsize=12)
plt.ylabel("Churn Rate (%)", fontsize=12)
plt.ylim(0, 60)

for p in ax2.patches:
    ax2.annotate(f'{p.get_height():.2f}%', 
                 (p.get_x() + p.get_width() / 2., p.get_height()), 
                 ha='center', va='bottom', fontsize=11, xytext=(0, 3), 
                 textcoords='offset points')

plt.tight_layout()
plt.show()

# Create bar plot for Churn Rate by Monthly Charge Tier
plt.figure(figsize=(8, 5))
ax3 = sns.barplot(
    x=charge_churn.index, 
    y=charge_churn.values, 
    palette="Reds_d"
)

plt.title("Churn Rate by Monthly Charge Tier", fontsize=14, fontweight='bold')
plt.xlabel("Monthly Charge Tier", fontsize=12)
plt.ylabel("Churn Rate (%)", fontsize=12)
plt.ylim(0, 45)

for p in ax3.patches:
    ax3.annotate(f'{p.get_height():.2f}%', 
                 (p.get_x() + p.get_width() / 2., p.get_height()), 
                 ha='center', va='bottom', fontsize=11, xytext=(0, 3), 
                 textcoords='offset points')

plt.tight_layout()
plt.show()