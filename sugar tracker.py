import csv
import datetime

class SugarTracker:
    def __init__(self, file='sugar_readings.csv', insulin_file='insulin_doses.csv', age=None):
        self.file = file
        self.insulin_file = insulin_file
        self.age = age
        try:
            with open(self.file, 'r') as f:
                pass
        except FileNotFoundError:
            with open(self.file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Date', 'Time', 'Glucose Level'])
        try:
            with open(self.insulin_file, 'r') as f:
                pass
        except FileNotFoundError:
            with open(self.insulin_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Date', 'Time', 'Insulin Type', 'Dose'])

    def log_reading(self, level):
        now = datetime.datetime.now()
        date = now.strftime('%Y-%m-%d')
        time = now.strftime('%H:%M:%S')
        with open(self.file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([date, time, level])
        print(f"Logged reading: {level} mg/dL at {time}")
        self.check_level(level)

    def log_insulin(self, insulin_type, dose):
        now = datetime.datetime.now()
        date = now.strftime('%Y-%m-%d')
        time = now.strftime('%H:%M:%S')
        with open(self.insulin_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([date, time, insulin_type, dose])
        print(f"Logged insulin: {dose} units of {insulin_type} at {time}")

    def check_level(self, level):
        if self.age is not None:
            if self.age <= 1:  # Newborn to 1 year
                low = 50
                high = 150
            elif self.age <= 6:  # 1-6 years
                low = 70
                high = 180
            elif self.age <= 12:  # 6-12 years
                low = 70
                high = 180
            else:  # 12-18 years
                low = 70
                high = 200
        else:
            low = 70
            high = 200
        if level < low:
            print("⚠️ Low Sugar! Give juice or glucose")
        elif level > high:
            print("⚠️ High Sugar! Check insulin/diet")
        else:
            print("✅ Normal")

    def view_history(self):
        try:
            with open(self.file, 'r') as f:
                reader = csv.reader(f)
                print("Date\t\tTime\t\tGlucose Level")
                print("-" * 40)
                for row in reader:
                    if row[0] != 'Date':  # Skip header
                        print(f"{row[0]}\t{row[1]}\t{row[2]}")
        except FileNotFoundError:
            print("No readings logged yet.")

    def view_insulin_history(self):
        try:
            with open(self.insulin_file, 'r') as f:
                reader = csv.reader(f)
                print("Date\t\tTime\t\tInsulin Type\t\tDose")
                print("-" * 50)
                for row in reader:
                    if row[0] != 'Date':  # Skip header
                        print(f"{row[0]}\t{row[1]}\t{row[2]}\t\t\t{row[3]}")
        except FileNotFoundError:
            print("No insulin doses logged yet.")

    def suggest_low_gi_foods(self):
        print("Low GI Indian Food Suggestions:")
        print("\nFruits:")
        fruits = [
            "Guava",
            "Pomegranate",
            "Apple",
            "Pear",
            "Orange",
            "Kiwi",
            "Blueberries",
            "Strawberries",
            "Cherries",
            "Grapes"
        ]
        for food in fruits:
            print(f"- {food}")
        
        print("\nDry Fruits/Nuts:")
        dry_fruits = [
            "Almonds",
            "Walnuts",
            "Peanuts",
            "Cashews",
            "Pistachios"
        ]
        for food in dry_fruits:
            print(f"- {food}")
        
        print("\nLentils/Pulses:")
        lentils = [
            "Moong Dal (Yellow Lentils)",
            "Chana Dal (Bengal Gram)",
            "Toor Dal (Pigeon Pea)",
            "Urad Dal (Black Gram)"
        ]
        for food in lentils:
            print(f"- {food}")
        
        print("\nGrains:")
        grains = [
            "Brown Rice",
            "Quinoa",
            "Whole Wheat Chapati (made with whole grain)",
            "Bajra (Pearl Millet) Roti",
            "Jowar (Sorghum) Roti"
        ]
        for food in grains:
            print(f"- {food}")
        
        print("\nVegetables:")
        vegetables = [
            "Spinach (Palak)",
            "Bitter Gourd (Karela)",
            "Okra (Bhindi)",
            "Brinjal (Eggplant)",
            "Cucumber",
            "Tomatoes",
            "Onions",
            "Garlic",
            "Ginger",
            "Curry Leaves",
            "Fenugreek Leaves (Methi)",
            "Drumstick (Moringa)"
        ]
        for food in vegetables:
            print(f"- {food}")
        
        print("\nDairy:")
        dairy = [
            "Yogurt (Dahi) - plain, unsweetened"
        ]
        for food in dairy:
            print(f"- {food}")
        
        print("\nTraditional Dishes:")
        dishes = [
            "Idli (made with less rice, more urad dal)",
            "Dhokla",
            "Khichdi (made with moong dal and vegetables)",
            "Rajma (Kidney Beans) - in moderation",
            "Chana Masala (Chickpea Curry)",
            "Palak Paneer (Spinach with Cottage Cheese)",
            "Baingan Bharta (Eggplant Mash)",
            "Aloo Gobi (Potato and Cauliflower) - use less potato",
            "Mixed Vegetable Curry",
            "Chicken or Fish Curry with vegetables",
            "Egg Curry",
            "Tandoori Chicken (grilled, no marinade sugar)"
        ]
        for food in dishes:
            print(f"- {food}")

    def view_health_summary(self):
        print("Health Summary:")
        try:
            with open(self.file, 'r') as f:
                reader = csv.reader(f)
                readings = []
                for row in reader:
                    if row[0] != 'Date':
                        readings.append(float(row[2]))
                if readings:
                    avg_glucose = sum(readings) / len(readings)
                    min_glucose = min(readings)
                    max_glucose = max(readings)
                    print(f"Average Glucose: {avg_glucose:.1f} mg/dL")
                    print(f"Min Glucose: {min_glucose} mg/dL")
                    print(f"Max Glucose: {max_glucose} mg/dL")
                    print(f"Total Readings: {len(readings)}")
                    # Alert
                    if self.age is not None:
                        if self.age <= 1:
                            high = 150
                        elif self.age <= 6:
                            high = 180
                        elif self.age <= 12:
                            high = 180
                        else:
                            high = 200
                    else:
                        high = 200
                    if avg_glucose > high:
                        print("⚠️ Alert: Average glucose is high. Consult doctor or adjust insulin/diet.")
                    elif avg_glucose < 70:
                        print("⚠️ Alert: Average glucose is low. Monitor for hypoglycemia.")
                    else:
                        print("✅ Average glucose is within normal range.")
                else:
                    print("No glucose readings logged.")
        except FileNotFoundError:
            print("No glucose readings logged.")
        
        try:
            with open(self.insulin_file, 'r') as f:
                reader = csv.reader(f)
                total_insulin = 0
                count = 0
                for row in reader:
                    if row[0] != 'Date':
                        total_insulin += float(row[3])
                        count += 1
                if count > 0:
                    print(f"Total Insulin Dosed: {total_insulin} units")
                    print(f"Insulin Entries: {count}")
                else:
                    print("No insulin doses logged.")
        except FileNotFoundError:
            print("No insulin doses logged.")

    def view_trends(self):
        print("Glucose Trends (last 7 days):")
        try:
            from collections import defaultdict
            with open(self.file, 'r') as f:
                reader = csv.reader(f)
                daily_readings = defaultdict(list)
                for row in reader:
                    if row[0] != 'Date':
                        date = row[0]
                        level = float(row[2])
                        daily_readings[date].append(level)
                if daily_readings:
                    # Sort dates
                    sorted_dates = sorted(daily_readings.keys(), reverse=True)[:7]
                    for date in sorted_dates:
                        levels = daily_readings[date]
                        avg = sum(levels) / len(levels)
                        print(f"{date}: Avg {avg:.1f} mg/dL ({len(levels)} readings)")
                else:
                    print("No readings to analyze.")
        except FileNotFoundError:
            print("No glucose readings logged.")

def main():
    try:
        age = int(input("Enter age in years (0 for newborn): "))
    except ValueError:
        print("Invalid age. Using default thresholds.")
        age = None
    tracker = SugarTracker(age=age)
    while True:
        print("\nSugar Level Tracker for Type 1 Diabetics")
        print("1. Log Blood Glucose Reading")
        print("2. View Reading History")
        print("3. Get Low GI Indian Food Suggestions")
        print("4. Log Insulin Dose")
        print("5. View Insulin History")
        print("6. Check Sugar Level")
        print("7. View Health Summary")
        print("8. View Trends")
        print("9. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            try:
                level = float(input("Enter glucose level (mg/dL): "))
                tracker.log_reading(level)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '2':
            tracker.view_history()
        elif choice == '3':
            tracker.suggest_low_gi_foods()
        elif choice == '4':
            insulin_type = input("Enter insulin type (e.g., Rapid-acting, Long-acting): ")
            try:
                dose = float(input("Enter dose (units): "))
                tracker.log_insulin(insulin_type, dose)
            except ValueError:
                print("Invalid input. Please enter a number for dose.")
        elif choice == '5':
            tracker.view_insulin_history()
        elif choice == '6':
            try:
                level = float(input("Enter glucose level to check (mg/dL): "))
                tracker.check_level(level)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '7':
            tracker.view_health_summary()
        elif choice == '8':
            tracker.view_trends()
        elif choice == '9':
            print("Exiting tracker.")
            break
        else:
            print("Invalid choice. Please select 1-9.")

if __name__ == "__main__":
    main()