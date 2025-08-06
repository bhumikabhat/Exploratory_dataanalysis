# Titanic Dataset - Exploratory Data Analysis (EDA)

This project performs **Exploratory Data Analysis (EDA)** on the Titanic dataset to understand patterns, relationships, and anomalies in the data using statistical summaries and visualizations.

---

## 📊 Objective

Understand the Titanic dataset using descriptive statistics and visual tools to gain insights into passenger survival rates, feature distributions, and relationships.

---

## 🛠️ Tools Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Plotly (for interactive visuals)

---

## 📁 Dataset

- `Titanic-Dataset.csv`
- Typical features include: `PassengerId`, `Survived`, `Pclass`, `Name`, `Sex`, `Age`, `Fare`, `Embarked`, etc.

---

## 📈 EDA Tasks Performed

1. **Summary Statistics**
   - Mean, median, standard deviation, and count of each feature.
   - Missing value detection.

2. **Univariate Analysis**
   - Histograms for numeric features to explore distributions.
   - Boxplots to detect outliers.

3. **Bivariate Analysis**
   - Boxplots of features like `Age`, `Fare` vs `Survived`.
   - Correlation matrix and heatmap.

4. **Multivariate Analysis**
   - Pairplot of selected features (`Survived`, `Pclass`, `Age`, `Fare`) for pattern recognition.
   - Plotly scatter plot (`Age` vs `Fare`) colored by survival status.

---

## 📦 How to Run

1. Clone this repository or download the files.
2. Ensure you have the required libraries
   ```bash
   pip install pandas matplotlib seaborn plotly
