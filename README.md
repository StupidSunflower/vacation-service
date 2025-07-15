# Сервис управления отпусками сотрудников

Микросервис для управления информацией об отпусках сотрудников через HTTP API.

## Технологии
- Python 3.10
- Django 4.0
- Django REST Framework
- PostgreSQL
- Docker

## Запуск сервиса

### Требования:
- Docker и Docker Compose

### Инструкция:
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-логин/ваш-репозиторий.git
   cd ваш-репозиторий
   ```

2. Запустите сервис:
   ```bash
   docker-compose up --build
   ```

3. После запуска сервис будет доступен по адресу:  
   http://localhost:8001/api/

## Документация API

### 1. Добавить отпуск
**Endpoint:** `POST /api/vacations/`  
**Тело запроса:**
```json
{
  "employee_id": 123,
  "start_date": "2023-07-01",
  "end_date": "2023-07-14"
}
```

**Успешный ответ (201 Created):**
```json
{
  "id": 1,
  "employee_id": 123,
  "start_date": "2023-07-01",
  "end_date": "2023-07-14"
}
```

### 2. Получить последние 3 отпуска сотрудника
**Endpoint:** `GET /api/vacations/?employee_id=123&limit=3`

### 3. Получить отпуска за период
**Endpoint:** `GET /api/vacations/?start_date=2023-07-01&end_date=2023-07-31`

### 4. Удалить отпуск
**Endpoint:** `DELETE /api/vacations/{id}/`  
**Успешный ответ:** 204 No Content

## Тестирование
```bash
docker-compose exec web python manage.py test vacations
```

## Особенности реализации
- Проверка пересечения отпусков при создании
- Фильтрация по сотруднику и датам
- Автоматическое создание суперпользователя при запуске
