# Write your solution here
list = []

while True:
    item = int(input("New Item:"))
    if item == 0:
        print("Bye!")
        break
    else:
        list.append(item)
        print("The list now:", list)
        print("The list in order:", sorted(list))
