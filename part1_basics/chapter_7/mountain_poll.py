responses = {}

# 设置调查是否继续的标志
polling_active = True

while polling_active:  # 提示输入被调查者的名字和回答
    name = input('\nWhat is your name? ')
    response = input("Which mountain would you like to climb someday？ ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response + ".")
