# Backend-часть для проекта Firstclass
## О проекте
Программа позволяет принимать заявки и отправлять подтверждение на электронную почту или по SMS.

## Запуск
Клонируйте репозиторий и войдите в папку проекта
```bash
https://github.com/AliakseiYafremau/FirstClass
cd BackEnd/back
```
Создайте виртуальное окружение и установите зависимости
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Примените миграции и запустите сервер
```bash
python manage.py migrate
python manage.py runserver
```

## Настройка отправки сообщения
1. Создаем в корневой папке файл .env.
2. Входим в google-аккаунт -> Безопасность -> Пароли приложений. Создаем пароль приложения.
3. Записываем в файл .env ключи:
   * ACCOUNT_NAME=ваша_почта_до_@gmail.com
   * ACCOUNT_PASSWORD=пароль_вашего_приложения
4. Для того чтобы проверить корректность отправки почты, используйте команду ```py manage.py test rest_api.tests```