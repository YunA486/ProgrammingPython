class InvalidCountError(Exception):
    def __init__(self, message):
        super().__init__(message)       # super().__init__("3자리 숫자가 아닙니다.")