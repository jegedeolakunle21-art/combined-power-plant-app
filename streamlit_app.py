
import os
import pickle
from pathlib import Path
from io import BytesIO

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import gdown
import requests
import plotly.express as px

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Industrial Predictive Analytics",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Combined Industrial Predictive Analytics Dashboard")

st.markdown("""
An integrated dashboard for industrial machine learning,
predictive maintenance, energy performance and operational analytics.
""")

# ==========================================
# 2. GOOGLE DRIVE FILE IDENTIFIERS
# ==========================================

DRIVE_MODELS = {
    "Model 1": "1oKzh_Cp9i_TTF92su5fHHv-2x2liIgWN",
    "Model 2": "1OXBgyRWsOUZzpeEIWPYtsqS2HOTjZfnC",
    "Model 3": "1YeRbenb91kgQlbpTiWozMTaf3-mH5U7w",
    "Model 4": "1JivSe0H_nPCp5DOQ_QfXHsIm3e2N782V"
}

GOOGLE_SHEETS = {
    "Dataset 1": "1oJFOtmFxOl_E56XjGVKyS-Rz3JPYdxx8",
    "Dataset 2": "1TA90_OGYHILpLYfoC_M_Th21WvdNjvmg"
}

# ==========================================
# 3. CREATE DATA DIRECTORIES
# ==========================================

DATA_DIR = Path("data")
MODEL_DIR = DATA_DIR / "models"

DATA_DIR.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)

# ==========================================
# 4. DOWNLOAD MODEL FILES FROM GOOGLE DRIVE
# ==========================================

@st.cache_data(show_spinner=False)
def download_model(file_id, filename):

    filepath = MODEL_DIR / filename

    if filepath.exists() and filepath.stat().st_size > 0:
        return str(filepath)

    url = f"https://drive.google.com/uc?id={file_id}"

    result = gdown.download(
        url=url,
        output=str(filepath),
        quiet=False,
        fuzzy=True
    )

    if not result or not filepath.exists() or filepath.stat().st_size == 0:
        raise RuntimeError(
            "Download failed. Check Google Drive sharing permissions."
        )

    return str(filepath)


# ==========================================
# 5. LOAD TRAINED MODELS
# ==========================================

@st.cache_resource(show_spinner=False)
def load_model(filepath):

    try:
        model = joblib.load(filepath)
    except Exception:
        with open(filepath, "rb") as file:
            model = pickle.load(file)

    return model


# ==========================================
# 6. LOAD GOOGLE SHEETS DATA
# ==========================================

@st.cache_data(show_spinner=False)
def load_google_sheet(sheet_id):

    url = (
        f"https://docs.google.com/spreadsheets/d/"
        f"{sheet_id}/export?format=csv"
    )

    response = requests.get(url, timeout=45)
    response.raise_for_status()

    if "text/html" in response.headers.get("content-type", "").lower():
        raise RuntimeError(
            "Google Sheets returned a permission or login page. "
            "Check that the sheet is shared with Anyone with the link."
        )

    if response.text.lstrip().lower().startswith("<html"):
        raise RuntimeError("Google Sheets did not return CSV data.")

    return pd.read_csv(BytesIO(response.content))


# ==========================================
# 7. LOAD ALL FOUR MODELS
# ==========================================

models = {}
model_errors = {}

with st.spinner("Connecting to Google Drive and loading models..."):

    for name, file_id in DRIVE_MODELS.items():

        try:
            filename = name.lower().replace(" ", "_") + ".pkl"

            filepath = download_model(file_id, filename)

            models[name] = load_model(filepath)

        except Exception as error:

            model_errors[name] = str(error)


# ==========================================
# 8. LOAD BOTH DATASETS
# ==========================================

datasets = {}
dataset_errors = {}

with st.spinner("Loading industrial datasets..."):

    for name, sheet_id in GOOGLE_SHEETS.items():

        try:
            datasets[name] = load_google_sheet(sheet_id)

        except Exception as error:

            dataset_errors[name] = str(error)


# ==========================================
# 9. SIDEBAR NAVIGATION
# ==========================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Dashboard",
    [
        "Overview",
        "Dataset Explorer",
        "Model Inspection",
        "Prediction Workbench",
        "System Information"
    ]
)


# ==========================================
# 10. MODEL INSPECTION FUNCTION
# ==========================================

def find_estimators(obj, path="artifact", depth=0):

    found = []

    if depth > 3:
        return found

    if hasattr(obj, "predict"):

        found.append((path, obj))

    elif isinstance(obj, dict):

        for key, value in obj.items():

            found.extend(
                find_estimators(
                    value,
                    f"{path}.{key}",
                    depth + 1
                )
            )

    elif isinstance(obj, (list, tuple)):

        for index, value in enumerate(obj):

            found.extend(
                find_estimators(
                    value,
                    f"{path}[{index}]",
                    depth + 1
                )
            )

    return found


# ==========================================
# 11. OVERVIEW DASHBOARD
# ==========================================

