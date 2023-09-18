# Main.py using polars and matplotlib to set data and see some plot

import polars as pl
import matplotlib.pyplot as plt


# Load the dataset from .csv file
def load_data():
    penguins_df = pl.read_csv("penguins.csv")
    print(penguins_df)


# Calculate mean, median, standard deviation of each columns
def calculate_stat():
    penguins_desc = load_data.describe()
    print(penguins_desc)


calculate_stat()


# Make a histogram of 'bill_length_mm' column in penguins.csv
def build_histogram():
    plt.hist(load_data["bill_length_mm"], bins=20, color="green", edgecolor="white")
    plt.xlabel("bill_length_mm")
    plt.ylabel("Frequency")
    plt.title("Bill Length Histogram")
    plt.savefig("bill_length_hist.png")
    plt.show()
    return


build_histogram()
