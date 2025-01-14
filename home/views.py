from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from . utils import GetResponse, send_gmail
from . models import UserComment


# Create your views here.

class GeminiSearchView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        query = request.data.get('query')
        if (len(str(query)) < 2):
            return Response({'message': "Ask something.."}, status=status.HTTP_204_NO_CONTENT)
        res = GetResponse(query, request)
        return Response({"message":res}, status=status.HTTP_200_OK)
    
class UserFeedbackView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        name = request.data.get('name')
        comment = request.data.get('comment')

        feedback = UserComment.objects.create(
            name = name,
            email= email, 
            comment = comment,
        )
        feedback.save()

        subject = "Thank you for your feedback."
        body = f"Thank you for your valuable feedback {name}"

        send_gmail(request, to_email=email, subject=subject, body=body)

        return Response({'message':'Your feedback is received'}, status=status.HTTP_200_OK)