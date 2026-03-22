# Table of Contents

* [About](#about)
* [Vulnerability Overview](#vulnerability-overview)
* [Feature Context](#feature-context)
* [Attack Surface](#attack-surface)
* [Vulnerable Flow](#vulnerable-flow)
* [Exploit](#exploit)
* [Impact](#impact)
* [Root Cause](#root-cause)
* [Fix (Base)](#fix-base)
* [Prevention](#prevention)
* [What’s Missing](#whats-missing)
* [Next Step](#next-step)
* [License](#license)

---

## About

Docker socket exposure breaks container isolation and gives direct host control.  
This pattern appears in CI agents, internal tooling, and production services.

---

## Vulnerability Overview

Class: Misconfiguration / Container Escape  

Mounting the Docker socket into a container exposes the Docker daemon.  
Any process inside gains root-equivalent control over the host.

---

## Feature Context

Containers interact with Docker to manage workloads dynamically.  
Used in CI pipelines, orchestration helpers, and internal automation tools.

---

## Attack Surface

Entry: compromised container (RCE, SSRF, creds)  
Boundary: container → host via Docker daemon

---

## Vulnerable Flow

Container runs with docker.sock mounted  
Attacker gains access to container  
Docker API becomes accessible  
New container is created with host filesystem mounted  
Attacker pivots into host environment

---

## Exploit

See exploit/  

Attacker uses Docker CLI or API  
Launches container with `/` mounted from host  
Executes commands inside host context  
Extracts sensitive data or establishes persistence

---

## Impact

Full host compromise  
Access to secrets, configs, credentials  
Lateral movement across infrastructure  
Persistence via new containers or host changes

---

## Root Cause

Docker daemon is exposed to an untrusted execution context.  
The system assumes container isolation, but grants root-level control via socket access.

---

## Fix (Base)

See fixed_config/  

Remove docker.sock mount.  
Do not allow containers to access Docker daemon directly.

---

# Prevention

Prevent issues through manual checks and **DevSecOps practices implementation**. 
This case demonstrates one of many possible approaches — a combination of several tools — and is not the only viable solution.

Find configurations in **DEVSECOPS.md**.

---

## What’s Missing

bypass techniques  
edge cases (partial access, read-only socket)  
detection strategies  
CI/CD enforcement  
runtime monitoring  
production hardening patterns  

---

## Next Step

Production coverage includes:  
checklist  
threat modeling  
hardening  
detection  

→ full production version is available in appsec-forge-pro

# License

This case is part of the repository licensed under the MIT License.
See the root LICENSE file for details.