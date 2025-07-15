# 🧱 Пустое FastAPI-приложение с DDD-архитектурой

Простой проект, реализующий [Domain-Driven Design (DDD)](https://en.wikipedia.org/wiki/Domain-driven_design) в FastAPI.  
Служит учебной основой для понимания архитектуры и принципов DI (инъекции зависимостей) с помощью библиотеки [Dishka](https://github.com/reagento/dishka).

---

## 🚀 Возможности

- ✅ Добавление пользователя (имя + email)
- ✅ Получение пользователя по UUID
- 🧠 Демонстрация DDD-структуры
- 🧪 Внедрение зависимостей через **Dishka**
- 🗄️ Асинхронный доступ к PostgreSQL через SQLAlchemy 2.x

---

## 🛠️ Стек технологий

- **FastAPI** — веб-фреймворк
- **PostgreSQL** — СУБД
- **SQLAlchemy 2.x (async)** — работа с БД
- **Alembic** — миграции
- **Docker + Docker Compose**
- **Dishka** — Dependency Injection (DI)

---

## ⚙️ Установка и запуск

### 1. Клонируй проект

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Создай файл `.env` на основе `.env.example`

```env
# пример .env
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_USER=fastapi
POSTGRES_PASSWORD=fastapi
POSTGRES_DB=fastapi
```

### 3. Пропиши адрес БД в `alembic.ini`

```ini
# alembic.ini
sqlalchemy.url = postgresql+asyncpg://fastapi:fastapi@db:5432/fastapi
```

> Или задай `DATABASE_URL` через переменные окружения

---

### 4. Собери и запусти контейнеры

```bash
docker compose up --build
```

### 5. Применить миграции (изнутри контейнера)

```bash
docker compose exec app alembic upgrade head
```

---

## 📬 Пример использования

Открой [http://localhost:8000/docs](http://localhost:8000/docs) — Swagger UI.

1. Вызови `POST /users/` с телом:

```json
{
  "name": "Максим",
  "email": "maks@example.com"
}
```

2. Скопируй `uuid` из ответа и вызови:

```http
GET /users/?user_id=<uuid>
```

---

## 📁 Архитектура проекта (DDD)

Проект разделён на слои:

```
DDD_example/
├── alembic/
├── src/
│   ├── api/  # HTTP контроллеры
│   ├── application/  # бизнес логика приложения
│   ├── domain/  # доменные сущности
│   ├── infrastructure/  # здесь хранятся адаптеры
│   ├── ioc_container.py  # IoC - контейнер с зависимостями
│   └── main.py  # точка входа
│
├── .env
├── alembic.ini
├── docker-compose.yaml


```

---

## 🧠 Почему этот проект?

> Я хотел научиться применять **DDD-подход**, внедрять **инъекцию зависимостей** и собирать **чистую архитектуру**.  
> Этот шаблон можно использовать как основу для будущих FastAPI-проектов.

---

