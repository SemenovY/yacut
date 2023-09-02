# **YaCut - Link shortening service**
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/-Scrapy-464646?style=flat&logo=Scrapy&logoColor=ffffff&color=043A6B)](https://scrapy.org/)
[![XPath](https://img.shields.io/badge/-XPath-464646?style=flat&logo=XPath&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![CSS](https://img.shields.io/badge/-CSS-464646?style=flat&logo=CSS&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/-Pytest-464646?style=flat&logo=Pytest&logoColor=ffffff&color=043A6B)](https://www.python.org/)
________


The YaCut project is a link shortening service. Its purpose is to associate a long user link with a short link that is offered by the user or provided by the service.

**An API has also been written for the project**
##Project Technologies

* Python — a high-level programming language.
* Flask — is a framework for creating web applications in the Python programming language, using the Werkzeug toolkit and the Jinja2 templating engine. It belongs to the category of so-called microframeworks - minimalistic web application frameworks that deliberately provide only the most basic features.

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
***The following worked on the project:***
* Yuriy Semenov | GitHub: [SemenovY](https://github.com/SemenovY) | Python developer.

### *Free Software, Not for commercial use!*
### =^..^=______/
