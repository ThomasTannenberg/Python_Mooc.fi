def suggest_clothing(temperature, will_rain):
    clothing_suggestion = "Wear jeans and a T-shirt"
    
    if temperature <= 5:
        clothing_suggestion += "\nI recommend a jumper as well"
        clothing_suggestion += "\nTake a jacket with you"
        clothing_suggestion += "\nMake it a warm coat, actually"
        clothing_suggestion += "\nI think gloves are in order"
    
    elif temperature <= 10:
        clothing_suggestion += "\nI recommend a jumper as well"
        clothing_suggestion += "\nTake a jacket with you"
    
    elif temperature <= 20:
        clothing_suggestion += "\nI recommend a jumper as well"
    
    if will_rain.lower() == "yes":
        clothing_suggestion += "\nDon't forget your umbrella!"
    
    return clothing_suggestion

def ask_user():
    print("What is the weather forecast for tomorrow?")
    temperature = int(input("Temperature: "))
    will_rain = input("Will it rain (yes/no): ")
    return temperature, will_rain

def main():
    temperature, will_rain = ask_user()
    suggestions = suggest_clothing(temperature, will_rain)
    print(suggestions)

main()





