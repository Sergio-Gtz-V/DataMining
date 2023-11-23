import os
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt


df = pd.read_csv('cleaned_database.csv')
output_dir = 'img/graphs'
#Determinar si el equipo local ganó
df['HOME_ADVANTAGE'] = df['PTS_home'] - df['PTS_away']
df['HOME_TEAM_WINS'] = (df['HOME_ADVANTAGE'] > 0).astype(int)

# Datos para la regresión
X = sm.add_constant(df[['HOME_TEAM_WINS']])  # Independent variable
y = df['HOME_ADVANTAGE']  # Dependent variable
model = sm.OLS(y, X).fit()

print(model.summary())
# Plot
plt.figure(figsize=(8, 6))
plt.scatter(df['HOME_TEAM_WINS'], df['HOME_ADVANTAGE'], alpha=0.3)
plt.plot(df['HOME_TEAM_WINS'], model.predict(X), color='red', linewidth=2)
plt.title('Linear Regression: Home Team Advantage')
plt.xlabel('Home Team Wins (1 if yes, 0 if no)')
plt.ylabel('Home Advantage (Points)')
plt.savefig(os.path.join(output_dir, 'LinearRegression'))
plt.show()

"""
OLS Regression Results
==============================================================================
Dep. Variable:         HOME_ADVANTAGE   R-squared:                       0.640
Model:                            OLS   Adj. R-squared:                  0.640
Method:                 Least Squares   F-statistic:                 4.258e+04
Date:                Mon, 20 Nov 2023   Prob (F-statistic):               0.00
Time:                        13:57:26   Log-Likelihood:                -84182.
No. Observations:               23904   AIC:                         1.684e+05
Df Residuals:                   23902   BIC:                         1.684e+05
Df Model:                           1
Covariance Type:            nonrobust
==================================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------
const            -10.2783      0.082   -124.779      0.000     -10.440     -10.117
HOME_TEAM_WINS    22.1929      0.108    206.342      0.000      21.982      22.404
==============================================================================
Omnibus:                     1525.006   Durbin-Watson:                   1.997
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             4404.807
Skew:                           0.334   Prob(JB):                         0.00
Kurtosis:                       4.994   Cond. No.                         2.87
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified."""

# Create a new column for winning percentage
df['WINNING_PERCENTAGE'] = df['HOME_TEAM_WINS']

# Select relevant features for the model
features = ['PTS_home', 'PTS_away', 'FG_PCT_home', 'FT_PCT_home']

# Prepare the data for linear regression
X = sm.add_constant(df[features])  # Independent variables
y = df['WINNING_PERCENTAGE']  # Dependent variable

# Fit the linear regression model
model = sm.OLS(y, X).fit()

# Print regression summary
print(model.summary())
print(model.params)