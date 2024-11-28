import logging

class Logger:
    @staticmethod
    def setup_logger():
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            filename='app.log',  # Ім'я файлу для логування
            filemode='w'  # 'w' - перезаписувати файл, 'a' - додавати нові записи
        )

    def log(message):
        logging.info(message)