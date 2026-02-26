# Freelancers' Tools & Resources Hub

A full-stack Django application that centralizes essential tools for freelancers — including time tracking, budgeting, gig discovery, and document management.

---

## 📌 Description

Freelancers' Tools & Resources Hub is designed to streamline freelance workflows by combining project tracking, financial management, and opportunity discovery into a single platform.

The project focuses on backend data modeling, structured workflow management, and REST API integration using Django and MySQL.

---

## ✨ Features

- **Dashboard** – Overview of income, expenses, and active projects  
- **Time Tracker** – Track billable hours across multiple projects  
- **Budget Manager** – Categorized income and expense tracking  
- **Gig Finder** – Fetch and display freelance job listings using REST APIs  
- **Document Organizer** – Upload and manage contracts and invoices  

---

## 🏗 Architecture Overview

The backend follows Django’s MVC-style architecture:

- **Models** – Define database schema and relationships using Django ORM  
- **Views** – Handle request processing and business logic  
- **Templates / Responses** – Render UI or return structured responses  

Database interactions are managed using Django ORM, ensuring clean abstraction from raw SQL queries and maintainable data handling.

Core modules such as time tracking, budgeting, and gig integration are logically separated for clarity and scalability.

---

## 🛠 Tech Stack

### Backend
- Django (Python)
- Django ORM
- MySQL

### Frontend
- HTML
- CSS
- JavaScript
- Bootstrap

### Tools & Integrations
- Git (Version Control)
- REST API Integration

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Pavankumar-22/freelancers-hub.git
cd freelancers-hub
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Database Migrations

```bash
python manage.py migrate
```

### 5️⃣ Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## 🚀 Usage

1. Register or log in  
2. Monitor income and expenses from the dashboard  
3. Track billable hours using the Time Tracker  
4. Manage financial records with the Budget Manager  
5. Discover freelance opportunities via the Gig Finder  
6. Upload and organize important documents  

---

## 📚 Key Learning Outcomes

- Backend development using Django  
- Relational database modeling with MySQL  
- REST API integration  
- Modular full-stack application structuring  
- Financial and time-based data management  

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository  
2. Create a feature branch:

```bash
git checkout -b feature-name
```

3. Commit your changes and push  
4. Submit a pull request  

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Pavan Kumar**  
📧 pavankumar80890@gmail.com  
🔗 https://www.linkedin.com/in/pavan-kumar-bb4581249/
