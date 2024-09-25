# glowbyte-iris
### № 1
#### Задача
Обучить модель для предсказания цветка ириса на данных датасета [iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html). Разработать REST сервис с использованием библиотеки `FastAPI`, который по переданным параметрам цветка будет возвращать предсказанное `species`.
#### Решение
Обучение и сохранение модели вы можете найти в файле `notebooks/iris_classification.ipynb`.

REST сервис на FastAPI вы можете найти в файле `app/main.py`. Подгружается сохраненная модель и затем используется в методе, который обрабатывает endpoint `/predict/`.  

### № 2
#### Задача
Разработанный сервис поднять как docker контейнер. Созданный docker образ загрузить на [hub.docker.com](https://hub.docker.com/).
#### Решение
`Dockerfile` вы можете найти в главной папке репозитория.

Образ вы можете найти по [ссылке](https://hub.docker.com/repository/docker/abdullinilgiz/iris/general).
```bash
sudo docker image pull abdullinilgiz/iris
```
Чтобы запустить образ выполните:
```bash
docker run -d --name iris-container 8000:8000 abdullinilgiz/iris
```
### Время
Оцените время, которое вам потребуется на выполнение заданий и вышлите свою оценку ответным письмом.

Задание было получено и даны разъеснения 23.09.2024 16:25.
Завершил задание 25.09.2024.