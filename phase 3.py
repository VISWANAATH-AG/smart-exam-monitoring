import time

risk_score = 0

print("================================")
print(" SMART EXAM RISK ENGINE")
print("================================")

while True:

    print("\nChoose Event")
    print("1. Mobile Phone Detected")
    print("2. Looking Away")
    print("3. No Violation")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        risk_score += 50
        print("Phone Detected (+50)")

    elif choice == "2":

        risk_score += 20
        print("Looking Away (+20)")

    elif choice == "3":

        print("No Violation")

    elif choice == "4":

        break

    else:

        print("Invalid Choice")
        continue

    print("\nCurrent Risk Score:", risk_score)

    if risk_score <= 30:

        print("Risk Level : LOW")

    elif risk_score <= 70:

        print("Risk Level : MEDIUM")

    else:

        print("Risk Level : HIGH")

print("\nFinal Risk Score:", risk_score)
print("System Closed")