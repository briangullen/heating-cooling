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
