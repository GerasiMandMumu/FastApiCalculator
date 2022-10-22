# FastApiCalculator

1. Реализовать в виде REST-сервиса простейший калькулятор, чтобы можно было передать строку выражения для вычисления как в Python через "eval", 
но НЕ используя эту функцию и вернуть результат. Например, строка выражения может быть такой: "2+2/2" или "2*(3+7)/5" и т.д.

2. Для GET-запроса по пути "/" или "/index", чтобы возвращал просто фразу "Hello world".

3. Для GET-запроса по пути "/eval", чтобы вычислял переданное через параметр (например "phrase") выражение и возвращал результат в полном виде: "выражение = результат". 
Например "2*(3+7)/5 = 4". Результат должен быть в виде обычной строки, с кодом возврата 200.

4. Для POST-запроса по пути "/eval", чтобы вычислял переданное в теле запроса так же через параметр (например "phrase") выражение и возвращал результат также в полном виде (см. п.3). 
Результат должен быть в формате JSON произвольной структуры на своё усмотрение, с кодом 201.

5. При ошибке вычисления переданного выражения возвращать описание ошибки, с кодом 400. Для GET-запроса возврат описания сообщения ошибки Python в виде строки. 
Для POST-запроса возврат описания сообщения ошибки Python в формате JSON, также произвольной структуры.

6. Сервис должен быть полностью асинхронным, например реализован на Tornado, aiohttp или FastAPI. Последний предпочтительно.

7. При объявлении передаваемых параметров функций, самих функций, свойств классов использовать типизацию, а также валидацию передаваемых в запросе данных.

8. Написать docker-файл для сборки проекта в docker-образ.

9. Выложить проект на GitHub и передать публичную ссылку на него.
