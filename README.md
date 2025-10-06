## 🚀 DevOps Automation Pipeline  

![Jenkins](https://img.shields.io/badge/Jenkins-Automation-blue?logo=jenkins&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-Configuration-red?logo=ansible&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue?logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-Version_Control-orange?logo=git&logoColor=white)
![Python](https://img.shields.io/badge/Flask-App-green?logo=flask&logoColor=white)

---

### 🎯 **Project Goals**

- ⚙️ Automate deployment of a **Flask web app** using **CI/CD pipeline**
- 🔁 Integrate **Git + Jenkins + Ansible + Docker** for full automation  
- 🧩 Achieve a one-click deployment workflow  
- 🐳 Run the app in a **Docker container** hosted automatically after Jenkins build  

---

### 🧠 **Tech Stack**

| Tool | Purpose |
|------|----------|
| 🧱 **Jenkins** | Continuous Integration & Orchestration |
| 🐙 **GitHub** | Source Code Repository |
| ⚙️ **Ansible** | Configuration Management & Continuous Delivery |
| 🐳 **Docker** | Application Containerization |
| 🐍 **Flask (Python)** | Lightweight Web Framework |
| 💻 **Linux (Kali/Ubuntu)** | Base Host System |

---

### 🧩 **Pipeline Workflow**

```text
Developer
   │
   ├── Push code to GitHub
   │
   ▼
Jenkins (CI Server)
   ├── Clones GitHub Repo
   ├── Builds Docker Image
   ├── Executes Ansible Playbook
   │
   ▼
Ansible (CD Tool)
   ├── Installs Docker (if not installed)
   ├── Starts Docker service
   ├── Runs Flask App container
   │
   ▼
Docker (Runtime)
   └── Hosts Flask Web App on port 5000
