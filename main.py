
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Load dataset
def load_data(file_path):   
    return pd.read_csv(file_path)


# Classify defect levels into quality status categories
def classify_quality_status(defects):
    if defects >= 50:
        return "High Defects"
    elif defects >= 30:
        return "Medium Defects"
    else:
        return "Low Defects"


def print_quality_status_summary(df):
    print("\nQuality Status Summary:")
    quality_counts = df["Quality_Status"].value_counts()
    print(quality_counts)


# Print statistical summary for key numeric columns
def print_statistical_summary(df):
    print("\n--- Statistical Summary ---")

    numeric_columns = ["Production", "Defects", "Downtime_Minutes"]

    for column in numeric_columns:
        mean_value = np.mean(df[column])
        min_value = np.min(df[column])
        max_value = np.max(df[column])
        std_value = np.std(df[column])

        print(f"\n{column}")
        print(f"Mean: {mean_value:.2f}")
        print(f"Min: {min_value}")
        print(f"Max: {max_value}")
        print(f"Std: {std_value:.2f}")

    # Measures the relationship between downtime and defects
    correlation = df["Defects"].corr(df["Downtime_Minutes"])
    print(f"\nCorrelation Defects vs Downtime: {correlation:.2f}")

    if correlation >= 0.7:
        print("Interpretation: Strong positive relationship.")
    elif correlation >= 0.3:
        print("Interpretation: Moderate positive relationship.")
    elif correlation > -0.3:
        print("Interpretation: Weak or no linear relationship.")
    elif correlation > -0.7:
        print("Interpretation: Moderate negative relationship.")
    else:
        print("Interpretation: Strong negative relationship.")


# Create and save production by day bar chart
def plot_production_by_day(df):
    plt.bar(
        df["Day"],
        df["Production"],
        color=["darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkgreen", "crimson", "darkcyan"]
    )

    plt.title("Production by Day")
    plt.xlabel("Day")
    plt.ylabel("Production")
    plt.ylim(0, 1600)

    for day, production in zip(df["Day"], df["Production"]):
        plt.text(day, production + 15, str(production), ha="center")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("images/production_by_day.png", dpi=300, bbox_inches="tight")
    plt.show()


# Create and save defects by day bar chart
def plot_defects_by_day(df):
    plt.bar(
        df["Day"],
        df["Defects"],
        color=["darkcyan", "darkcyan", "darkcyan", "darkcyan", "darkgreen", "crimson", "darkcyan"]
    )

    plt.title("Defects by Day")
    plt.xlabel("Day")
    plt.ylabel("Defects")
    plt.ylim(0, 100)

    for day, defects in zip(df["Day"], df["Defects"]): 
        plt.text(day, defects +1, str(defects), ha="center")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("images/defects_by_day.png", dpi=300, bbox_inches="tight")
    plt.show()


# Create and save defects vs downtime scatter plot with trend line
def plot_defects_vs_downtime(df):
    # Calculate trend line for the relationship between downtime and defects
    pendiente, intercepto = np.polyfit(
        df["Downtime_Minutes"],
        df["Defects"],
        1
    )

    y_linea = pendiente * df["Downtime_Minutes"] + intercepto

    # Scatter plot with actual data points
    plt.scatter(
        df["Downtime_Minutes"],
        df["Defects"],
        color="darkcyan",
        s=100,
        alpha=0.8,
        label="Actual data"
    )

    # Add trend line
    plt.plot(
        df["Downtime_Minutes"],
        y_linea,
        color="crimson",
        linewidth=3,
        label="Trend Line"
    )

    plt.grid(alpha=0.3)
    plt.xlim(5, 75)
    plt.ylim(15, 65)
    plt.title("Defects vs Downtime")
    plt.xlabel("Downtime (minutes)")
    plt.ylabel("Defects")
    plt.legend()
    plt.tight_layout()
    plt.savefig("images/defects_vs_downtime.png", dpi=300, bbox_inches="tight")
    plt.show()


# Print key operational findings from the dataset
def print_key_findings(df):
    print("\n--- Key Findings ---")

    # Defects analysis
    max_defects = df["Defects"].max()
    most_defects_day = df[df["Defects"] == max_defects]

    average_defects = df["Defects"].mean()
    above_average_defects = df[df["Defects"] > average_defects]

    print("\nDefects Analysis")
    print(f"Maximum defects: {max_defects}")
    print(f"Day with most defects: {most_defects_day['Day'].iloc[0]}")
    print(f"Average defects: {average_defects:.2f}")
    print("Days with above average defects:")
    print(above_average_defects[["Day", "Defects"]])


    # Production analysis
    max_production = df["Production"].max()
    max_production_day = df[df["Production"] == max_production]

    print("\nProduction Analysis")
    print(f"Maximum production: {max_production}")
    print(f"Day with maximum production: {max_production_day['Day'].iloc[0]}")
    print(f"Production: {max_production_day['Production'].iloc[0]}")


# Run the full analysis workflow
def main():
    df = load_data("data/production_data.csv")
    
    df["Quality_Status"] = df["Defects"].apply(classify_quality_status)   
    
    print(df)
    print_statistical_summary(df)
    print_key_findings(df)
    print_quality_status_summary(df)
    
    plot_production_by_day(df)
    plot_defects_by_day(df)
    plot_defects_vs_downtime(df)


if __name__ == "__main__":
    main()
