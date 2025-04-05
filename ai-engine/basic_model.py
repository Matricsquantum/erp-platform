# Basic AI model for SynapseCore ERP
import numpy as np
from sklearn.linear_model import LinearRegression

# Mock training data
X = np.array([[1], [2], [3], [4]]).reshape(-1, 1)  # Past months
y = np.array([1000, 1200, 1500, 1800])  # Past revenues

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict next month
next_month = np.array([[5]]).reshape(-1, 1)
prediction = model.predict(next_month)[0]
print(f"Predicted Revenue for Month 5: ${prediction:.2f}")

# Save for API use
import joblib
joblib.dump(model, 'ai-engine/model.pkl')
