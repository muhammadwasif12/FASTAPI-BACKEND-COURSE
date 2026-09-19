# ⚡ FastAPI Backend Mastery Course

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis" />
  <img src="https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white" alt="Celery" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens" alt="JWT" />
</p>

A structured, practical roadmap progressing from **FastAPI core fundamentals** to building **enterprise-grade, production-ready distributed backend architectures**.

---

## 📂 Repository Structure

```
FASTAPI-BACKEND-COURSE/
├── 📁 crash-course/           # Phase 1: FastAPI Fundamentals (Issue Tracker API)
│   ├── app/
│   │   ├── middleware/        # Custom execution timing middleware
│   │   ├── routes/            # Modular APIRouters (Issues CRUD)
│   │   ├── schemas.py         # Pydantic data validation & serialization
│   │   └── storage.py         # File-based JSON data persistence layer
│   ├── data/issues.json       # Mock database storage
│   ├── main.py                # App entrypoint, CORS & middleware config
│   └── requirements.txt       # Dependencies
│
└── 📁 beyond-crud/            # Phase 2: Production-Grade REST API (Bookly)
    ├── src/
    │   ├── auth/              # Dual JWT, RBAC, Password Hashing & URL Tokens
    │   ├── books/             # Books Domain (Routes, Services, Schemas)
    │   ├── reviews/           # Reviews Domain (1:N Relationships & Ownership)
    │   ├── tags/              # Tags Domain (Many-to-Many via BookTag)
    │   ├── db/                # Async PostgreSQL, SQLModel & Redis Blocklist
    │   ├── celery_tasks.py    # Asynchronous worker tasks (Email dispatch)
    │   ├── mail.py            # FastAPI-Mail SMTP client integration
    │   ├── errors.py          # Centralized domain exception handlers
    │   ├── middleware.py      # Latency profiler, CORS & TrustedHost
    │   └── config.py          # Pydantic BaseSettings (.env management)
    ├── migrations/            # Alembic schema versioning scripts
    ├── compose.yml            # Multi-container orchestration (App, Postgres, Redis, Worker)
    ├── Dockerfile             # Container packaging
    ├── requirements.txt       # Project dependencies
    └── PROJECT_EXPLANATION.md # 📖 350+ lines ultra-detailed architectural deep dive
```

---

## 📑 Projects Overview

| Feature / Concept | 🐣 [Crash Course](./crash-course/) | 🚀 [Beyond CRUD (Bookly)](./beyond-crud/) |
| :--- | :--- | :--- |
| **Domain** | Issue Tracker API | Book Review & Social Platform (Bookly) |
| **Data Layer** | JSON File Storage | PostgreSQL (Async via `async_engine`) |
| **ORM / Modeling** | Pure Pydantic | **SQLModel** (Pydantic + Async SQLAlchemy) |
| **Authentication** | None (Public API) | **JWT (Access + Refresh)** & bcrypt hashing |
| **Token Invalidation**| N/A | **Redis JTI Blocklisting** (Stateless Logout) |
| **Authorization** | Open | **RBAC** (`admin`, `user`) + Email Verification |
| **Async Background** | Synchronous | **Celery + Redis** (Non-blocking Emails) |
| **DB Migrations** | None | **Alembic** (Incremental Schema Revisions) |
| **Architecture** | Simple Modular Router | **Layered Architecture** (Routes → Services → Models) |
| **DevOps / Deploy** | Local Virtualenv | **Docker & Docker Compose** (4 Containers) |

---

## 🐣 Project 1: FastAPI Crash Course (Issue Tracker API)

A hands-on introduction to FastAPI's modern paradigms.

### Key Highlights:
* **Pydantic Validation**: Strong request typing, default values, and response models.
* **Modular Routing**: Clean route separation with `APIRouter`.
* **Custom Middleware**: HTTP request duration profiler (`timing_middleware`).
* **CORS Setup**: Allowing cross-origin calls for frontend integration.
* **CRUD Mechanics**: Real-world operations on structured resources (`GET`, `POST`, `PUT`, `DELETE`).

### Quickstart (Crash Course):
```bash
cd crash-course
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
API Interactive Docs: `http://127.0.0.1:8000/docs`

---

## 🚀 Project 2: Beyond CRUD — "Bookly" Production API

An advanced, scalable web service for managing books, user reviews, and tags. Designed according to real-world software engineering principles.

