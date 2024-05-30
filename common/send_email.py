import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(sender_email, receiver_email, subject, body, email_password, smtp_server='smtp.qq.com',
               port=465, attachments=None):
    """
    发送带有附件的电子邮件。

    :param sender_email: 发送者电子邮件地址
    :param receiver_email: 接收者电子邮件地址
    :param subject: 邮件主题
    :param body: 邮件正文
    :param attachments: 附件文件路径的列表
    :param smtp_server: SMTP服务器地址,默认qq邮箱
    :param port: SMTP服务端口
    :param email_password: 发送者邮箱的密码
    """
    # 创建一个多部分消息
    message = MIMEMultipart("mixed")

    # 添加邮件正文
    text_part = MIMEText(body, "plain")
    message.attach(text_part)
    # 如果您想在邮件中嵌入图片，需要按以下步骤操作：

    # 添加邮件主题
    message["Subject"] = subject
    message["From"] = sender_email
    if isinstance(receiver_email, str):
        receiver_email = [receiver_email]
    message["To"] = ','.join(receiver_email)

    # 遍历附件列表，添加每个附件
    if attachments:
        for file_path in attachments:
            # 确保文件存在
            if os.path.isfile(file_path):
                with open(file_path, "rb") as attachment:
                    # 创建MIMEApplication对象
                    part = MIMEApplication(attachment.read(), Name=os.path.basename(file_path))
                    part['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(file_path)

                # 添加附件到消息
                message.attach(part)
            else:
                print(f"文件 {file_path} 不存在，跳过附件。")

    # 发送邮件
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, email_password)
        server.sendmail(sender_email, receiver_email, message.as_string())


# 示例使用
if __name__ == "__main__":
    receiver_email = ['wuggfox@foxmail.com', '424434104@qq.com']
    send_email(
        sender_email="wuggfox@foxmail.com",
        receiver_email=receiver_email,
        subject="带有附件的邮件",
        body="这是邮件正文。",
        attachments=[],
        smtp_server="smtp.qq.com",
        port=465,
        email_password="gqqzbwyedhjpbeef"
    )
