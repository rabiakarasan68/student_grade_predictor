import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

X = data[["vize", "katilim"]]
y = data["final"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

lr = LinearRegression()
lr.fit(X_train, y_train) # Model eğitilir
lr_pred = lr.predict(X_test) 
lr_error = mean_absolute_error(y_test, lr_pred)

rf = RandomForestRegressor()
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_error = mean_absolute_error(y_test, rf_pred)

print("Linear Regression Hata: ", lr_error)
print("Random Forest Hata: ", rf_error)

if lr_error < rf_error:
    best_model = lr
    print("En iyi model: Linear Regression")
else:
    best_model = rf
    print("En iyi model: Random Forest")

joblib.dump(best_model, "model.pkl")

print("Model eğitildi ve kaydedildi!")

best_pred = best_model.predict(X_test)

plt.scatter(y_test, rf_pred, label="Random Forest")
plt.scatter(y_test, lr_pred, label="Linear Regression")
plt.scatter(y_test, best_pred, label="Best model")
plt.xlabel("Gerçek Not")
plt.ylabel("Tahmin")
plt.title("Random Forest Tahmin Performansı")
plt.legend()
plt.show()
