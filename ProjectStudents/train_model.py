import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder

stud_data = pd.read_csv('StudentsPerformance.csv')

stud_data.head()

stud_data['average_score'] = stud_data[['math score', 'reading score', 'writing score']].mean(axis=1)

# Coding data

label_encoder = LabelEncoder()
stud_data.rename(columns={'parental level of education' : 'Par_education'}, inplace=True)

stud_data.head()
stud_data['Par_education'] = label_encoder.fit_transform(stud_data['Par_education'])

df_encoded = pd.get_dummies(stud_data, columns=['gender', 'race/ethnicity', 'lunch', 'test preparation course'], drop_first=True, dtype=int)
# Standarizing data
scaler = StandardScaler()
features_for_scaler = df_encoded[['math score', 'reading score', 'writing score']]

scaled_features = scaler.fit_transform(features_for_scaler)
df_scaled = pd.DataFrame(scaled_features, columns=features_for_scaler.columns)
df_scaled = df_scaled.add_suffix('_scaled')
df_encoded_scaled = df_encoded.join(df_scaled)
df_encoded_scaled = df_encoded_scaled.drop(columns=['math score', 'reading score', 'writing score'])

# Training model

X = df_encoded_scaled.drop(columns=['average_score'], axis=1)
y = stud_data['average_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

model = RandomForestRegressor(n_estimators=100, random_state=2)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'MSE:, {mse:.3f}')
print(f'R2:, {r2:.3f}')

# scores = cross_val_score(model, X, y, cv=5, scoring='r2')
# print(scores)

# plt.figure(figsize=(10, 6))
# plt.scatter(y_test, y_pred)
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='black')
# plt.grid(True)
# plt.show()

# Predicting test data

input_data = [[0.000000,0.000000,1.000000,0.000000,0.000000,0.000000,1.000000,1.000000,0.324041,0.947790,0.654857]]

input_df = pd.DataFrame(input_data, columns=X.columns)

predicted_score = model.predict(input_df)
print(f'Expected average rating: {predicted_score[0]:.2f}')