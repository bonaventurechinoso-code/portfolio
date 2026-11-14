# Bonaventure Chinonso Mabia — Python Portfolio Engine

A modern, high-performance Full-Stack Software & DevOps Engineering portfolio built on **Python & Flask**. This project preserves the exact dark-mode design with dynamic Jinja2 templating, structured data models, interactive resume preview with shareable & downloadable PDF, contact inquiry persistence, and admin logging.

---

## 🌐 Live Demo & Production Links

* **Live Production Server (School ERP):** [https://bonaveeict.com.ng](https://bonaveeict.com.ng)
* **GitHub Profile:** [https://github.com/bonaventurechinoso-code](https://github.com/bonaventurechinoso-code)
* **Local Development Engine:** [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📁 Project Structure

```
Portfolio/
├── app.py                  # Main Flask application & factory (create_app)
├── config.py               # Application configuration (HOST, PORT, SECRET_KEY)
├── requirements.txt        # Pinned Python dependencies (Flask, python-dotenv)
├── README.md               # Setup and architecture documentation
├── .gitignore              # Ignores venv/, __pycache__/, .env, messages.txt, .mypy_cache/
├── .env.example            # Environment variables template
├── data/
│   ├── __init__.py         # Package initialization
│   └── portfolio.py        # Centralized Python data dictionary (profile, skills, projects, education)
├── templates/
│   ├── base.html           # Master layout (head, nav, mobile drawer, footer, flash alerts)
│   ├── index.html          # Portfolio view extending base.html (loops through portfolio.py)
│   ├── resume.html         # Interactive resume preview with PDF download, print & share
│   ├── messages.html       # Internal admin console displaying inquiries from messages.txt
│   └── 404.html            # Custom dark-theme 404 error page
├── static/
│   ├── css/                # Custom CSS styling
│   ├── js/                 # Custom client-side scripts
│   ├── docs/               # Official PDF documents (Bonaventure_Chinonso_Mabia_Resume.pdf)
│   └── images/             # Profile passport and project architecture images
└── messages.txt            # Auto-generated log of contact form inquiries (not committed)
```

---

## 🚀 Setup & Execution Guide (Windows)

### 1. Create the Virtual Environment
Open PowerShell in the project directory and create an isolated virtual environment:
```powershell
python -m venv venv
```

### 2. Activate the Virtual Environment
```powershell
.\venv\Scripts\activate
```
*(If script execution is restricted in PowerShell, you can run directly with `.\venv\Scripts\python.exe`)*

### 3. Install Dependencies
Install all required packages strictly inside the virtual environment:
```powershell
pip install -r requirements.txt
```

### 4. Configure Environment Variables (Optional)
Copy `.env.example` to `.env`:
```powershell
Copy-Item .env.example .env
```
Default configuration binds strictly to `127.0.0.1:5000`.

### 5. Run the Python Engine
```powershell
python app.py
```
Or using the virtual environment directly:
```powershell
.\venv\Scripts\python.exe app.py
```

### 6. Access in Browser
* **Portfolio Home:** [http://127.0.0.1:5000](http://127.0.0.1:5000)
* **Resume Preview & PDF:** [http://127.0.0.1:5000/resume](http://127.0.0.1:5000/resume)
* **Direct PDF View:** [http://127.0.0.1:5000/resume/pdf](http://127.0.0.1:5000/resume/pdf)
* **Health Check API:** [http://127.0.0.1:5000/health](http://127.0.0.1:5000/health)
* **Inquiries Admin Log:** [http://127.0.0.1:5000/messages](http://127.0.0.1:5000/messages)

---

## 🛠️ Routes & Capabilities

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Serves the full portfolio, rendering data dynamically from `data/portfolio.py`. |
| `GET` | `/resume` | Interactive resume preview page with PDF download, link sharing, and print options. |
| `GET` | `/resume/pdf` | Inline PDF viewer and shareable direct link for recruiters and clients. |
| `GET` | `/download-resume` | Serves the official vector PDF resume as an attachment download (`Bonaventure_Chinonso_Mabia_Resume.pdf`). |
| `GET` | `/health` | JSON service monitor endpoint returning `{"status": "ok"}`. |
| `GET` | `/favicon.ico` | Serves favicon icon preventing browser 404 resource errors. |
| `POST` | `/contact` | Validates submitted Name, Email, and Message, appends entry with timestamp to `messages.txt`, flashes confirmation, and redirects to `/#contact`. |
| `GET` | `/messages` | Private internal admin console parsing and listing all inquiries stored in `messages.txt`. |
| `*` | `404 Handler` | Catches non-existent routes and renders the dark-theme `404.html`. |

---

## 📝 How to Edit Content (`data/portfolio.py`)

All site content is decoupled from HTML into clean Python data structures in [`data/portfolio.py`](file:///c:/Users/DELL/Desktop/Portfolio/data/portfolio.py):

* **Developer Profile (`PROFILE`):** Change `name`, `title`, `avatar` (`images/bonaventure-passport.jpg`), `hero_bio`, `availability_status`, `email`, and timezone.
* **Skills Matrix (`SKILLS`):** Modify tier categories (`Front-End Tier`, `Back-End & Data`, `DevOps & Infra`) and clean technology skill badges.
* **Featured Projects (`PROJECTS`):** Add, update, or reorder systems (e.g. School ERP, BCM Portfolio), including labels, specs, and repository URLs.
* **Education & Credentials (`EDUCATION`):** Update degrees, institutions, and coursework highlights.
* **Direct Channels (`SOCIAL_LINKS`):** Change links and contact handles for Email, GitHub, and Portfolio.
