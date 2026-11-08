# Combined Industrial Predictive Analytics Dashboard

A Streamlit starter app that downloads four `.pkl` model artifacts from public Google Drive links and reads two Google Sheets as CSV.

## Files
- `streamlit_app.py` — dashboard, downloads, dataset explorer, artifact inspection, cautious prediction workbench.
- `requirements.txt` — Python dependencies.

## Run locally
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy to Streamlit Community Cloud
1. Push these files to a GitHub repository.
2. Create an app in Streamlit Community Cloud.
3. Select `streamlit_app.py` as the entry point.
4. Deploy.

The four Drive files and two Sheets must be accessible using **Anyone with the link – Viewer**.
The app currently uses the supplied IDs directly. It does not need Google credentials for public files.

## Important
The app initially labels the models Model 1–4 and the sheets Dataset 1–2 because their business roles and schemas have not yet been confirmed. It inspects artifacts and displays dataset columns so the next iteration can map each model to the correct input features, preprocessing steps, target and dashboard KPI.

Only load pickle/joblib artifacts that you created or trust. Pickle files can execute code when loaded. Public link sharing may expose data to anyone with the link.
