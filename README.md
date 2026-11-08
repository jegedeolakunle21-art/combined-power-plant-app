# 🏭 Combined Power Plant & Industrial Predictive Analytics Dashboard

### Machine Learning | Power Plant Performance | Predictive Analytics | Energy Optimization

An integrated machine learning and industrial analytics application developed with **Python and Streamlit** to support predictive modelling, industrial dataset exploration, model inspection, and operational decision support.

The application provides a centralized dashboard for working with trained machine learning models and industrial datasets, with an emphasis on energy systems, power plant performance, and industrial operations.

## 🚀 Project Overview

Power plants and industrial facilities generate operational data that can be used to improve equipment reliability, energy efficiency, and operational performance.

This project demonstrates how machine learning and interactive data visualization can support industrial analytics by integrating trained predictive models, datasets, and an interactive dashboard.

The application connects to trained model artifacts stored in Google Drive and datasets stored in Google Sheets, allowing users to explore data, inspect machine learning models, and generate predictions through a web-based interface.

## 🎯 Project Objectives

- Develop an integrated industrial predictive analytics platform.
- Apply machine learning to industrial and energy-related datasets.
- Support power plant performance analysis and operational decision-making.
- Provide an interactive environment for exploring industrial datasets.
- Enable inspection and deployment of trained machine learning models.
- Demonstrate the application of AI and data analytics to energy systems.

## ✨ Key Features

### 1. Industrial Analytics Overview
- Displays the number of successfully loaded machine learning models.
- Tracks dataset connection status.
- Displays total dataset records.
- Provides an overview of application resources.

### 2. Dataset Explorer
- Loads datasets from Google Sheets.
- Displays dataset previews.
- Reports dataset dimensions and missing values.
- Generates descriptive statistical summaries.
- Provides interactive variable trend visualizations.

### 3. Machine Learning Model Inspection
- Loads four trained machine learning model artifacts.
- Identifies prediction-capable estimators.
- Displays model object types.
- Inspects available model components and dictionary keys.
- Displays model file sizes and loading errors.

### 4. Prediction Workbench
- Provides an interactive prediction interface.
- Detects available model input features.
- Generates numerical input fields automatically.
- Executes predictions using trained estimators.
- Displays prediction outputs and error messages.

### 5. System Information
- Displays application architecture and deployment information.
- Provides model and dataset loading statistics.
- Includes information about external data storage.

## ⚡ Power Plant and Energy Analytics Applications

The project is designed to support machine learning applications in industrial energy systems, including:

- Power plant performance prediction.
- Net power output analysis.
- Net heat rate prediction.
- CO₂ emissions prediction.
- Energy efficiency monitoring.
- Industrial operational analytics.
- Data-driven performance optimization.

The current dashboard provides generic model inspection and prediction interfaces. Individual model roles and engineering KPIs should be mapped to their corresponding artifacts before interpreting predictions as specific plant performance indicators.

## 🛠️ Technology Stack

| Technology | Application |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive dashboard |
| Pandas | Data manipulation |
| NumPy | Numerical computing |
| Scikit-learn | Machine learning |
| Joblib | Model serialization and loading |
| Pickle | Model artifact loading |
| Plotly | Interactive visualization |
| Google Drive | Trained model storage |
| Google Sheets | Dataset storage |
| Requests | Data retrieval |
| GitHub | Version control and source code hosting |
| Streamlit Community Cloud | Application deployment |

## 🏗️ Application Architecture

The application follows a simple data-driven architecture:

```text
       GOOGLE DRIVE
      (Trained Models)
             |
             v
       Model Download
          (gdown)
             |
             v
       Model Loading
     (Joblib / Pickle)
             |
             |
             v
       STREAMLIT APP
             |
      +------+------+
      |      |      |
      v      v      v
   Overview Dataset Model
            Explorer Inspection
             |
             v
       Prediction
        Workbench
             |
             v
      Prediction Results


       GOOGLE SHEETS
       (Industrial Data)
             |
             v
       CSV Data Loading
             |
             v
       Dataset Explorer
             |
             v
      Statistical Analysis
       & Visualization
```

## 📂 Repository Structure

```text
combined-power-plant-app/
│
├── streamlit_app.py
│
├── requirements.txt
│
├── README.md
│
└── LICENSE
```

**Note:** Trained model files and datasets are stored externally in Google Drive and Google Sheets rather than being committed directly to the repository.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/jegedeolakunle21-art/combined-power-plant-app.git
```

### 2. Navigate into the project directory

```bash
cd combined-power-plant-app
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure external data sources

The application retrieves:

- Four trained model artifacts from Google Drive.
- Two datasets from Google Sheets.

Ensure the Google Drive model files and Google Sheets are accessible to the application using the configured sharing permissions.

The corresponding file identifiers are configured in `streamlit_app.py`.

### 6. Run the application

```bash
streamlit run streamlit_app.py
```

The application will open in your browser.

## ☁️ Deployment

The application is designed for deployment using Streamlit Community Cloud.

Deployment procedure:

1. Push the project repository to GitHub.
2. Visit https://share.streamlit.io/
3. Sign in using your GitHub account.
4. Select the `combined-power-plant-app` repository.
5. Select the `main` branch.
6. Set the application entry point to `streamlit_app.py`.
7. Deploy the application.

The trained model artifacts are downloaded from Google Drive, while datasets are retrieved from Google Sheets.

## 🔬 Engineering and Research Significance

This project demonstrates the integration of mechanical engineering, power plant systems, machine learning, and industrial data analytics.

It provides a foundation for developing intelligent energy management systems capable of supporting:

- Predictive power plant performance monitoring.
- Energy efficiency assessment.
- Carbon emissions analysis.
- Machine learning-assisted operational decisions.
- Industrial digital transformation.

Future development will focus on linking individual machine learning models to clearly defined engineering performance indicators, adding model validation metrics, and integrating real-time operational data.

## 🔮 Future Improvements

- Integration of real-time power plant sensor data.
- Automated performance monitoring.
- Advanced machine learning model comparison.
- Model accuracy and validation dashboards.
- Predictive maintenance integration.
- Power plant optimization algorithms.
- Explainable AI using SHAP.
- Carbon emissions and energy efficiency benchmarking.
- Integration with industrial IoT and SCADA systems.
- Automated operational alerts.

## ⚠️ Important Notes

- Model files must be accessible through their configured Google Drive permissions.
- Google Sheets must allow the application to retrieve CSV data.
- Model inputs, feature ordering, units, and preprocessing must be verified before using predictions.
- Only load trusted Pickle or Joblib model files because serialized files can execute malicious code.
- Public sharing links should be used cautiously. Avoid exposing confidential industrial data or sensitive credentials.

## 👨‍💻 Author

**Olakunle Jegede**

Mechanical Engineer | Energy Systems | Machine Learning | Industrial Analytics | Predictive Maintenance

**Technical Interests:**
- Thermodynamics and Heat Transfer
- Power Plant Engineering
- Computational Fluid Dynamics (CFD)
- Artificial Intelligence and Machine Learning
- Energy Optimization
- Industrial Predictive Analytics

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## ⭐ Acknowledgements

This project reflects the application of machine learning, engineering principles, and data analytics to industrial energy systems.

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

**Project:** Combined Power Plant & Industrial Predictive Analytics Dashboard

**Repository:** https://github.com/jegedeolakunle21-art/combined-power-plant-app
