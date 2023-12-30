from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ContactMessage

class SendEmailAPIView(APIView):
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        email = request.data.get('email')
        message_text = request.data.get('message')

        ContactMessage.objects.create(name=name, email=email, message=message_text)

        return Response({"message": "Your message has been received. Thank you!"}, status=status.HTTP_200_OK)
