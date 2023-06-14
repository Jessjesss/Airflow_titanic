# Airflow_titanic

1. Создала директорию проекта airflow и перешла в нее

`mkdir airflow`

`cd airflow`

3. Скачала docker-compose.yaml файл

`curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.6.1/docker-compose.yaml'`

3. Создала директории:
- ./dags
- ./logs
- ./plugins

`mkdir -p ./dags ./logs ./plugins`

4. Создала файл .env с параметром AIRFLOW_UUID

`echo -e "AIRFLOW_UID=$(id -u)" > .env`

6. Инициализировала базу данных

`docker-compose up airflow-init`

8. Запустила Apache Airflow с помощью docker-compose

`docker-compose up`
# Описание DAG:
1. Скачивает датасет по ссылке с помощью Pandas
```python
  import pandas as pd
  df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
  df.to_csv("df.csv")
  ```
2. Группирует по классу 
```python
gr = df.groupby("Pclass").agg({"Survived": "mean"})
```

4. Сохраняет в файл
```python
gr.to_csv("output.csv")
```

Запустила titanic_dag, отработал успешно, без ошибок.

![airfow](https://github.com/Jessjesss/Airflow_titanic/assets/113085452/2f27bbe2-352b-4e92-a3a2-d8b15de30a26)

![ww](https://github.com/Jessjesss/Airflow_titanic/assets/113085452/19356000-a6d2-4d15-a0c4-3bd6b3d1bb97)

