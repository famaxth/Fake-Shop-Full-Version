import db

admin_id = 768779619  # ID администратора
token = "1300793798:AAEB9iG1h5S3iJ4TS0AFWfSEayb-EXxEnjo"  # Токен бота

db.init_db()
hello_text = db.return_hello()
information = db.return_information()


file_2 = open("call_center_edit.txt", "r")
support = file_2.read()

file_4 = open("name_shop.txt", "r")
name = file_4.read()

file_5 = open("qiwi_number.txt", "r")
qiwi = file_5.read()

file_6 = open("qiwi_token.txt", "r")
token_qiwi = file_6.read()

file_7 = open("bitcoin.txt", "r")
bitcoin = file_7.read()
