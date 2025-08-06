import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load dataset
df = pd.read_csv('Titanic-Dataset.csv')  # Change path if needed

# 1. Summary Statistics
print("=== Summary Statistics ===")
print(df.describe(include='all'))

# Check for missing values
print("\n=== Missing Values ===")
print(df.isnull().sum())

# 2. Histograms for Numeric Features
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[numeric_cols].hist(figsize=(12, 8), bins=20)
plt.suptitle('Histograms of Numeric Features')
plt.tight_layout()
plt.show()

# 3. Boxplots for Numeric Features vs Survived (if 'Survived' exists)
if 'Survived' in df.columns:
    for col in numeric_cols:
        if col != 'Survived':
            plt.figure(figsize=(6, 4))
            sns.boxplot(data=df, x='Survived', y=col)
            plt.title(f'Boxplot of {col} by Survived')
            plt.show()

# 4. Correlation Matrix and Heatmap
plt.figure(figsize=(10, 6))
corr_matrix = df.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
plt.show()

# 5. Pairplot for Selected Features
selected_features = ['Survived', 'Pclass', 'Age', 'Fare']
df_selected = df[selected_features].dropna()
sns.pairplot(df_selected, hue='Survived')
plt.suptitle('Pairplot of Selected Features', y=1.02)
plt.show()

# 6. Optional: Plotly Interactive Visualization
if 'Age' in df.columns and 'Fare' in df.columns and 'Survived' in df.columns:
    fig = px.scatter(df, x='Age', y='Fare', color='Survived', 
                     title='Age vs Fare (Colored by Survival)',
                     hover_data=['Pclass', 'Sex'])
    fig.show()
