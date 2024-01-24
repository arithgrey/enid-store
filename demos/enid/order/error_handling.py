from rest_framework import status

class ErrorResponse:
    @staticmethod
    def handle_exception(e):
        return {"error": str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR