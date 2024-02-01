class ErrorResponse:
    @staticmethod
    def handle_exception(e):
        return {"error": str(e)}