# Equilibrium Finance: LSTM Stock Predictor

An end-to-end Machine Learning web application that predicts the next-day closing price of Microsoft (MSFT) stock. 

This project demonstrates a complete MLOps lifecycle: from Exploratory Data Analysis (EDA) and model training in a Jupyter environment, to deploying a TensorFlow/Keras LSTM model via a Django web interface with a live data pipeline.

### 🖼️ UI/UX Design
*(Place your UI screenshot here by dragging and dropping the image directly into the GitHub editor!)*

---

## 🛠️ Tech Stack
* **Machine Learning:** TensorFlow, Keras, Pandas, NumPy, Scikit-learn
* **Backend Framework:** Django, Python
* **Data Pipeline:** yfinance (Live Yahoo Finance API integration)
* **Frontend:** HTML5, CSS3 (Custom flat vector, minimalist pastel design)

---

## 🚀 Features
* **Live Data Integration:** Bypasses static CSV limitations by utilizing `yfinance` to fetch the most recent trading days upon every user request.
* **Deep Learning Inference:** Feeds live, dynamically reshaped stock data into a pre-trained Long Short-Term Memory (LSTM) neural network.
* **Frictionless UI:** Features a minimalist, single-action interface designed with soothing pastel colors to make complex data visually approachable.

---

## 🧠 The Architecture & The Efficient Market Hypothesis
While this project functions perfectly as an architectural demonstration of serving deep learning models on the web, it is important to acknowledge the mathematical limitations of predicting financial markets using univariate data.

During the EDA and recursive prediction phases of this project, the LSTM exhibited classic behaviors associated with the **Efficient Market Hypothesis (EMH)** and the **Random Walk Theory**:
1. **The Recursive Flatline:** When forced to predict multiple days into the future by feeding predictions back into itself, the model's output quickly flatlines. Without external real-world signals (news, earnings, sentiment), the model defaults to predicting the statistical mean to minimize error.
2. **The One-Day Shift:** Models trained strictly on historical closing prices often learn that the safest prediction for tomorrow's price is simply today's price. 

**Conclusion:** This model serves as a successful proof-of-concept for deploying recurrent neural networks and handling time-series sliding windows. However, a production-level trading algorithm would require multivariate inputs, sentiment analysis, and reinforcement learning to capture true market volatility. 

---

## 💻 How to Run Locally

If you would like to run this Django application on your own machine, follow these steps:

**1. Clone the repository**
```bash
git clone [https://github.com/YourUsername/YourRepositoryName.git](https://github.com/YourUsername/YourRepositoryName.git)
cd YourRepositoryName
```

**2. Create a Virtual Environment**
```bash
python -m venv venv
```
**3. Activate the Virtual Environment**
```bash
source venv/Scripts/activate
```
**4. Install dependencies**
```bash
pip install -r requirements.txt
```
**5. Start Django Server**
```bash
python manage.py runserver
```
**6. View the App**

Open your web browser and navigate to http://127.0.0.1:8000/
