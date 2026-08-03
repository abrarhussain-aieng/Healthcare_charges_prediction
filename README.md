# 🏥 Healthcare Charges Prediction

A Machine Learning web application that predicts **medical insurance charges** based on patient information using a trained **Gradient Boosting Regressor**.

The application provides an interactive interface where users can enter healthcare-related information and receive real-time predicted insurance charges through a deployed Streamlit application.

---

## 🚀 Live Demo

You can try the deployed application here:

🔗 https://healthcarechargesprediction-nmypkjlay7qxdr3cmgkkz9.streamlit.app/

---

# 📌 Project Overview

Healthcare cost prediction helps insurance companies and healthcare providers estimate future medical expenses based on patient characteristics.

This project uses Machine Learning regression techniques to predict healthcare charges by analyzing important factors such as age, BMI, smoking status, and other patient attributes.

The complete Machine Learning workflow includes:

- Data preprocessing
- Exploratory Data Analysis
- Feature engineering
- Model training
- Model evaluation
- Model deployment using Streamlit

---

# 🤖 Machine Learning Model

## Algorithm Used

### Gradient Boosting Regressor

Gradient Boosting is an ensemble learning algorithm that combines multiple weak prediction models (decision trees) sequentially to create a powerful regression model.

It improves prediction accuracy by reducing errors from previous models.

---

# 🔄 Machine Learning Workflow

```
Dataset
   |
   ↓
Data Cleaning
   |
   ↓
Exploratory Data Analysis
   |
   ↓
Feature Engineering
   |
   ↓
Encoding & Preprocessing
   |
   ↓
Gradient Boosting Model Training
   |
   ↓
Model Evaluation
   |
   ↓
Save Model (.pkl)
   |
   ↓
Streamlit Deployment
```

---

# 📊 Model Performance

The Gradient Boosting Regressor achieved the following performance on the test dataset:

| Metric | Score |
|---|---|
| R² Score | 0.9028 |
| Mean Absolute Error (MAE) | 2507.7637 |
| Mean Squared Error (MSE) | 17856861.8576 |
| Root Mean Squared Error (RMSE) | 4225.738 |

---

## Performance Interpretation

- **R² Score (0.9028)** indicates that the model explains approximately **90.28% of the variation** in healthcare charges.
- **MAE (2507.76)** means the average prediction error is around 2508 charges units.
- **RMSE (4225.74)** measures the overall prediction error while giving more weight to larger mistakes.

---

# 📂 Project Structure

```
Healthcare_Charges_Prediction/

│
├── app.py
├── requirements.txt
├── runtime.txt
│
├── gbr_model.pkl
├── scaler.pkl
├── columns.pkl
│
└── README.md
```

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Machine Learning

- Scikit-learn
- Gradient Boosting Regressor
- Joblib

## Data Processing

- Pandas
- NumPy

## Visualization

- Matplotlib
- Seaborn

## Deployment

- Streamlit
- GitHub
- Streamlit Community Cloud

---

# 📥 Input Features

The model uses healthcare-related patient information including:

- Age
- Gender
- BMI
- Number of Children
- Smoking Status
- Region
- Other patient attributes

---

# 🖥️ Application Features

✅ Interactive healthcare input form  
✅ Real-time insurance charge prediction  
✅ Machine Learning powered regression model  
✅ Modern Streamlit user interface  
✅ Fast prediction response  
✅ Cloud deployment ready  

---

# 🧠 Model Files

### `gbr_model.pkl`

Contains the trained Gradient Boosting Regressor used for predicting healthcare charges.

### `scaler.pkl`

Contains preprocessing/scaling transformation used before prediction.

### `columns.pkl`

Stores the final feature column order used during model training to ensure prediction consistency.

---

# 📦 Installation & Setup

Clone the repository:

```bash
git clone https://github.com/yourusername/Healthcare_Charges_Prediction.git
```

Navigate into the project directory:

```bash
cd Healthcare_Charges_Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# 🌐 Deployment

The application is deployed using:

**Streamlit Community Cloud**

Live Application:

https://healthcarechargesprediction-nmypkjlay7qxdr3cmgkkz9.streamlit.app/

---

# 🚀 Future Improvements

- Add prediction confidence intervals
- Add explainable AI using SHAP
- Add healthcare cost visualization dashboard
- Improve model comparison section
- Deploy using FastAPI backend

---

# 👨‍💻 Author

**Abrar Hussain**

Machine Learning Developer

---

# 📜 License

This project is created for educational and portfolio purposes.
