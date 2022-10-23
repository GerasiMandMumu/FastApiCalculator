# FastApiCalculator

Простейший калькулятор в виде REST-сервиса.

Запуск:

git clone https://github.com/GerasiMandMumu/FastApiCalculator.git

docker build -t image .

docker run -d --name mycontainer -p 80:80 image

Примеры
http://127.0.0.1:8000/eval?phrase=1%2B1

http://127.0.0.1:8000/eval?phrase=2*(3%2B7)/5
