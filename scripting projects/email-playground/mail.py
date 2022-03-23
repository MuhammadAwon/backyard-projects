'''Let's create a dynamic email service that allows to send different
files and attachments as requirement arises using built-in python modules'''

# import smtplib
# import imghdr
# from email.message import EmailMessage
# from string import Template
# from pathlib import Path


# email = EmailMessage()
# email['from'] = 'Awon08'
# email['to'] = 'awon195@gmail.com'
# email['subject'] = 'Image attached...'
# email_body = '''This is sent from Python'''

# html_text = Template(Path('index.html').read_text())
# email.set_content(html_text.substitute(name = email_body), 'html')

# images = ['pikachu.png', 'astro-thumbnail.png',
# 'blur-squirtle.png', 'grey-squirtle.png'
# ]

# for imgage in images:
#     with open(imgage, 'rb') as f:
#         file_data = f.read()
#         file_name = f.name
#         file_type = imghdr.what(f.name)

#     email.add_attachment(file_data, maintype='image', subtype='png', filename=file_name)

# with smtplib.SMTP('smtp.gmail.com', 587) as server:
#     server.ehlo()
#     server.starttls()
#     server.login('awon195@gmail.com', 'Gmail08.')
#     print('successfully logged in')
#     server.send_message(email)
#     print('message sent')
