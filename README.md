# Airflow_titanic

1. Создала директорию проекта airflow 
2. Скачала docker-compose.yaml файл

3. Создала директории:
- ./dags
- ./logs
- ./plugins
 
4. Создала файл .env с параметром AIRFLOW_UUID
5. Инициализировала базу данных
6. Запустила Apache Airflow с помощью docker-compose

# Описание DAG:
1. Скачивает датасет по ссылке с помощью Pandas
2. Группирует по классу 
3. Сохраняет в файл

![airfow](https://github.com/Jessjesss/Airflow_titanic/assets/113085452/2f27bbe2-352b-4e92-a3a2-d8b15de30a26)
