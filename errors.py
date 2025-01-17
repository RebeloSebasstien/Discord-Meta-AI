
class AIParseError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
    
class APIError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message