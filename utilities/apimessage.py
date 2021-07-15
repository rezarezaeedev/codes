from datetime import datetime


class Message:

    @classmethod
    def error(self, request, message, **kwargs) ->dict :
        now = datetime.now()
        dic = {
            'message': message,
            'method': request.method,
            'date': now.strftime('%Y/%m/%d - %H:%M:%S'),
            **kwargs,
        }

        return dic

    @classmethod
    def message(self, request, message:dict, **kwargs) ->dict:
        now = datetime.now()
        dic = {
            **message,
            'method': request.method,
            'date': now.strftime('%Y/%m/%d - %H:%M:%S'),
            **kwargs,
        }

        return dic

    @classmethod
    def found_data(self, request, data:"list|tuple", **kwargs) ->dict:
 
        now = datetime.now()
        dic = {
            f'message': f'found {len(data)} successfully',
            'method': request.method,
            'date': now.strftime('%Y/%m/%d - %H:%M:%S'),
            "data": data,
            **kwargs,
        }

        return dic

    @classmethod
    def found(self, request, data:dict,   **kwargs)  :
        '''
        use when founded a record object
        '''
        now = datetime.now()
        dic = {
            f'message': f'Data found successfully',
            'method': request.method,
            'date': now.strftime('%Y/%m/%d - %H:%M:%S'),
            "data":data,
            **kwargs,
        }

        return dic

    @classmethod
    def created(self, request, data:dict,   **kwargs)  :
        '''
        use when create a record object
        '''
        now = datetime.now()
        dic = {
            f'message': f'Object created successfuly',
            'method': request.method,
            'date': now.strftime('%Y/%m/%d - %H:%M:%S'),
            "data":data,
            **kwargs,
        }

        return dic

    @classmethod
    def updated(self, request, data:dict,   **kwargs)  :
        '''
        use when change a record object
        '''
        now = datetime.now()
        dic = {
            f'message': f'Object changed successfuly',
            'method': request.method,
            'date': now.strftime('%Y/%m/%d - %H:%M:%S'),
            "data":data,
            **kwargs,
        }

        return dic

    @classmethod
    def deleted(self, request, data:dict,   **kwargs)  :
        '''
        use when delete a record object
        '''
        now = datetime.now()
        dic = {
            f'message': f'Object deleted successfuly',
            'method': request.method,
            'date': now.strftime('%Y/%m/%d - %H:%M:%S'),
            "data":data,
            **kwargs,
        }

        return dic


