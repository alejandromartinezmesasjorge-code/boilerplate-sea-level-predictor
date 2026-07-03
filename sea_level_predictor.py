import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # First line of best fit (1880-2050)
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x = pd.Series(range(1880, 2051))
    y = res.intercept + res.slope * x
    plt.plot(x, y, "r", label="Best Fit 1880-2050")

    # Second line of best fit (2000-2050)
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )
    x_recent = pd.Series(range(2000, 2051))
    y_recent = res_recent.intercept + res_recent.slope * x_recent
    plt.plot(x_recent, y_recent, "green", label="Best Fit 2000-2050")

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing
    plt.savefig("sea_level_plot.png")
    return plt.gca()