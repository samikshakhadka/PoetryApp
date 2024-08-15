import os
from celery import shared_task
from django.core.mail import send_mail
from .models import CustomUser
import logging
from django.conf import settings
from django.urls import reverse

@shared_task
def send_verification_email_task(user_id):
    logger = logging.getLogger(__name__)
    try:
        logger.info(f"EMAIL_HOST: {os.environ.get('EMAIL_HOST')}")
        user = CustomUser.objects.get(id=user_id)
        verification_url = f"{settings.SITE_URL}{reverse('verify-email', args=[user.verification_token])}"
        send_mail(
            'Verify your email',
            f'Please verify your email by clicking on the following link: {verification_url}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
        logger.info(f"Verification email sent to {user.email}")
    except Exception as e:
        logger.error(f"Error sending verification email: {e}")



