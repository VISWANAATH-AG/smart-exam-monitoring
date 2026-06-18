import pandas as pd
import os

print("================================")
print(" AI REPORT GENERATOR")
print("================================")

# Check reviewed file

if not os.path.exists("violations_reviewed.csv"):
    print("Error: violations_reviewed.csv not found")
    exit()

data = pd.read_csv("violations_reviewed.csv")

approved = data[data["Status"] == "Approved"]

total = len(data)
approved_count = len(approved)

# Risk Level

if approved_count == 0:
    risk_level = "LOW"

elif approved_count <= 3:
    risk_level = "MEDIUM"

else:
    risk_level = "HIGH"

# Create Report

report = f"""
================================
SMART EXAM MONITORING REPORT
================================

Total Violations : {total}

Approved Violations : {approved_count}

Risk Level : {risk_level}

Violation Summary:
"""

for index, row in approved.iterrows():

    report += f"\n- {row['Violation']}"

report += """

Recommendation:
"""

if risk_level == "LOW":

    report += """
Student behavior appears normal.
No further action required.
"""

elif risk_level == "MEDIUM":

    report += """
Some suspicious activity detected.
Manual verification recommended.
"""

else:

    report += """
Repeated suspicious behavior detected.
Immediate review by invigilator advised.
"""

print(report)

# Save Report

with open("final_report.txt", "w") as file:
    file.write(report)

print("\nReport saved as final_report.txt")