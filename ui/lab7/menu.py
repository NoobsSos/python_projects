from shared.functions.httpFunctions import displayData, record_history, askToSave

from classes.requestClasses.RequestSettings import RequestSettings
from classes.requestClasses.APIRequestFactory import APIRequestFactory

from ui.lab7.settings_menu import settingsMenu


def menu():
    settings = RequestSettings()
    APIFactory = APIRequestFactory(settings)
    while True:
        print("1. Use requests")
        print("2. Requests settings")
        print("3. Exit")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                request = APIFactory.create_request(APIFactory)
                data = request.send()
                record_history(settings, settings.url, settings.method, data)
                displayData(data, settings.header_color)

                askToSave(data)
            case "2":
                settingsMenu(settings)
            case _:
                break