if page == "Overview":

    st.header("Industrial Analytics Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Models Loaded",
        f"{len(models)}/4"
    )

    col2.metric(
        "Datasets Loaded",
        f"{len(datasets)}/2"
    )

    total_rows = sum(
        len(df) for df in datasets.values()
    )

    col3.metric(
        "Total Dataset Records",
        f"{total_rows:,}"
    )

    st.divider()

    st.subheader("Model Connection Status")

    for name in DRIVE_MODELS:

        if name in models:

            st.success(f"{name}: Successfully loaded")

        else:

            st.error(
                f"{name}: {model_errors.get(name, 'Not loaded')}"
            )

    st.subheader("Dataset Connection Status")

    for name in GOOGLE_SHEETS:

        if name in datasets:

            df = datasets[name]

            st.success(
                f"{name}: {len(df)} records, {len(df.columns)} columns"
            )

        else:

            st.error(
                f"{name}: {dataset_errors.get(name, 'Not loaded')}"
            )

    st.info(
        "The model and dataset roles have not yet been identified. "
        "Inspect the artifacts and datasets before assigning operational KPIs."
    )


# ==========================================
# 12. DATASET EXPLORER
# ==========================================

elif page == "Dataset Explorer":

    st.header("Industrial Dataset Explorer")

    if not datasets:

        st.warning("No datasets were loaded.")

    for name, df in datasets.items():

        st.subheader(name)

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", len(df))

        col2.metric("Columns", len(df.columns))

        col3.metric(
            "Missing Values",
            int(df.isnull().sum().sum())
        )

        st.write("Dataset Preview")

        st.dataframe(
            df.head(100),
            use_container_width=True
        )

        st.write("Statistical Summary")

        st.dataframe(
            df.describe().T,
            use_container_width=True
        )

        numeric_columns = df.select_dtypes(
            include=np.number
        ).columns.tolist()

        if numeric_columns:

            selected_column = st.selectbox(
                f"Select variable to visualize: {name}",
                numeric_columns,
                key=name
            )

            fig = px.line(
                df,
                y=selected_column,
                title=f"{selected_column} Trend"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    for name, error in dataset_errors.items():

        st.error(f"{name}: {error}")


# ==========================================
# 13. MODEL INSPECTION
# ==========================================

elif page == "Model Inspection":

    st.header("Machine Learning Model Inspection")

    if not models:

        st.warning("No trained models were loaded.")

    for name, model in models.items():

        with st.expander(name, expanded=True):

            st.write(
                "Model Object Type:",
                type(model).__name__
            )

            if isinstance(model, dict):

                st.write(
                    "Available dictionary keys:",
                    list(model.keys())
                )

            estimators = find_estimators(model)

            st.write(
                "Prediction-capable objects:",
                [item[0] for item in estimators]
            )

            filepath = MODEL_DIR / (
                name.lower().replace(" ", "_") + ".pkl"
            )

            st.write(
                "File size:",
                f"{filepath.stat().st_size:,} bytes"
            )

    for name, error in model_errors.items():

        st.error(f"{name}: {error}")


# ==========================================
# 14. PREDICTION WORKBENCH
# ==========================================

elif page == "Prediction Workbench":

    st.header("Industrial Machine Learning Prediction")

    st.warning(
        "Only use predictions after confirming the model's "
        "input features, feature order, units and preprocessing."
    )

    if not models:

        st.warning("No models available for prediction.")

    for name, model in models.items():

        with st.expander(name):

            estimators = find_estimators(model)

            if not estimators:

                st.info(
                    "No predict-capable estimator was found in this artifact."
                )

                continue

            estimator_names = [
                item[0] for item in estimators
            ]

            selected = st.selectbox(
                "Choose estimator",
                estimator_names,
                key=f"estimator_{name}"
            )

            estimator = dict(estimators)[selected]

            features = getattr(
                estimator,
                "feature_names_in_",
                None
            )

            n_features = getattr(
                estimator,
                "n_features_in_",
                None
            )

            if features is not None:

                inputs = {}

                cols = st.columns(2)

                for index, feature in enumerate(features):

                    with cols[index % 2]:

                        inputs[feature] = st.number_input(
                            str(feature),
                            value=0.0,
                            key=f"{name}_{feature}"
                        )

                if st.button(
                    "Run Prediction",
                    key=f"predict_{name}"
                ):

                    try:

                        input_df = pd.DataFrame(
                            [inputs],
                            columns=list(features)
                        )

                        prediction = estimator.predict(input_df)

                        st.success(
                            f"Predicted Output: {prediction[0]}"
                        )

                    except Exception as error:

                        st.error(
                            f"Prediction failed: {error}"
                        )

            elif n_features is not None:

                st.warning(
                    f"This model expects {n_features} input features, "
                    "but their names are unavailable. Confirm the "
                    "training feature order before creating the form."
                )

            else:

                st.info(
                    "The input schema is not available in this model artifact."
                )


# ==========================================
# 15. SYSTEM INFORMATION
# ==========================================

elif page == "System Information":

    st.header("System Information")

    st.write("Application: Combined Industrial Predictive Analytics")

    st.write("Platform: Python and Streamlit")

    st.write("Model Storage: Google Drive")

    st.write("Dataset Storage: Google Sheets")

    st.write("Deployment: Streamlit Community Cloud")

    st.write("Models:", len(models), "of 4 loaded")

    st.write("Datasets:", len(datasets), "of 2 loaded")

    st.warning(
        "Only load pickle/joblib files from sources you trust. "
        "Pickle files can execute code during loading. "
        "Public Google Drive sharing may expose your files to anyone "
        "who has their links."
    )

    st.markdown(
        "[Streamlit Documentation](https://docs.streamlit.io/)"
    )

    st.markdown(
        "[Google Drive](https://drive.google.com/)"
    )


# ==========================================
# 16. FOOTER
# ==========================================

st.divider()

st.caption(
    "Combined Industrial Predictive Analytics Dashboard | "
    "Machine Learning | Industrial Operations | Energy Analytics"
)

