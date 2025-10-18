# ⚽ Onside

**Keep your finances in the game.**

Onside is a personal financial companion that turns expense tracking from a chore into an engaging, motivational, and social game. Instead of just listing numbers, Onside acts as your pocket-sized financial coach, helping you stay "onside" with your budget and achieve your savings goals.

---

## ✨ Project Vision & Key Features

This app is being built with emotion, intelligence, and experience in mind.

* **🎮 1. Gamification — Make Money Management Fun**
    * **SmartPoints:** Earn points for positive habits like logging expenses or hitting budget goals.
    * **Streaks & Rewards:** Get motivational badges for consistency (e.g., "7-day tracking streak!").
    * **Saving Challenges:** "Spend less than €100 on coffee this month to unlock a reward."

* **🧠 2. AI Money Coach**
    * Get proactive, personalized insights, not just data.
    * *"Hey! You're spending 25% less on dining—great job 👏."*
    * *"If you cut your subscriptions by €10, you can save €120 yearly."*

* **🖼️ 3. Mood-Based Dashboard**
    * Customize your app's theme to match your financial mood (e.g., Calm Mode, Hustle Mode, Minimal Mode).

* **🪄 4. Smart Insights & Stories**
    * Receive visual, story-based weekly summaries of your financial habits, not just static charts.

* **🌍 5. Social & Shared Goals**
    * Create collaborative savings goals with friends (e.g., "Let's save €300 for a trip").
    * Includes a built-in bill-splitting feature.

* **💸 6. Smart Automation**
    * Auto-categorization that learns your spending habits.
    * A subscription tracker that detects recurring payments.

---

## 🛠️ Tech Stack

This project is being built in phases.

| Component | Phase 1 (Current MVP) | Phase 2 & Beyond (Roadmap) |
| :--- | :--- | :--- |
| **Backend** | Django | Django REST Framework |
| **Frontend** | HTML, CSS (Bootstrap) | React |
| **Database**| SQLite | PostgreSQL |
| **Deployment**| (Local Development) | Docker, CI/CD (GitHub Actions) |

---

## 🚀 Getting Started (Running the MVP)

You can run the current, server-rendered version of the app on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/onside.git](https://github.com/your-username/onside.git)
    cd onside
    ```

2.  **Create and activate a virtual environment:**
    * On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required dependencies:**
    ```bash
    pip install Django
    ```

4.  **Apply the database migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
    (Remember: The password will be hidden as you type!)

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7.  **Open the app!**
    Navigate to `http://127.0.0.1:8000/` in your web browser. You can sign up for a new account or log in.

---

## 🗺️ Project Roadmap

* **✅ Phase 1: The Core Functional App (Complete)**
    * Secure user authentication (Sign up, Login, Logout).
    * Full CRUD (Create, Read, Update, Delete) for transactions.
    * Simple dashboard with total income, expenses, and net balance.
    * *Technology: Django, HTML, CSS, SQLite.*

* **➡️ Phase 2: The Modern Frontend & API**
    * Decouple the frontend and backend.
    * Build a REST API using **Django REST Framework**.
    * Build a new, dynamic frontend using **React**.
    * Implement "Mood-Based Dashboards" and basic charts.
    * Migrate database to **PostgreSQL**.

* **➡️ Phase 3: Intelligence & Gamification**
    * Build the backend logic for the "AI Coach" (rule-based insights).
    * Implement the SmartPoints, Badges, and Streaks system.
    * Add the Subscription Tracker.

* **➡️ Phase 4: Social & Deployment**
    * Build the Shared Goals and Bill Splitting features.
    * Containerize the entire application using **Docker**.
    * Set up a **CI/CD** pipeline for automated testing and deployment.
