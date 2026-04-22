import messages

name = input(messages.MSG_INPUT_NAME).strip()

if name.isalpha():
    name = name.title()
    print(messages.MSG_NAME_OK.format(name=name))

age = input(messages.MSG_INPUT_AGE).strip().strip("0")

if age.isdigit():
    print(messages.MSG_AGE_OK.format(age=age))

phone = input(messages.MSG_INPUT_PHONE).strip()

if phone.isdigit():
    print(messages.MSG_PHONE_OK.format(phone=phone))

print(messages.MSG_FINISH)