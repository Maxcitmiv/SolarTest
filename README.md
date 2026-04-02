## Проект UI автотестов `rt-solar.ru`

### Используемые технологии
<p align="center">
  <code><img width="5%" title="PyCharm" src="images/logo_stacks/pycharm.svg"></code>
  <code><img width="5%" title="Python" src="images/logo_stacks/python.svg"></code>
  <code><img width="5%" title="Pytest" src="images/logo_stacks/pytest.svg"></code>
  <code><img width="5%" title="Selene" src="images/logo_stacks/selene.svg"></code>
  <code><img width="5%" title="Selenium" src="images/logo_stacks/selenium.svg"></code>
  <code><img width="5%" title="GitHub" src="images/logo_stacks/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo_stacks/jenkins.svg"></code>
  <code><img width="5%" title="Selenoid" src="images/logo_stacks/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo_stacks/allure.svg"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo_stacks/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/logo_stacks/jira.svg"></code>
  <code><img width="5%" title="Telegram" src="images/logo_stacks/telegram.png"></code>
</p>

### Что проверяем
* Поиск в хедере и переход на страницу поиска
* Открытие формы консультации и наличие обязательных полей
* Автодополнение поля компании (пример: `ПАО СБЕРБАНК`)
* Переход на страницу аналитики из хедера
* Выбор продукта и проверка открытия промо-формы

### Подготовка и запуск
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
```

`.env` (в корне проекта):
```env
LOGIN=your_selenoid_login
PASSWORD=your_selenoid_password
```

### <img width="3%" title="Jenkins" src="images/logo_stacks/jenkins.svg"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/autotes11/)

##### При нажатии на "Build Now" запускается сборка и прогон UI-тестов в удаленном браузере через Selenoid.
![Jenkins Job](images/screenshots/jenkins_job.png)

### <img width="3%" title="Allure Report" src="images/logo_stacks/allure.svg"> Allure report

### [Allure report build #19](https://jenkins.autotests.cloud/job/autotes11/19/allure/)

##### В отчете доступны шаги теста, вложения (screenshot, page source, console log) и ссылка на видео прогона.
![Allure Report](images/screenshots/allure_report.png)

### <img width="3%" title="Allure TestOps" src="images/logo_stacks/allure_testops.png"> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/5159/dashboards)

##### Результаты прогонов сохраняются в Allure TestOps с дашбордами по тест-кейсам, автотестам и запускам.
![Allure TestOps Dashboard](images/screenshots/allure_testops_dashboard.png)

### <img width="3%" title="Jira" src="images/logo_stacks/jira.svg"> Интеграция с Jira

##### Через интеграцию можно связывать автотесты и результаты прогонов с задачами в Jira.
![Jira Task](images/screenshots/jira_issue.png)

### <img width="3%" title="Telegram" src="images/logo_stacks/telegram.png"> Интеграция с Telegram

##### После завершения прогона бот отправляет краткий отчет с итогами и ссылкой на Allure.
![Telegram Notification](images/screenshots/telegram_notification.png)

### Видео прогона теста

<video src="images/video/test_search_company.mp4" controls width="100%"></video>

Если в вашей среде превью не отображается, файл доступен по ссылке:
[test_search_company.mp4](images/video/test_search_company.mp4)

### Примечание
Иконки сохранены локально в `images/logo_stacks/` (часть из Devicon, часть из официальных ресурсов GitHub, Allure, Qameta и Selenoid).
Скриншоты и видео тоже лежат в репозитории (в `images/`), поэтому README не зависит от внешних CDN.
