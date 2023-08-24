
phone_book = {}

while True:
    command = input("1 search, 2 add, 3 quit")

    if command == "1":
      name = input("name: ")
      if name not in phone_book:
        print("no number")
      else:
        print(phone_book[name])

    elif command == "2":
      name = input("name: ")
      number = input("number: ")
      phone_book[name] = number
      print("ok!")

    elif command == "3":
      print("quitting...")
      break

    else:
      print("invalid command")






