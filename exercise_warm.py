user_input = float(input ("Insert temperature: "))
def weather_condition(temperature):
    if temperature >= 7:
        return "Warm"
    else: 
        return "Cold"
print(weather_condition(user_input))
