from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CalculatorAPIView(APIView):
    def post(self, request):
        try:
            # Extract numbers and operation from the request
            num1 = float(request.data.get('num1'))
            num2 = float(request.data.get('num2'))
            operation = request.data.get('operation')

            # Perform the operation
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    return Response({'error': 'Division by zero is not allowed.'}, status=status.HTTP_400_BAD_REQUEST)
                result = num1 / num2
            else:
                return Response({'error': 'Invalid operation. Use add, subtract, multiply, or divide.'}, status=status.HTTP_400_BAD_REQUEST)

            # Return the result
            return Response({'result': result}, status=status.HTTP_200_OK)
        except (TypeError, ValueError):
            return Response({'error': 'Invalid input. Please provide two numbers and an operation.'}, status=status.HTTP_400_BAD_REQUEST)
