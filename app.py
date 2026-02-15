import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Argus IA", layout="wide")

@st.cache_resource
def load_assets():
    model = joblib.load('models/car_price_model.pkl')
    columns = joblib.load('models/model_columns.pkl')
    return model, columns

try:
    model, model_columns = load_assets()
except:
    st.stop()

st.title("Estimateur de Prix Automobile")

col1, col2, col3 = st.columns(3)

with col1:
    hp = st.number_input("Horsepower", min_value=40, max_value=500, value=110)
    engine_size = st.number_input("Engine Size", min_value=50, max_value=300, value=120)
    rpm = st.slider("Peak RPM", 4000, 7500, 5000)

with col2:
    weight = st.number_input("Curb Weight", value=2500)
    length = st.number_input("Car Length", value=170.0)
    wheelbase = st.number_input("Wheelbase", value=95.0)

with col3:
    city_mpg = st.slider("City MPG", 10, 60, 25)
    fuel = st.selectbox("Fuel Type", ["Gas", "Diesel"])
    body = st.selectbox("Car Body", ["Sedan", "Hatchback", "Convertible", "Wagon", "Hardtop"])

def prepare_input_data():
    input_dict = {col: [0] for col in model_columns}
    df = pd.DataFrame(input_dict)

    df['horsepower'] = hp
    df['enginesize'] = engine_size
    df['curbweight'] = weight
    df['carlength'] = length
    df['wheelbase'] = wheelbase
    df['peakrpm'] = rpm
    df['citympg'] = city_mpg

    fuel_col = f"fueltype_{fuel.lower()}"
    if fuel_col in df.columns:
        df[fuel_col] = 1

    body_col = f"carbody_{body.lower()}"
    if body_col in df.columns:
        df[body_col] = 1

    return df[model_columns]

if st.button("Calculer", use_container_width=True):
    final_input = prepare_input_data()
    prediction_raw = model.predict(final_input)[0]
    
    coeff = 3.5
    prediction_tn = prediction_raw * coeff

    st.metric(label="Prix Estimé (DT)", value=f"{prediction_tn:,.2f}")
    st.write(f"Prix d'origine : ${prediction_raw:,.2f}")