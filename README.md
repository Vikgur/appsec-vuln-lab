# Оглавление
* [О проекте](#о-проекте)
* [Подход](#подход)
* [Навигация](#навигация)
* [Как использовать репозиторий](#как-использовать-репозиторий)

---

# О проекте

Данный репозиторий — коллекция кейсов из моей личной практики в области анализа и предотвращения уязвимостей в приложениях и инфраструктуре.

Репозиторий демонстрирует навыки работы на всех ключевых этапах AppSec:

* выявление и анализ уязвимостей
* моделирование и демонстрация эксплуатации
* поиск корневых причин и внедрение исправлений
* разработка профилактических мер и правил обнаружения

Уязвимости систематизированы по следующим категориям:

* языки программирования
* контексты среды выполнения
* фреймворки
* инфраструктурные технологии
* облачные платформы

**Цель репозитория** — наглядно представить опыт работы с полным циклом AppSec‑задач. Каждый кейс выстроен по [воспроизводимой методологии](#подход) и охватывает этапы:  

контекст продукта → уязвимость → эксплуатация → анализ → исправление → предотвращение → обнаружение

---

# Подход

Каждый кейс создаётся по воспроизводимой методологии:

1. Выбор реальной **фичи продукта / архитектурного контекста / стека**  
2. Анализ **поверхности атаки**  
3. Выявление наиболее вероятной **уязвимости**  
4. Создание **уязвимого кода**  
5. Демонстрация **эксплуатации**  
6. Определение **первопричины уязвимости**  
7. Внедрение **корректного исправления**  
8. Формирование **рекомендаций по предотвращению**  
9. Разработка шаблонов **правил обнаружения уязвимости** в security‑инструментах

---

# Навигация

От корня репозитория:

## `devsecops/`

Примеры конфигураций security-инструментов, сгруппированные по типу контроля.

## `infrastructure/`

Уязвимости и best practices для инфраструктуры.

Структура: **область → инструмент → контекст → кейс**

Области:

* `cloud/`
* `containerization/`
* `orchestration/`
* `iac-and-config/`

Контексты по областям:

* **cloud:** `identity`, `compute`, `storage`, `network`, `secrets`, `logging-monitoring`
* **containerization:** `image`, `build`, `runtime`, `registry`
* **orchestration:** `rbac`, `workloads`, `network`, `secrets`, `configuration`, `supply-chain`
* **iac-and-config:** `secrets`, `misconfiguration`, `drift`, `access`, `state-management`

Каждый кейс содержит:

* `feature.md` — описание продукта и контекста возникновения уязвимости
* `vuln_config/` — уязвимая реализация
* `fixed_config/` — исправленная версия
* `exploit/` — пример эксплуатации
* `CHECK_LIST.md` — рекомендации и меры защиты
* `README.md` — полный разбор кейса

## `languages/`

Уязвимости по языкам программирования.

Структура: **язык → контекст → фреймворк → кейс**

Контексты:

* `web`
* `cli`
* `system`
* `mobile`
* `embedded`

Каждый кейс содержит:

* `feature.md` — описание продукта и контекста возникновения уязвимости
* `vuln_app.*` — уязвимая реализация
* `fixed_app.*` — исправленная версия
* `exploit_payload.txt` — пример эксплуатации
* `CHECK_LIST.md` — рекомендации и меры защиты
* `README.md` — полный разбор кейса

## `supply-chain/`

Уязвимости и best practices для цепочки поставки ПО (Supply Chain Security).

Структура: **домен → инструмент/технология → контекст → кейс**

Домены:

* `ci-cd/`
* `dependencies/`
* `artifacts/`

Контексты по доменам:

* **ci-cd:** `pipeline`, `secrets`, `access`, `artifacts`, `triggers`
* **dependencies:** `confusion`, `typosquatting`, `poisoning`, `trust`, `versioning`
* **artifacts:** `signing`, `provenance`, `integrity`, `distribution`

Каждый кейс содержит:

* `feature.md` — описание продукта и контекста возникновения уязвимости
* `vuln_config/` — уязвимая реализация (pipeline, registry, dependency config и т.д.)
* `fixed_config/` — исправленная версия
* `exploit/` — пример эксплуатации
* `CHECK_LIST.md` — рекомендации и меры защиты
* `README.md` — полный разбор кейса

---

# Как использовать репозиторий

**На примере кейса SQL Injection в Python/Flask** (шаги универсальны для любого кейса):

1. Перейти к интересующему языку и контексту:  
   [languages/python/web/flask/sql-injection-login-query](languages/python/web/flask/sql-injection-login-query)

2. Изучить сценарий продукта и контекст возникновения уязвимости:  
   [languages/python/web/flask/sql-injection-login-query/feature.md](languages/python/web/flask/sql-injection-login-query/feature.md)

3. Изучить уязвимую реализацию:  
   [languages/python/web/flask/sql-injection-login-query/vuln_app.py](languages/python/web/flask/sql-injection-login-query/vuln_app.py)

4. Ознакомиться с примером эксплуатации:  
   [languages/python/web/flask/sql-injection-login-query/exploit_payload.txt](languages/python/web/flask/sql-injection-login-query/exploit_payload.txt)

5. Изучить анализ уязвимости:  
   [languages/python/web/flask/sql-injection-login-query/README.md](languages/python/web/flask/sql-injection-login-query/README.md)

6. Изучить рекомендации предотвращения:  
   [languages/python/web/flask/sql-injection-login-query/CHECK_LIST.md](languages/python/web/flask/sql-injection-login-query/CHECK_LIST.md)

7. Изучить примеры правил автоматического обнаружения уязвимости:  

   **SAST:**   

   * **Semgrep**: [devsecops/sast/semgrep/languages/python/web/flask/sql-injection-login-query.yaml](devsecops/sast/semgrep/languages/python/web/flask/sql-injection-login-query.yaml)
   * **CodeQL**: [devsecops/sast/codeql/languages/python/web/flask/sql-injection-login-query.ql](devsecops/sast/codeql/languages/python/web/flask/sql-injection-login-query.ql)
   * **Bandit**: [devsecops/sast/bandit/languages/python/web/flask/sql-injection-login-query.yaml](devsecops/sast/bandit/languages/python/web/flask/sql-injection-login-query.yaml)

   **DAST:**   

   * **Owasp ZAP**: [devsecops/dast/owasp-zap/languages/python/web/flask/sql-injection-login-query.yaml](devsecops/dast/owasp-zap/languages/python/web/flask/sql-injection-login-query.yaml)
   * **Nuclei**: [devsecops/dast/nuclei/languages/python/web/flask/sql-injection-login-query.yaml](devsecops/dast/nuclei/languages/python/web/flask/sql-injection-login-query.yaml)

   **Fuzzing:**   

   * **RESTler**: [devsecops/fuzzing/restler/languages/python/web/flask/sql-injection-login-query.yaml](devsecops/fuzzing/restler/languages/python/web/flask/sql-injection-login-query.yaml)
   * **FFUF**: [devsecops/fuzzing/ffuf/languages/python/web/flask/sql-injection-login-query.txt](devsecops/fuzzing/ffuf/languages/python/web/flask/sql-injection-login-query.txt)

   **Scripts:**   

   * **sql-injection-login-query.sh**: [devsecops/scripts/languages/python/web/flask/sql-injection-login-query.sh](devsecops/scripts/languages/python/web/flask/sql-injection-login-query.sh)

