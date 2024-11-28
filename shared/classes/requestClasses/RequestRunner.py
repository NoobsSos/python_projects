from shared.functions.httpFunctions import displayData, record_history, askToSave

from shared.classes.requestClasses.RequestSettings import RequestSettings
from shared.classes.requestClasses.APIRequestFactory import APIRequestFactory


from ui.MenuItem import MenuItem
from ui.MenuBuilder import MenuBuilder


class RequestRunner:

    def menu(self):
        settings = RequestSettings()
        APIFactory = APIRequestFactory(settings)

        def use_requests():
            request = APIFactory.create_request(APIFactory)
            data = request.send()
            record_history(settings, settings.url, settings.method, data)
            displayData(data, settings.header_color)
            askToSave(data)

        menu_items = [
            MenuItem("1", "Use Requests", use_requests),
            MenuItem("2", "Requests Settings", use_requests),
            MenuItem("0", "Exit", exit),
        ]

        menu_builder = MenuBuilder(menu_items)
        while True:
            menu_builder.initialize()
