import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from my_logging import Logger
from setup import configs


def send_email(
    sender: str,
    mail_host: str,
    mail_pass,
    receivers: list[str],
    msg: str,
    attach_files: list[str] = [],
    subject: str = "新通知",
    from_name: str = "BLS-BOT",
    to_name: str = "绅士さん",
) -> bool:
    """发送邮件

    Args:
        sender (str): 发件人邮箱
        mail_host (str): SMTP邮箱域名
        mail_pass (_type_): 邮箱密码/授权码
        receivers (list[str]): 接收人邮箱，列表格式
        msg (str): 邮件信息,支持HTML
        attach_files (list[str], optional): 附件路径. Defaults to [].
        subject (str, optional): _description_. Defaults to "新通知".
        from_header (str, optional): 发件人称呼. Defaults to "BLS-Bot".
        to_header (str, optional): 收件人称呼. Defaults to "绅士さん".

    Returns:
        bool: _description_
    """

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message["From"] = Header(f"{from_name} <{sender}>")
    message["To"] = Header(to_name, "utf-8")
    message["Subject"] = Header(subject, "utf-8")

    print(message)
    # 邮件正文内容
    message.attach(MIMEText(msg, "html", "utf-8"))

    if len(attach_files) != 0:
        # 循环添加附件
        for file in attach_files:
            # 构造附件，传送指定的文件
            att = MIMEText(open(file, "rb").read(), "base64", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            # filename为邮件中显示的名字
            att["Content-Disposition"] = 'attachment; filename="test.txt"'
            message.attach(att)

    logger = Logger("email")
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host)
        smtpObj.login(sender, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        logger.log(f"邮件发送成功! sender:{sender},[{','.join(receivers)}],{subject}")
        return True
    except smtplib.SMTPException as e:
        logger.error(f"邮件发送失败! sender:{sender},[{','.join(receivers)}],{subject},{e}")
        e.with_traceback()
        return False


if __name__ == "__main__":
    send_email(
        configs["email"]["sender"],
        configs["email"]["mail_host"],
        configs["email"]["mail_pass"],
        [],
        """
    <div class="container">
        <h1>404</h1>
        <p>Sorry, the page you requested could not be found.会不会乱码</p>
        <button onclick="history.go(-1)">Go Back</button>
        <div style="height: 200px;"></div>
    </div>
        """,
    )
