# Оглавление

- [О проекте](#о-проекте)  
- [Наполнение](#наполнение)  
- [Навигация](#навигация)  
- [Использование](#использование)

---

# О проекте

Репозиторий для сбора всех известных уязвимостей, их исправлений и кейсов настроек DevSecOps инструментов, которые помогают их обнаруживать. 

**Цель** — централизовать паттерны уязвимостей по языкам, направлениям разработки и инфраструктуре, чтобы минимизировать риск попадания уязвимого кода в прод.  

---

# Наполнение

Репозиторий будет постепенно наполняться по мере появления реальных продовых кейсов и инструкций из личной практики, формируя живую энциклопедию уязвимостей, исправлений, payload’ов и конфигураций DevSecOps инструментов — эталонный источник знаний для профессионалов уровня Senior AppSec/DevSecOps.

---

# Навигация

От корня репозитория:

- `languages/` — примеры уязвимостей по языкам и направлениям: **python**, **javascript**, **typescript**, **java**, **dotnet**, **c**, **cpp**, **erlang**, **go**, **rust**
  - Внутри каждого языка контекст: `web/`, `cli/`, `system/`, `mobile/`, `embedded/`
  - Каждый кейс содержит:
    - `vuln_app.*` — уязвимый код  
    - `fixed_app.*` — исправленная версия  
    - `exploit_payload.txt` — демонстрация атаки (если применимо)  
    - `README.md` — описание кейса

- `infrastructure/` — примеры уязвимостей и best-practice по Cloud, Orchestration, Containerization, IaC

- `devsecops/` — конфиги и примеры инструментов безопасности: **sast**, **dast**, **fuzzing**, **secrets**, **sca**, **iac-scanning**, **ci-cd-pipelines**

---

# Использование

Перейти к языку и контексту интересующего кейса, например:  
[languages/python/web/flask/sql-injection-unparameterized-query](languages/python/web/flask/sql-injection-unparameterized-query)

Сравнить уязвимый и исправленный код:  
[vuln_app.py](languages/python/web/flask/sql-injection-unparameterized-query/vuln_app.py) | [fixed_app.py](languages/python/web/flask/sql-injection-unparameterized-query/fixed_app.py)

Изучить конфиги инструментов для кейса:  
[devsecops/sast/semgrep/python/sql-injection-unparameterized-query.yaml](devsecops/sast/semgrep/python/sql-injection-unparameterized-query.yaml)
