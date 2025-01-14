import os
from dotenv import load_dotenv
from . models import UserQuery
import google.generativeai as genai
from django.core.mail import send_mail


load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def send_gmail(request, to_email, subject, body):
    send_mail(
            subject,
            body,
            'mail.slipwrite@gmail.com',
            [to_email,],
            fail_silently=True
        )


def compare_questions(query):
    queries = UserQuery.objects.filter(query=query).first()
    return queries


def GetResponse(query, request):
    if compare_questions(query):
        quer = UserQuery.objects.get(query = query)
        return quer.answer
    else:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(str(query))
        userquery = UserQuery.objects.create(user= request.user, query = query, answer=response.text, model = 'gemini-1.5-flash')
        userquery.save()
        return response.text