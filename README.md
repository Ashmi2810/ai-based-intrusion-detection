# AI-Based Intrusion Detection System (IDS)

## Project Overview
This project implements an **AI-based Intrusion Detection System (IDS)** to detect anomalies and potential attacks in network traffic. It uses **machine learning** to analyze network data and identify suspicious activity in real-time.

---

## Problem Statement
Traditional network security systems rely heavily on predefined rules and signatures, making them less effective against new or evolving attacks.  
This project aims to:

- Automatically detect anomalies in network traffic
- Reduce false positives compared to rule-based IDS
- Provide a real-time dashboard for easy monitoring

---

## Workflow
The project follows a structured pipeline:

1. **Data Collection (`collector.py`)**  
   Captures network traffic and saves it in CSV format (`traffic.csv`)

2. **Data Inspection (`inspect_data.py`)**  
   Explores and analyzes collected data to understand patterns

3. **Data Preparation (`prepare_data.py`)**  
   Cleans and transforms data to be suitable for machine learning

4. **Model Training (`train_ids.py`)**  
   Trains an Isolation Forest model to detect anomalies in network traffic

5. **Dashboard (`dashboard.py`)**  
   Visualizes detected anomalies in real-time using Streamlit

---

## Machine Learning Model
**Isolation Forest** is used for anomaly detection:

- Detects outliers in high-dimensional data
- Efficient for real-time network monitoring
- Requires minimal labeled data

---

## How to Run the Project

### 1️⃣ Install dependencies
pip install -r requirements.txt

### 2️⃣ Run the collector
python collector.py

### 3️⃣ Inspect and prepare data
python inspect_data.py
python prepare_data.py

### 3️⃣ Inspect and prepare data
python inspect_data.py
python prepare_data.py

### 4️⃣ Train the IDS model
python train_ids.py

### 5️⃣ Launch the dashboard
streamlit run dashboard.py

## Output / Dashboard
The Streamlit dashboard shows:

- Network traffic overview
- Detected anomalies highlighted
- Real-time updates with new data

 ### screenshots/
 ├── dashboard.png
 ├── anomaly_output.png

## Project Structure
├── collector.py
├── inspect_data.py
├── prepare_data.py
├── train_ids.py
├── dashboard.py
├── traffic.csv
├── clean_data.csv
├── ids_output.csv
├── requirements.txt
├── README.md
└── screenshots/

## Key Skills & Tools:

-Python, Pandas, Scikit-learn
-Machine Learning (Anomaly Detection)
-Streamlit for interactive dashboards
-Git & GitHub for version control

## Author
**Ashmi Parmar**
**Data Science Enthusiast | ML Projects | GitHub Portfolio**



