import utils


def main():
    utils.send_email(
        recipients=['dkushnir2012@ukr.net'],
        mail_body='this is mail body <br> another line',
        mail_subject='Test data',
    )


main()