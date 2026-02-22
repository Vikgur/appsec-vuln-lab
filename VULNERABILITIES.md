# Описание

Этот файл содержит полный список HIGH/CRITICAL уязвимостей, покрытых в данном репозитории.  
Цель — показать знание всех основных классов угроз по разным языкам, фреймворкам и контекстам.

---

# Контекст

## Web / Backend

### Python / Flask

*По 1 репрезентативному примеру на каждый*

1. **SQL Injection**  
2. **Command Injection**  
3. **NoSQL Injection**  
4. **Template Injection (SSTI)**  
5. **Path Traversal**  
6. **Insecure File Upload**  
7. **Unsafe Deserialization (pickle)**  
8. **Unsafe YAML Load**  
9. **Reflected XSS**  
10. **Stored XSS**  
11. **CSRF** (state-changing POST без защиты)  
12. **Broken Authentication**  
    - session fixation  
    - отсутствие ротации session id  
    - слабый session id  
13. **JWT Validation Flaws**  
    - alg confusion  
    - отсутствие проверки exp / aud / iss  
14. **IDOR** (горизонтальная эскалация)  
15. **Vertical Privilege Escalation**  
    - проверка роли только в UI  
    - отсутствие backend enforcement  
16. **SSRF**  
    - доступ к внутренним сервисам  
    - metadata endpoint  
17. **Open Redirect**  
18. **Insecure Cryptography**  
    - MD5 / SHA1 для паролей  
    - отсутствие salt  
    - слабый random  
19. **Hardcoded Secret / Secret Leakage**  
    - ключи в коде  
    - debug mode / verbose errors  
20. **Dependency Risk**  
    - unpinned версии  
    - использование небезопасной библиотеки  
21. **Race Condition / TOCTOU**  
    - двойное списание  
    - check-then-use bug  
22. **Resource Exhaustion / DoS**  
    - бесконтрольный upload  
    - regex catastrophic backtracking  
23. **CORS Misconfiguration**  
    - `Access-Control-Allow-Origin: *` с credentials  
    - динамическое отражение Origin