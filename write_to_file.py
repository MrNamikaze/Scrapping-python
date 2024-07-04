from datetime import datetime

current_date = datetime.now().date()
formatted_date = current_date.strftime("%d-%m-%Y")
print("Formatted date:", formatted_date)