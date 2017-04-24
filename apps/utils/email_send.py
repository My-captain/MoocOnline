# _*_ encoding:utf-8_*_
from random import Random
from django.core.mail import send_mail
from users.models import EmailVerifyRecord
from MoocOnline.settings import EMAIL_FROM


def random_str(randomlength=8):
    str = ''
    chars = 'ABCDEFGHYJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0,length)]
    return str


def send_register_email(email, send_type):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""
    if send_type == "register":
        email_title = "慕课网--刘少个人项目  用户注册激活链接"
        email_body = "尊敬的用户:" \
                     "      感谢您注册使用刘少的慕课在线学习网，请点击以下链接激活您的账号:" \
                     "http://10.120.52.198:8000/active/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "慕课网--刘少个人项目  用户密码重置链接"
        email_body = "尊敬的用户：" \
                     "      请点击一下链接重置您的密码:" \
                     "http://10.120.52.198:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
