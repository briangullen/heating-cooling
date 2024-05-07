def heating_cooling(actual_temp: int, desired_temp: int):
    print(f'Current temp {actual_temp}')
    print(f'Desired temp {desired_temp}')
    if actual_temp < desired_temp:
        action = 'Run heat'
    elif actual_temp > desired_temp:
        action = 'Run A/C'
    else:
        action = 'Standby'
    return print(action)


current_temp = int(input('What is the current temperature? '))
ideal_temp = int(input('What is your desired temperature? '))
heating_cooling(current_temp, ideal_temp)


def convert_temp(temp_celsius: float, target_unit: str):
    match target_unit:
        case "K":
            print('Converting to Kelvin')
            temp_converted = temp_celsius + 273.15
        case "F":
            print('Converting to Fahrenheit')
            temp_converted = (temp_celsius * 1.8) + 32
        case "C":
            print('No conversion needed.')
            temp_converted = temp_celsius
        case _:
            print('Sorry you did not enter a valid Temperature unit.')
    return print(f'The converted temperature is: {temp_converted} {target_unit}')


current_celsius = float(input(f'What is the temperature in Celsius? '))
desired_unit = str(input('What unit do you want the temperature converted to? (C, F or K): ').upper())
convert_temp(current_celsius, desired_unit)
