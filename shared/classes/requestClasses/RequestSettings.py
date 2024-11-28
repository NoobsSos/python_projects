from shared.functions.httpFunctions import get_user_ip
from shared.functions.errorFunctions import isValidUrl

class RequestSettings:
    # Доступні API
    availableAPI = [
        {"1": "Рандомний користувач: https://randomuser.me/api/"},
        {"2": "Жарти програмістів: https://official-joke-api.appspot.com/jokes/programming/ten"},
        {"3": "Інформація про ваш IP: https://ipinfo.io/{}/geo"}
    ]
    availableColors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

    def __init__(self):
        self.url = self.availableAPI[1]["2"].split(": ")[1]
        self.method = "get"
        self.header_color = 31
        self.history = []

    def setUrl(self):
        print("Available APIs:")
        for idx, api in enumerate(self.availableAPI, start=1):
            for key, url in api.items():
                print(f"{idx}: {key} {url}")

        choice = input("Choose 1, 2, 3 for predefined options, or 4 to enter a custom URL: ")

        if choice == "4":
            custom_url = input("Please enter your custom URL: ").strip()
            if isValidUrl(custom_url):
                self.url = custom_url
                print(f"Custom URL set to: {self.url}")
                return True
            else:
                print("Invalid URL format. Please enter a valid URL.")
                return False

        for api in self.availableAPI:
            if choice in api:
                if choice == "3":
                    user_ip = get_user_ip()  # Забираємо IP користувача
                    self.url = api[choice].split(": ")[1].format(user_ip)
                else:
                    self.url = api[choice].split(": ")[1]
                print(f"URL set to: {self.url}")
                return True

        print("Invalid choice. Please choose between 1, 2, 3, or 4.")
        return False

    def changeColor(self):
        print(self.availableColors)
        header_color = input("Enter header_color")
        if header_color in self.availableColors:
            match header_color:
                case 'black':
                    self.header_color = 30
                case 'red':
                    self.header_color = 31
                case 'green':
                    self.header_color = 32
                case 'yellow':
                    self.header_color = 33
                case 'blue':
                    self.header_color = 34
                case 'magenta':
                    self.header_color = 35
                case 'cyan':
                    self.header_color = 36
                case 'white':
                    self.header_color = 37

        else:
            self.header_color = 30

