from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_template_mail(user_email, variable_dict, template_path, subject):
    subject = subject
    from_email = 'mail.slipwrite@gmail.com'
    to_email = [user_email]

    # Render the HTML template with context
    html_content = render_to_string(template_path, variable_dict)
    text_content = strip_tags(html_content)  # Fallback text for email clients that don’t support HTML

    # Create the email message
    email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email.attach_alternative(html_content, "text/html")  # Attach the HTML content
    email.send(fail_silently=False)

