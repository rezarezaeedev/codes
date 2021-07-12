from datetime import datetime


class Message:

    @classmethod
    def error(self, request, message, **kwargs):
        now = datetime.now()
        dic={
            'error': message,
            'method': request.method,
            'date': now.strftime('%Y/%m/%d - %H:%M:%S'),
            **kwargs,
            
        }
        return dic


    @classmethod
    def warning(self, request, message, **kwargs):
        now = datetime.now()
        dic={
            'warning': message,
            'method': request.method,
            'date': now.strftime('%Y/%m/%d - %H:%M:%S'),
            **kwargs,
            
        }
        return dic


    
