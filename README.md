# Road Accident Analysis Dashboard & NLP Pipeline

**Road Accident Analysis** is a comprehensive project combining an interactive Power BI dashboard with a Python-based NLP pipeline to analyze and classify road accident data. This repository provides end-to-end assets—from data ingestion and preprocessing to model training, evaluation, and visualization.

---

## 📋 Table of Contents
1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Getting Started](#getting-started)
4. [Prerequisites](#prerequisites)
5. [Installation](#installation)
6. [Usage](#usage)
   - [NLP Pipeline](#nlp-pipeline)
   - [Power BI Dashboard](#power-bi-dashboard)
7. [Contributing](#contributing)
8. [License](#license)

---

## ✨ Features
- **Interactive Power BI Dashboard**: Visualize accident trends, severity, and contributing factors with rich, slicable charts and maps.
- **NLP Classification Pipeline**: Clean, preprocess, and classify accident severity using logistic regression.
- **Automated Data Processing**: Scripts to generate cleaned datasets and model predictions.
- **Evaluation & Reporting**: Automated generation of classification reports and confusion matrix PNGs.

---

## 🗂️ Project Structure
```
road-accident-analysis/
├── data/
│   ├── raw/                   # Original dataset
│   │   └── Road Accident Data.csv
│   └── processed/             # Output of preprocessing and predictions
│       ├── cleaned_accident_data.csv
│       └── model_predictions.csv
├── notebooks/                 # Jupyter notebooks for EDA
│   └── 01_eda.ipynb
├── powerbi/                   # Power BI report file
│   └── Road Accident Analysis Dashboard.pbix
├── reports/                   # Generated evaluation artifacts
│   └── figures/
│       └── confusion_matrix.png
├── saved_models/              # Serialized trained model
│   └── nlp_model.pkl
├── src/                       # Source code for NLP pipeline
│   ├── __init__.py
│   ├── preprocessing.py       # Text cleaning utilities
│   ├── model.py               # Model definition
│   ├── train.py               # Training and data processing script
│   ├── evaluate.py            # Evaluation and plotting functions
│   └── utils.py               # Helper functions
├── main.py                    # Entry point for training & evaluation
├── requirements.txt           # Python dependencies
└── README.md                  # Project overview and setup instructions
```

---

## 🚀 Getting Started
Follow these steps to set up and run the project locally.

### Prerequisites
- **Python 3.7+**
- **Power BI Desktop** (to open `.pbix` file)
- (Optional) Virtual environment tool: `venv` or `conda`

---

## ⚙️ Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/road-accident-analysis.git
   cd road-accident-analysis
   ```
2. **Create and activate a virtual environment** (recommended):
   ```bash
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🖥️ Usage

### NLP Pipeline
1. Place the raw dataset at `data/raw/Road Accident Data.csv`.
2. Run the main script:
   ```bash
   python main.py
   ```
3. **Outputs**:
   - **Cleaned Data**: `data/processed/cleaned_accident_data.csv`
   - **Model Predictions**: `data/processed/model_predictions.csv`
   - **Trained Model**: `saved_models/nlp_model.pkl`
   - **Evaluation**: Console output of classification report
   - **Confusion Matrix**: `reports/figures/confusion_matrix.png`

### Power BI Dashboard
1. Open **Power BI Desktop**.
2. Navigate to `powerbi/Road Accident Analysis Dashboard.pbix`.
3. Interact with the report: slicers, maps, charts.

---



## 📄 License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

