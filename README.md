# Lumino

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

**Langue / Language**: [🇫🇷 Français](#-présentation) | [🇬🇧 English](#-overview)

---

## 🇫🇷 Présentation

**Lumino** est un système d’éclairage intelligent basé sur Raspberry Pi et Arduino. Il permet d’automatiser l’allumage ou l’extinction des lampes selon la présence dans une pièce, détectée par un capteur infrarouge. Économe en énergie et modulaire, il s’administre via un tableau de bord web développé en Python (Flask).

---

### ✨ Fonctionnalités principales

- 👤 **Détection de présence IR** pour un éclairage automatisé
- 💡 **Contrôle des lampes** en temps réel depuis l’interface web
- 🔌 **Communication Raspberry Pi ↔ Arduino** (série ou protocole personnalisé)
- 🌍 **Dashboard local responsive** sans base de données
- 🛠 **Configuration des seuils, délais et profils** via fichiers XML
- 🔐 **Accès sécurisé en local** (mot de passe ou clé API)

---

## ⚙️ Prérequis

- Raspberry Pi (Pi 3 ou 4 recommandé)

- Arduino (Uno, Nano, etc.)

- Python 3.9+

- pip

- Flask

- Capteur PIR (IR) + relais ou module de commande lumière

---

## 🚀 Lancement de l’application

1. **Cloner le dépôt** :

```bash
git clone https://github.com/lunaris1212/Lumino.git
cd Lumino
```

2. **Installer les dépendances** :

```bash
[commande d'installation des dépendances avec pip ...]
```

3. **Démarrer l'application** :

```bash
[commande pour lancer le fichier main.py ...]
```

---

## 📝 Licence
Ce projet est sous licence **Creative Commons BY-NC-ND 4.0**.

Usage personnel et non commercial autorisé.

Redistribution modifiée interdite sans accord de l’auteur.

Plus d’infos : https://creativecommons.org/licenses/by-nc-nd/4.0/

---

## 📩 Contact
Pour toute demande de redistribution, intégration ou usage commercial :
[lunaris121200@gmail.com]

---
---

# Lumino

## 🇬🇧 Overview
**Lumino** is a smart lighting system based on Raspberry Pi and Arduino. It automates light control based on IR presence detection and offers a lightweight, local web interface built with Python (Flask). Its goal: comfort and energy savings without sacrificing simplicity.

### ✨ Key Features
- 👤 **IR-based presence detection** for automatic light control

- 💡 **Real-time control of lights** via web dashboard

- 🔌 **Raspberry Pi ↔ Arduino** communication (serial or custom protocol)

- 🌍 **Local web dashboard** – no database required

- 🛠 **Profile & behavior customization** via XML files

- 🔐 **Local access secured** with password or API key

---

## ⚙️ Requirements

- Raspberry Pi (Pi 3 or 4 recommended)

- Arduino (Uno, Nano, etc.)

- Python 3.9+

- pip

- Flask

- PIR sensor + relay or smart light control module

---

##  🚀 How to Run

1. **Clone the repository**:

```bash
git clone https://github.com/lunaris1212/Lumino.git
cd Lumino
```

2. **Install dependencies**:

```bash
[dependency install command using pip ...]
```

3. **Start the application**:

```bash
[command to launch main.py ...]
```

---

## 📝 License

This project is licensed under **Creative Commons BY-NC-ND 4.0**.

Personal and non-commercial use is allowed.

Distribution of modified versions is forbidden without permission.

More info: https://creativecommons.org/licenses/by-nc-nd/4.0/

---

## 📩 Contact
For redistribution, integration, or commercial use:
[lunaris121200@gmail.com]
