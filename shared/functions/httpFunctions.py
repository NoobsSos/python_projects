from tabulate import tabulate
import requests
import datetime

from shared.classes.saveClasses.SaveContext import SaveContext
from shared.classes.saveClasses.SaveCSV import SaveCSV
from shared.classes.saveClasses.SaveTXT import SaveTXT
from shared.classes.saveClasses.SaveJSON import SaveJSON

def flatten_data(data, parent_key='', sep='_'):
    """
    Рекурсивно розпаковує вкладені словники/списки в одну плоску структуру.
    """
    items = []

    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            items.extend(flatten_data(value, new_key, sep=sep))
    elif isinstance(data, list):
        for idx, value in enumerate(data):
            new_key = f"{parent_key}{sep}{idx}" if parent_key else str(idx)
            items.extend(flatten_data(value, new_key, sep=sep))
    else:
        items.append((parent_key, data))

    return items

def color_table_headers(table_str, color_code):
    color_start = f'\033[{color_code}m'
    color_end = '\033[0m'

    table_lines = table_str.splitlines()

    table_lines[1] = color_start + table_lines[1] + color_end

    return "\n".join(table_lines)

def displayData(data, color_code):
    if isinstance(data, list):
        # If it's a list, flatten each item
        flattened_data = [dict(flatten_data(item)) for item in data]
    else:
        # If it's a dictionary, flatten the single item
        flattened_data = [dict(flatten_data(data))]

    # Use tabulate to print the table with "keys" as headers
    table = tabulate(flattened_data, headers="keys", tablefmt="grid")

    # Apply color to the headers (e.g., blue = '34')
    colored_table = color_table_headers(table, color_code)  # 34 is the color code for blue

    print(colored_table)


def get_user_ip():
    # Отримує IP-адресу користувача за допомогою API ipify
    try:
        ip_response = requests.get("https://api.ipify.org?format=json")
        ip_response.raise_for_status()
        ip_data = ip_response.json()
        return ip_data.get("ip", "")
    except requests.RequestException as e:
        print(f"Error getting IP address: {e}")
        return None

def record_history(historyClass, url, method, result):
       # Записуємо історію запиту
       timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
       historyClass.history.append({
           "timestamp": timestamp,
           "url": url,
           "method": method,
           "result": result
       })

def printHistory(historyClass):
    if not historyClass.history:
        print("No history available.")
    else:
        for record in historyClass.history:
            print(f"Timestamp: {record['timestamp']}, URL: {record['url']}, Result: {record['result']}")

def askToSave(data):
    print("Would you like to save the data?")
    print("1: Save as JSON")
    print("2: Save as CSV")
    print("3: Save as TXT")
    print("4: Skip saving")

    choice = input("Enter your choice (1, 2, 3, or 4): ").strip()

    match choice:
        case "1":
            save_context = SaveContext(SaveJSON())
            save_context.save_data(data, "data.json")
            print("Data saved as JSON.")
        case "2":
            save_context = SaveContext(SaveCSV())
            save_context.save_data(data, "data.csv")
            print("Data saved as CSV.")
        case "3":
            save_context = SaveContext(SaveTXT())
            save_context.save_data(data, "data.txt")
            print("Data saved as TXT.")
        case "4":
            print("Data not saved.")
        case _:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")