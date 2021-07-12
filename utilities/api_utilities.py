from datetime import datetime


class Message:

    @classmethod
    def error(self, request, message, **kwargs):
        now = datetime.now()
        dic = {
            'error': message,
            'method': request.method,
            'date': now.strftime('%Y/%m/%d - %H:%M:%S'),
            **kwargs,
        }

        return dic

    @classmethod
    def message(self, request, subject, message, **kwargs):
        now = datetime.now()
        dic = {
            f'{subject}': message,
            'method': request.method,
            'date': now.strftime('%Y/%m/%d - %H:%M:%S'),
            **kwargs,
        }

        return dic
