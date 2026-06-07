# 🩺 Diabetes Prediction App

A machine learning–powered web app built with **Streamlit** that predicts the likelihood of diabetes based on patient health metrics. Designed for early detection and accessible to both technical and non-technical users.

---

## 📌 Overview

Enter key health biomarkers through a simple Streamlit interface and get an instant diabetes risk prediction from a trained ML classifier — no setup beyond Python required.

---

## ✨ Features

- **Instant Prediction** — Real-time diabetic / non-diabetic classification
- **Confidence Score** — Probability output alongside the prediction
- **Interactive UI** — Sliders and input fields for all health parameters
- **Model Insights** — Feature importance chart and confusion matrix
- **Single-file Deployment** — Runs entirely in Streamlit, no separate backend needed

---

## 🧬 Input Features

| Feature | Description |
|---|---|
| Pregnancies | Number of times pregnant |
| Glucose | Plasma glucose concentration (mg/dL) |
| Blood Pressure | Diastolic blood pressure (mm Hg) |
| Skin Thickness | Triceps skinfold thickness (mm) |
| Insulin | 2-hour serum insulin (μU/mL) |
| BMI | Body mass index (kg/m²) |
| Diabetes Pedigree Function | Genetic likelihood score |
| Age | Age in years |

> Dataset: [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) (UCI ML Repository)

---

## 🛠 Tech Stack

| Component | Technology |
|---|---|
| UI & App | Streamlit |
| ML Model | scikit-learn |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Model Serialization | joblib / pickle |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- pip / virtualenv

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/diabetes-prediction-app.git
cd diabetes-prediction-app
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Model

```bash
python train_model.py           # saves model.pkl to /model
```

### 5. Run the App

```bash
streamlit run app.py
```

App will open at `http://localhost:8501`

---

## 📁 Project Structure

```
diabetes-prediction-app/
├── app.py                      # Streamlit app (main entry point)
├── train_model.py              # Model training script
├── model/
│   └── diabetes_model.pkl      # Serialized trained model
├── data/
│   └── diabetes.csv            # Pima Indians dataset
├── notebooks/
│   └── model_training.ipynb    # EDA and training notebook
├── requirements.txt
└── README.md
```

---

## 🤖 Model Details

| Metric | Value |
|---|---|
| Algorithm | Random Forest Classifier |
| Accuracy | ~78% |
| Precision | ~76% |
| Recall | ~72% |
| F1 Score | ~74% |
| Cross-validation | 5-fold stratified |

Full EDA and training steps are in `notebooks/model_training.ipynb`.

---

## 📦 requirements.txt

```
streamlit
scikit-learn
pandas
numpy
matplotlib
seaborn
joblib
```

---

## ☁️ Deployment

Deploy for free on **Streamlit Community Cloud**:

1. Push your repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo and set `app.py` as the entry point
4. Click **Deploy**

---

## ⚠️ Disclaimer

> This application is for **educational and informational purposes only**. It is **not a substitute** for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical decisions.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Commit your changes: `git commit -m "feat: add your feature"`
4. Push and open a Pull Request

---

## 📄 License

MIT License © 2025 [Your Name]