> 📖 **Deep Dive Documentation**: For an exhaustive, step-by-step breakdown of every single file, architectural decision, and request trace, read [**`beyond-crud/PROJECT_EXPLANATION.md`**](./beyond-crud/PROJECT_EXPLANATION.md).

### Key Architectural Systems:

#### 1. Layered Clean Architecture
* **Routes (`src/*/routes.py`)**: Thin controllers handling HTTP transport, dependency injection, and HTTP status codes.
* **Services (`src/*/service.py`)**: Isolated business logic and database access.
* **Schemas (`src/*/schemas.py`)**: Strict DTOs preventing internal model leakage.
* **Models (`src/db/models.py`)**: SQLModel entities with relational integrity.

#### 2. Advanced Security & RBAC
* **Dual-Token Flow**: Short-lived Access Tokens (1 Hour) paired with long-lived Refresh Tokens (2 Days).
* **Stateless Revocation (Redis)**: When logging out, token `jti` IDs are stored in Redis with TTL to immediately revoke access before expiration.
* **Cryptographic URL Tokens**: Safe email verification and password reset links powered by `itsdangerous`.
* **Role Enforcement**: Reusable `RoleChecker(["admin", "user"])` dependency checking verification status and privileges.

#### 3. Fully Asynchronous Relational Database
* Powered by **SQLModel** + **Asyncpg** + **PostgreSQL**.
* **1:N Relationships**: User to Books, Book to Reviews.
* **M:N Relationships**: Books to Tags through `BookTag` junction table.
* **Eager Pre-fetching**: Utilizes `sa_relationship_kwargs={"lazy": "selectin"}` to eliminate async Greenlet lazy-loading errors.

#### 4. Asynchronous Task Queue (Celery + Redis)
* Offloads blocking SMTP operations (FastAPI-Mail) to background **Celery Workers**.
* User signup and password resets respond in milliseconds without waiting for SMTP handshakes.

#### 5. Resilient Error Handling & Middleware
* Centralized domain exception hierarchy (`BooklyException`) returning predictable error envelopes:
  ```json
  {
    "message": "User with email already exists",
    "error_code": "user_exists"
  }
  ```
* Host Header validation via `TrustedHostMiddleware` and custom latency logging.

---

## 🐳 Quickstart (Beyond CRUD with Docker)

The easiest way to run the entire distributed stack (FastAPI, PostgreSQL, Redis, and Celery Worker):

```bash
cd beyond-crud

# 1. Copy environment configuration
cp .env.example .env

# 2. Build and start all services
docker compose up --build
```

### Services Started:
* 🌐 **FastAPI Web Service**: `http://localhost:8000`
* 📚 **Interactive Swagger UI**: `http://localhost:8000/api/v1/docs`
* 🐘 **PostgreSQL**: `localhost:5432`
* 🔴 **Redis Cache / Broker**: `localhost:6379`
* ⚙️ **Celery Worker**: Background task executor

---

## 🛠️ Tech Stack & Libraries

| Technology | Purpose |
| :--- | :--- |
| **[FastAPI](https://fastapi.tiangolo.com/)** | Modern, high-performance async Python web framework |
| **[SQLModel](https://sqlmodel.tiangolo.com/)** | Combined power of SQLAlchemy ORM & Pydantic validation |
| **[PostgreSQL](https://www.postgresql.org/)** | Primary ACID-compliant relational database |
| **[Redis](https://redis.io/)** | In-memory store for JWT blocklist and Celery message broker |
| **[Celery](https://docs.celeryq.dev/)** | Distributed asynchronous task queue |
| **[Alembic](https://alembic.sqlalchemy.org/)** | Database schema migration tool |
| **[PyJWT](https://pyjwt.readthedocs.io/)** & **[Passlib](https://passlib.readthedocs.io/)** | Cryptographic token handling & bcrypt password hashing |
| **[FastAPI-Mail](https://sabuhish.github.io/fastapi-mail/)** | Async transactional email dispatcher |
| **[Docker](https://www.docker.com/)** | Multi-service containerization |

---

## 👨‍💻 Author

**Muhammad Wasif**  
* GitHub: [@muhammadwasif12](https://github.com/muhammadwasif12)  
* Repository: [FASTAPI-BACKEND-COURSE](https://github.com/muhammadwasif12/FASTAPI-BACKEND-COURSE)

⭐ If you found this repository helpful, consider giving it a star!
