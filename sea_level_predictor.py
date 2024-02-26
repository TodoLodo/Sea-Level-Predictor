import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(16, 9))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Plot the line of best fit extending to the year 2050
    x_values = range(df["Year"].min(), 2051)
    y_values = slope * x_values + intercept
    ax.plot(x_values, y_values, color="red", label="Line of Best Fit")

    # Create second line of best fit
    recent_data = df[df["Year"] >= 2000]
    slope, intercept, _, _, _ = linregress(recent_data["Year"], recent_data["CSIRO Adjusted Sea Level"])

    # Plot the line of best fit extending to the year 2050
    x_values = range(2000, 2051)
    y_values = slope * x_values + intercept
    ax.plot(x_values, y_values, color="green", label="Line of Best Fit (2000-Present)")

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    #ax.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    #plt.show()
    plt.savefig('sea_level_plot.png')
    return plt.gca()

#draw_plot()