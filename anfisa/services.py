import requests


def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text.strip()
    else:
        return '<ошибка на сервере погоды. попробуйте позже>'

def what_temperature(weather):    
    if (weather == '<сетевая ошибка>' or
        weather == '<ошибка на сервере погоды. попробуйте позже>'):
        return weather
    temperature = weather.split()[1]
    parsed_temperature = ''
    for char in temperature:
        if char == '-':
            parsed_temperature += char
        try:
            num = int(char)
            parsed_temperature += char
        except ValueError:
            continue
    return parsed_temperature

def what_conclusion(parsed_temperature):
    try:
        temperature = int(parsed_temperature)
        
        if temperature < 18:
            return f'На улмце холодно, подумай о своих близких!'
        elif 18 <= temperature <= 27:
            return f'Морожка сейчас прям в самый раз! Порадуй себя '
        else:
            return f'Жарко, забирай все что есть а то не успеешь!:) '
       
    except ValueError:
        return f'Не могу узнать погоду...'

