from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_order_status_mail(order_id,order_status,email):
    if order_status == "confirmed":
        subject="Your order is confirmed"
        message = "order is confirmed"
    else:
        subject = "order status changed"
        message=f"your order is ${order_status}"
    send_mail(subject,message,"from@gmail.com",[email])    