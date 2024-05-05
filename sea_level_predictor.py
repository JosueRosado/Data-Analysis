import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
    a = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(1880,2051)
    y1 = x*a.slope + a.intercept
    plt.plot(x1,y1)

    # Create second line of best fit
    df_new = df[df.Year>=2000]
    b = linregress(x=df_new['Year'], y=df_new['CSIRO Adjusted Sea Level'])
    x2 = np.arange(2000,2051)
    y2 = x*b.slope + b.intercept
    plt.plot(x2,y2);


    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea level (inches)')
    ax.set_title('Rise in sea level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
