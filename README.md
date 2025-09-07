# diary-backend

Простой backend-ежедневник на FastAPI с PostgreSQL.

## Функционал

- создавать записи;  
- редактировать запись;
- удалять запись;
- читать запись;
- просматривать список всех записей;
- помечать запись как выполненную.


## Используемые технологии

- **Python** — основной язык программирования  
- **FastAPI** — веб-фреймворк для создания API  
- **SQLAlchemy** — ORM для работы с базой данных  
- **PostgreSQL** — реляционная база данных  
- **Uvicorn** — ASGI сервер для запуска FastAPI  
- **Docker** — для контейнеризации приложения и базы данных  

## Развёртывание

1) git clone git@github.com:RH1532/diary-backend.git
2) python -m venv venv
3) source venv/Scripts/activate
4) docker-compose up --build
5) после запуска http://localhost:8000/docs