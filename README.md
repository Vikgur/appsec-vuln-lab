# appsec-vuln-lab

Практическая лаборатория по AppSec / DevSecOps с реалистичными кейсами.

Демонстрирует мой опыт: как уязвимости возникают в реальных системах, как они эксплуатируются и как устраняются на уровне production.

---

# Оглавление

* [О проекте](#о-проекте)
* [Ключевые навыки](#ключевые-навыки)
* [Навигация](#навигация)
* [Структура кейса](#структура-кейса)
* [Как смотреть](#как-смотреть)

---

# О проекте

Репозиторий отражает полный цикл работы AppSec / DevSecOps инженера:

**контекст продукта → уязвимость → эксплуатация → исправление → предотвращение → обнаружение**

Все кейсы построены на реалистичных сценариях:

- реальные архитектурные паттерны  
- типичные ошибки разработки и инфраструктуры  
- практические векторы атак  

Цель — показать не теорию, а прикладные навыки работы с безопасностью в production-системах.

---

# Ключевые навыки

**AppSec**

- анализ поверхности атаки  
- выявление и классификация уязвимостей  
- разбор первопричин  

**Exploitation**

- воспроизведение атак  
- построение exploit-сценариев  

**Secure Development**

- внедрение корректных исправлений  
- secure coding / secure configuration  

**DevSecOps**

- формализация правил предотвращения  
- подготовка CHECKLIST и security-рекомендаций  
- применение security-практик в инфраструктуре и CI/CD  

---

# Навигация

Основные разделы:

- `languages/` — уязвимости в приложениях (язык → контекст → фреймворк → кейс)  
- `infrastructure/` — безопасность инфраструктуры и облака  
- `supply-chain/` — безопасность CI/CD, зависимостей и артефактов  
- `devsecops/` — конфигурации security-инструментов  

---

# Структура кейса

Каждый кейс включает:

- `feature.md` — контекст продукта  
- `vuln_*` — уязвимая реализация  
- `exploit/` или `exploit_payload.txt` — сценарий атаки  
- `fixed_*` — исправление  
- `CHECK_LIST.md` — меры предотвращения  
- `README.md` — полный разбор  

---

# Как смотреть

**На примере кейса SQL Injection в Python/Flask:**

1. Открыть кейс:  
   [languages/python/web/flask/sql-injection-login-query](languages/python/web/flask/sql-injection-login-query)

2. Понять контекст продукта:  
   [languages/python/web/flask/sql-injection-login-query/feature.md](languages/python/web/flask/sql-injection-login-query/feature.md)

3. Изучить уязвимость:  
   [languages/python/web/flask/sql-injection-login-query/vuln_app.py](languages/python/web/flask/sql-injection-login-query/vuln_app.py)

4. Посмотреть эксплуатацию:  
   [languages/python/web/flask/sql-injection-login-query/exploit_payload.txt](languages/python/web/flask/sql-injection-login-query/exploit_payload.txt)

5. Проверить исправление:  
   [languages/python/web/flask/sql-injection-login-query/README.md](languages/python/web/flask/sql-injection-login-query/fixed_app.py)

6. Ознакомиться с разбором:  
   [languages/python/web/flask/sql-injection-login-query/README.md](languages/python/web/flask/sql-injection-login-query/README.md)

7. Изучить меры предотвращения:  
   [languages/python/web/flask/sql-injection-login-query/CHECK_LIST.md](languages/python/web/flask/sql-injection-login-query/CHECK_LIST.md)
