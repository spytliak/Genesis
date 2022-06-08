### Tasks for create scripts

1. Дано 3 отрезка, длина которых a, b и c соответственно (вводится с консоли).
Требуется написать программу, которая проверяет, можно ли составить из данных отрезков треугольник и если треугольник получится, указать его тип (равносторонний, равнобедренный, прямоугольный или разносторонний)
Обязательно в решении использовать функции.

2. Написать скрипт, который будет выводить в консоль текущую погоду для Вашего населённого пункта (или ближайшего, если вашего нет в базе сервиса).
Для получения погоды использовать API https://openweathermap.org/api

 
 * [classify_triangles.py](/DevOps_School/Python/classify_triangles.py) - The script checks the possibility of making a triangle of the given segments, and if the triangle is successful, it will show the type.  
 * [requirements.txt](/DevOps_School/Python/requirements.txt)           - The packages that the weather_forecast.py script requires  
 * [weather_forecast.py](/DevOps_School/Python/weather_forecast.py)     - The script shows the current weather forecast for your city. For script need to install the library [pyown](https://pyowm.readthedocs.io/en/latest/index.html), which works with API https://openweathermap.org/api, and export the environment variable APIID (API key) in your env. Example for linux is below:  
 ```
 export APIID=ca21196f733dbc96062304d5d79aa777
 ```

 #### Examples
Output of classify_triangles.py  
```
$ python classify_triangles.py 
Please enter the length of the sides:
a = 2
b = 3
c = 2
The triangle is an Isosceles
```

Outputs of weather_forecast.py:  
```
$ python weather_forecast.py 
Please enter a city: kyiv
The weather in the KYIV is: 
temperature: 27.59 °C
wind: 2.68 m/s
humidity: 24 %
```
```
$ python weather_forecast.py london
The weather in the LONDON is: 
temperature: 21.19 °C
wind: 7.72 m/s
humidity: 48 %
```