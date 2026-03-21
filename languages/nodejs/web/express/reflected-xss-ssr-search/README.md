# Table of Contents

* [About](#about)
* [Vulnerability Overview](#vulnerability-overview)
* [Feature Context](#feature-context)
* [Attack Surface](#attack-surface)
* [Vulnerable Flow (High-Level)](#vulnerable-flow-high-level)
* [Exploit](#exploit)
* [Impact](#impact)
* [Root Cause](#root-cause)
* [Fix (Base)](#fix-base)
* [What’s Missing](#whats-missing)
* [Next Step](#next-step)

---

# About

Reflected XSS in Express.js SSR breaks user trust and session security.  
This pattern appears in real dashboards, admin panels, and internal tools.

---

# Vulnerability Overview

Cross-Site Scripting (XSS).  
Untrusted input is rendered as executable HTML.  
Browser executes attacker-controlled JavaScript.

---

# Feature Context

Search feature in a server-rendered dashboard.  
Used to display user queries and improve navigation.

---

# Attack Surface

Query parameters (q).  
Boundary: user input → server HTML response → browser execution.

---

# Vulnerable Flow (High-Level)

User sends search request with input.  
Server injects input into HTML response.  
No encoding applied.  
Browser parses response as code.  
Injected script executes.

---

# Exploit

See exploit_payload.txt.  
Attacker crafts malicious URL.  
Victim opens link.  
Script runs in victim session.

---

# Impact

Session theft.  
Account takeover.  
Data exfiltration.  
Action execution on behalf of user.

---

# Root Cause

User-controlled input is directly embedded into HTML without output encoding.  
Rendering logic treats data as trusted content.

---

# Fix (Base)

See fixed_app.js.  
Apply HTML encoding before rendering user input.  
Convert unsafe characters into safe output.

---

# What’s Missing

Bypass techniques  
Edge-case payloads  
Template engine behavior  
Detection strategies  
CI/CD enforcement  
Production hardening  

---

# Next Step

Production coverage includes:  
checklist  
threat modeling  
hardening  
detection  

→ full production version is available in appsec-forge-pro