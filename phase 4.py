import pandas as pd
import os

print("================================")
print(" HUMAN-IN-THE-LOOP REVIEW")
print("================================")

if not os.path.exists("violations.csv"):
    print("No violations found!")
    exit()

data = pd.read_csv("violations.csv")

if len(data) == 0:
    print("No violations available.")
    exit()

for index, row in data.iterrows():

    print("\n--------------------------------")
    print("Violation ID :", index + 1)
    print("Time         :", row["Time"])
    print("Violation    :", row["Violation"])
    print("Evidence     :", row["Image"])
    print("--------------------------------")

    choice = input(
        "Approve Violation? (yes/no): "
    ).lower()

    if choice == "yes":

        data.loc[index, "Status"] = "Approved"

    else:

        data.loc[index, "Status"] = "Rejected"

data.to_csv("violations_reviewed.csv", index=False)

print("\nReview Completed!")
print("Saved as violations_reviewed.csv")