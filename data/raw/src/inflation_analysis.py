import pandas as pd
import matplotlib.pyplot as plt

def plot_inflation(df):
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Index'], label='Inflation Index')
    plt.title('UK Inflation Trend')
    plt.xlabel('Date')
    plt.ylabel('Index')
    plt.legend()
    plt.show()
