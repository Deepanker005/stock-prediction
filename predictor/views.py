from django.shortcuts import render
import os
import numpy as np
import yfinance as yf
from tensorflow.keras.models import load_model

# 1. Locate and load your trained brain when the server starts
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'stock_lstm_model.keras')
model = load_model(MODEL_PATH)

def home(request):
    # Default variables to send to the HTML before the button is clicked
    context = {
        'predicted_price': None, 
        'status_text': '&#9432; Awaiting prediction generation'
    }
    
    # 2. Check if the user clicked the "Predict" button (a POST request)
    if request.method == 'POST':
        try:
            # Fetch the last 5 days of real MSFT stock data
            msft = yf.Ticker("MSFT")
            hist = msft.history(period="5d")
            
            # Isolate the Closing prices for the last 3 days 
            # (Note: Change the '3' if your Jupyter Notebook sliding window used a different number of days!)
            recent_closes = hist['Close'].values[-3:] 
            
            # Reshape the data for the LSTM: (Batch Size, Time Steps, Features) -> (1, 3, 1)
            x_input = np.array(recent_closes).reshape((1, 3, 1))
            
            # 3. Make the Prediction
            prediction = model.predict(x_input)
            
            # Extract the raw number and round it to 2 decimal places
            predicted_value = round(float(prediction[0][0]), 2)
            
            # 4. Update the context to send back to the HTML
            context['predicted_price'] = f"{predicted_value:,.2f}"
            context['status_text'] = '&#10003; Prediction successfully generated from live data'
            
        except Exception as e:
            # If anything breaks, show the error on the screen cleanly
            context['status_text'] = f'&#9888; Error: {str(e)}'

    return render(request, 'index.html', context)