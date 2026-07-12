import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

df = pd.read_csv("diamond_data.csv")
# print(df.head(5))

x = df[["Rough_Weight_ct","Shape","Length_mm","Width_mm","Height_mm","Color","Clarity","Crack_Level","Cut_Type"]]
y = df["Final_Weight_ct"]

categorical_features=[
    "Shape","Color","Clarity","Crack_Level","Cut_Type"
]

numerical_features=[
    "Rough_Weight_ct","Length_mm","Width_mm","Height_mm"
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "num",
            "passthrough",
            numerical_features
        )
    ]
)

model = RandomForestRegressor(
    n_estimators=300,
    random_state=42,
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    n_jobs=-1
)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", model)
])

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

pipeline.fit(x_train,y_train)

y_pred = pipeline.predict(x_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("=" * 40)
print("Random Forest Regression Results")
print("=" * 40)

print(f"MAE  : {mae:.4f}")
print(f"MSE  : {mse:.4f}")
print(f"RMSE : {rmse:.4f}")
print(f"R² Score : {r2:.4f}")

# ==========================
# Save Model
# ==========================
# joblib.dump(pipeline, "diamond_weight_model.joblib")

# print("\nModel saved as diamond_weight_model.joblib")