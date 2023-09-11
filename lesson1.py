import requests
import datetime

# url api с параметрами
urlWeather = "https://api.open-meteo.com/v1/forecast?"
urlGeocoding = "https://geocoding-api.open-meteo.com/v1/search?name="

yesSeriesDays = 1
startDate = datetime.date.today()
endDate = startDate

while True:
    # точка входа
    what = input("""\nВыберите вариант:
    Найти координаты вашего города? Введите 1
    Найти погоду по координатам города? Введите 2
    Найти погоду по названию города? Введите 3
    Найти погоду за вчера, указав город? Введите 4
    Найти когда восход и заход солнца в городе? Введите 5
    Выйти из программы? Введите 0""")

    if what == "1":
        city = input("Введите город на англ., Пример: Moscow, Berlin")
            # url api с параметрами
        resUrlGeocoding = urlGeocoding+city
            # запрашиваем ответ в JSON
        Geocoding = requests.get(resUrlGeocoding).json()
            # из JSON получаем Широту и Долготу
        valueLatitude = Geocoding["results"][0]["latitude"]
        valueLongitude = Geocoding["results"][0]["longitude"]
        print("\nКоординаты вашего города\n", "Широта: ", valueLatitude, "\nДолгота: ", valueLongitude)

    if what == "2":
        valueLatitude = input("Введите широту: ")
        valueLongitude = input("Введите долготу: ")
        yesSeriesDays = input("\nЗа сколько дней вывести погоду? Введите от 1 до 16")
        weatherYourCity = urlWeather + f"latitude={valueLatitude}" + "&" + f"longitude={valueLongitude}" + "&hourly=temperature_2m" + f"&forecast_days={yesSeriesDays}"
        reqWeatherYourCity = requests.get(weatherYourCity).json()
        # из JSON получаем Дату и Температуру
        dataYourCity = reqWeatherYourCity["hourly"]["time"]
        tempYourCity = reqWeatherYourCity["hourly"]["temperature_2m"]
        # формируем красивый вывод погоды на сегодня
        compilationDataTemp = []
        for d, t in zip(dataYourCity, tempYourCity):
            res = (str(d) + " - " + str(t) + " °C")
            compilationDataTemp.append(res)
        print("\nПогода по заданным координатам:\n", *compilationDataTemp, sep="\n")

    if what == "3":
        city = input("Введите город на англ., Пример: Moscow, Berlin")
        # url api с параметрами
        resUrlGeocoding = urlGeocoding + city
        # запрашиваем ответ в JSON
        Geocoding = requests.get(resUrlGeocoding).json()
        # из JSON получаем Широту и Долготу
        valueLatitude = Geocoding["results"][0]["latitude"]
        valueLongitude = Geocoding["results"][0]["longitude"]
        yesSeriesDays = input("\nЗа сколько дней вывести погоду? Введите от 1 до 16")
        weatherYourCity = urlWeather + f"latitude={valueLatitude}" + "&" + f"longitude={valueLongitude}" + "&hourly=temperature_2m" + f"&forecast_days={yesSeriesDays}"
        reqWeatherYourCity = requests.get(weatherYourCity).json()
        # из JSON получаем Дату и Температуру
        dataYourCity = reqWeatherYourCity["hourly"]["time"]
        tempYourCity = reqWeatherYourCity["hourly"]["temperature_2m"]
        # формируем красивый вывод погоды на сегодня
        compilationDataTemp = []
        for d, t in zip(dataYourCity, tempYourCity):
            res = (str(d) + " - " + str(t) + " °C")
            compilationDataTemp.append(res)
        print("\nПогода в вашем городе:\n", *compilationDataTemp, sep="\n")

    if what == "4":
        city = input("Введите город на англ., Пример: Moscow, Berlin")
        # url api с параметрами
        resUrlGeocoding = urlGeocoding + city
        # запрашиваем ответ в JSON
        Geocoding = requests.get(resUrlGeocoding).json()
        # из JSON получаем Широту и Долготу
        valueLatitude = Geocoding["results"][0]["latitude"]
        valueLongitude = Geocoding["results"][0]["longitude"]

        weatherYourCity = urlWeather + f"latitude={valueLatitude}" + "&" + f"longitude={valueLongitude}" + "&hourly=temperature_2m" + "&past_days=1" + "&forecast_days=0"
        reqWeatherYourCity = requests.get(weatherYourCity).json()
        print(reqWeatherYourCity)
        # из JSON получаем Дату и Температуру
        dataYourCity = reqWeatherYourCity["hourly"]["time"]
        tempYourCity = reqWeatherYourCity["hourly"]["temperature_2m"]
        # формируем красивый вывод погоды на сегодня
        compilationDataTemp = []
        for d, t in zip(dataYourCity, tempYourCity):
            res = (str(d) + " - " + str(t) + " °C")
            compilationDataTemp.append(res)
        print("\nВчера было :\n", *compilationDataTemp, sep="\n")

    if what == "5":
        city = input("Введите город на англ., Пример: Moscow, Berlin")
        chooseDay = input("На сегодня узнать или на другую дату? Введите Сегодня или Другая")
        if chooseDay == "Сегодня":
            pass
        else:
            startDate = input("Укажите желаемую дату. Введите в формете YYYY-MM-DD")
            endDate = startDate
        # url api с параметрами
        resUrlGeocoding = urlGeocoding + city
        # запрашиваем ответ в JSON
        Geocoding = requests.get(resUrlGeocoding).json()
        # из JSON получаем Широту и Долготу
        valueLatitude = Geocoding["results"][0]["latitude"]
        valueLongitude = Geocoding["results"][0]["longitude"]
        weatherYourCity = urlWeather + f"latitude={valueLatitude}" + "&" + f"longitude={valueLongitude}" + "&daily=sunset,sunrise" + "&forecast_days=0" +"&timezone=auto" + f"&start_date={startDate}" + f"&end_date={endDate}"
        reqWeatherYourCity = requests.get(weatherYourCity).json()
        valueSunset = reqWeatherYourCity["daily"]["sunset"]
        valueSunrise = reqWeatherYourCity["daily"]["sunrise"]

        for a in valueSunset:
            print(f"Заход в вашем городе, в это время - {a[-4:]}")
        for b in valueSunrise:
            print(f"Восход в вашем городе, в это время - {b[-4:]}")

    if what == "0":
        break
