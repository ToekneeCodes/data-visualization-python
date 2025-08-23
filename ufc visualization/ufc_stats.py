import pandas as pd
import matplotlib.pyplot as plt

# Load data
ufc_frame = pd.read_csv("rankings_history.csv")

# Make sure date is treated as datetime
ufc_frame["date"] = pd.to_datetime(ufc_frame["date"])


# let user pick what weightclass they would like to view
while True:
    weightclass = input("Enter a valid UFC weightclass: ")
    weightclass = weightclass.capitalize()
    if weightclass in ufc_frame["weightclass"].unique():
        break


# filtering top 5 fighters depending on user input
def plot_top5(weightclass):
    if weightclass not in ufc_frame["weightclass"].unique():
        return "Not valid weightclass, please enter again"
    wc_data = ufc_frame[ufc_frame["weightclass"] == weightclass]
    
    top5 = (
    wc_data.groupby("fighter")["rank"]
    .mean()
    .nsmallest(5)  # smallest rank numbers are better
    .index
    )

    filtered = wc_data[wc_data["fighter"].isin(top5)]

    pivot = filtered.pivot_table(
    index="date",
    columns="fighter",
    values="rank",
    aggfunc="min"
    )

    pivot.plot(kind="line", marker="o", linestyle="--", figsize=(12,6))
    plt.title(f"Top 5 {weightclass} Rankings Over Time")
    plt.xlabel("Date")
    plt.ylabel("Rank")
    plt.gca().invert_yaxis()
    plt.legend(title="Fighter", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

plot_top5(weightclass)


