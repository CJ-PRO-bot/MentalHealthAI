# Healthcare Data Science Project – Bhutan
### --Using WHO Health Indicators to Support Mental Health Insights in Bhutan

This project is an end-to-end Python data science workflow built to analyze Bhutan’s national health indicators using official datasets from the World Health Organization (WHO) Global Health Observatory (GHO).
Although the dataset covers many general health indicators (life expectancy, cholesterol, mortality rates, etc.), one long-term goal of this project is to use these indicators to support mental-health–related insights, such as understanding:
how lifestyle, non-communicable diseases, or demographic factors may correlate with mental health trends, how national health patterns evolve over time, which regions or years show unusual patterns that may relate to stress, wellbeing, or broader public-health conditions.

This project lays the technical foundation for future mental-health prediction and research tools in Bhutan.

## Project Objectives
Analyze official WHO health indicators for Bhutan

Build a reproducible Python data analysis pipeline

Perform data cleaning, preparation, and exploratory data analysis (EDA)

Prepare datasets for future prediction models (e.g., forecasting life expectancy, identifying risk patterns)

Build a basic Streamlit dashboard to visualize health trends

Support longer-term goals of studying mental health from a scientific, data-driven perspective

## Project Structure
healthcare-bhutan/
│
├── data/
│   ├── raw/                # Raw WHO datasets (CSV)
│   ├── processed/          # Cleaned and preprocessed data
│
├── notebooks/
│   ├── 01_data_exploration.ipynb   # Jupyter EDA (cleaning, plots)
│   ├── 02_feature_engineering.ipynb (upcoming)
│   ├── 03_modeling.ipynb           (upcoming)
│
├── src/
│   ├── data_loader.py      # Data loading + initial cleaning functions
│   ├── preprocessing.py     # Advanced preprocessing for modeling
│   ├── train_model.py       # Simple ML training script
│   ├── utils.py             # Helper utilities
│
├── app/
│   ├── streamlit_app.py     # Interactive dashboard
│
├── models/
│   ├── life_expectancy_model.pkl (upcoming)
│
├── starter.py               # Runs Step 1 cleaning pipeline
├── run_preprocessing.py     # Runs Step 2 preprocessing
├── requirements.txt         # Dependencies
└── README.md


## Dataset Source
All health indicators are taken from:

WHO Global Health Observatory (GHO)
🔗 https://data.humdata.org/dataset/who-data-for-btn

(official WHO dataset for Bhutan)

The dataset includes indicators such as:

Life expectancy

Mortality rates

Non-communicable disease metrics

Cholesterol and blood pressure values

Health law implementations

Environmental health metrics

These indicators help us understand broader public health patterns that may indirectly influence mental-health risks.

## Installation & Setup
1. Create a virtual environment
python -m venv venv
source venv/bin/activate     # macOS / Linux
venv\Scripts\activate        # Windows

2. Install dependencies
pip install -r requirements.txt

3. Run the cleaning pipeline
python starter.py

4. Run preprocessing (optional, for ML)
python run_preprocessing.py

5. Launch Streamlit dashboard
streamlit run app/streamlit_app.py

## Why Mental Health?
While the dataset does not provide direct “depression/suicide” indicators, mental health is influenced by many general health and societal indicators, such as:

life expectancy

NCD burden

alcohol & tobacco indicators

household fuel use

demographic stress

healthcare access

Understanding national health trends is the first step toward building data-driven mental-health insights for Bhutan.

This project builds the technical foundation for future work such as:

risk-factor analysis

early warning indicators

district-level health/mood segmentation

simple mental-health prediction models

## License
This project is open-source under the MIT License
