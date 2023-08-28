# **YaCut - Link shortening service**
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
________


Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

**Для проекта также написан API**
## Технологии проекта

* Python — высокоуровневый язык программирования.
* Flask — фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2. Относится к категории так называемых микрофреймворков — минималистичных каркасов веб-приложений, сознательно предоставляющих лишь самые базовые возможности.

## **How to start a project**:

* Clone a repository and change to it on the command line:
```
git clone git@github.com:SemenovY/yacut

```

* Create and activate virtual environment:
```
python3 -m venv venv

source venv/Scripts/activate
```

* Install dependencies from a file requirements.txt:
```
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

* Create an .env file in the root directory with the following variables:
```
FLASK_APP=yacut
FLASK_ENV=development или production
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=<ваш_секретный_ключ>
```

* Launch the application:
```
flask run
```
_____________
Creator: Семёнов Юрий -> GitHub: [SemenovY](https://github.com/SemenovY)
