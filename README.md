## Автоматизация тестирования с помощью Selenium и Python

Финальный проект курса "Автоматизация тестирования с помощью Selenium и Python" (Stepik)


Чтобы запустить проект нужно клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AigulParamonova/selenium_project_stepik.git
```

```
cd selenium_project_stepik
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас Windows

    ```
    source venv/Scripts/activate
    ```

Обновить менеджер пакета pip

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Запустить тесты:

```
pytest -v test_main_page.py
pytest -v test_product_page.py
pytest -v --tb=line --language=en -m need_review (для ревью)
```

### Технологии:
- Python 3.10.5
- Pytest 7.1.3
- Selenium 4.4.3
- Git
