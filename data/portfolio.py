"""
Portfolio Data Source
Bonaventure Chinonso Mabia - Full-Stack Software & DevOps Engineer
"""

PROFILE = {
    "name": "Bonaventure Chinonso Mabia",
    "title": "Full-Stack Software & DevOps Engineer",
    "avatar": "images/bonaventure-passport.jpg",
    "github": "https://github.com/bonaventurechinoso-code",
    "github_username": "bonaventurechinoso-code",
    "availability_status": "AVAILABLE FOR HIGH-IMPACT SOFTWARE ENGINEERING ROLES",
    "availability_badge": "READY FOR HIRE",
    "hero_bio": (
        "Engineering resilient web applications, distributed APIs, and scalable infrastructure. "
        "Specializing in robust Python/Django enterprise systems, enterprise Java workflows, "
        "modular front-end architecture, and zero-downtime deployment automation."
    ),
    "email": "bonaventure.chinoso@gmail.com",
    "timezone": "WAT / UTC+1 · Flexible Remote Overlap",
    "availability_description": (
        "Available for full-time engineering roles, high-impact remote distributed teams, "
        "and DevOps contract engagements with full timezone overlap adaptability."
    ),
    "architecture_highlights": [
        {
            "tag": "ARCHITECTURE",
            "title": "100% SOLID",
            "subtitle": "Clean Code & Domain Design",
            "icon": "verified",
            "status_icon": "check_circle"
        },
        {
            "tag": "CORE STACK",
            "title": "Full-Stack Polyglot",
            "subtitle": "Python/Django, Java, Modern JS",
            "icon": "terminal",
            "status_icon": "integration_instructions"
        },
        {
            "tag": "INFRASTRUCTURE",
            "title": "DevOps Ready",
            "subtitle": "Automated CI/CD & Linux Admin",
            "icon": "deployed_code",
            "status_icon": "published_with_changes"
        }
    ]
}

SKILLS = [
    {
        "id": "frontend",
        "category": "Front-End Tier",
        "subtitle": "Client Architecture",
        "badge": "UI/UX",
        "icon": "web",
        "skills": [
            "Tailwind CSS",
            "React",
            "Next.js",
            "TypeScript",
            "JavaScript (ES6+)",
            "Responsive UI & DOM Engineering",
            "HTML5 & Semantic Web",
            "CSS3 & Bootstrap Framework",
            "Flexbox/Grid",
            "DOM API",
            "PWA & Service Workers"
        ]
    },
    {
        "id": "backend",
        "category": "Back-End & Data",
        "subtitle": "Services & Schema",
        "badge": "SERVER",
        "icon": "dns",
        "skills": [
            "Flask",
            "Python & Django Framework",
            "Node.js",
            "Express.js",
            "Java (Core & OOP)",
            "SQL & PostgreSQL Engineering",
            "RESTful API Design & Auth",
            "Data Modeling",
            "Django REST"
        ]
    },
    {
        "id": "devops",
        "category": "DevOps & Infra",
        "subtitle": "Cloud & Automation",
        "badge": "OPS",
        "icon": "settings_suggest",
        "skills": [
            "Docker",
            "Linux System Administration",
            "CI/CD Automation Pipelines",
            "GitLab CI/CD",
            "Git, GitHub & GitLab",
            "Deployment & Health Monitoring",
            "Nginx / Gunicorn",
            "Log Monitoring",
            "Vercel",
            "Render"
        ]
    }
]

PROJECTS = [
    {
        "id": "school-erp",
        "badge": "Multi-Tenant & Multi-Tier",
        "title": "School ERP - Multi-tenant, Multi-tier Staff and Students Lifecycle",
        "description": (
            "School ERP built to manage the full lifecycle of staff and students for multiple schools "
            "(tenants) on one system. Handles student admission and enrollment, course registry, "
            "grading and GPA, and staff records, using a multi-tier architecture."
        ),
        "image": "images/project-portal.jpg",
        "specs": [
            {"label": "Back-End", "value": "Java Core + OOP"},
            {"label": "Database", "value": "SQL Server / PostgreSQL"},
            {"label": "Front-End", "value": "HTML/CSS/JS, PWA"}
        ],
        "demo_url": "https://bonaveeict.com.ng",
        "demo_label": "LIVE DEMO"
    },
    {
        "id": "bcm-portfolio",
        "badge": "Personal Portfolio",
        "title": "BCM Portfolio",
        "description": (
            "My personal portfolio site built to show my profile, skills, projects and contact."
        ),
        "image": "images/project-erp.jpg",
        "specs": [
            {"label": "Back-End", "value": "Python, Flask"},
            {"label": "Front-End", "value": "HTML/CSS, JavaScript"}
        ],
        "demo_url": "/",
        "demo_label": "LIVE DEMO",
        "source_url": "https://github.com/bonaventurechinoso-code/portfolio"
    }
]

EDUCATION = [
    {
        "id": "hnd",
        "badge": "ACADEMIC DEGREE",
        "badge_style": "border-primary/40 text-primary bg-primary/10",
        "status": "Completed with Distinction",
        "title": "Higher National Diploma (HND) in Computer Science",
        "institution": "Federal Polytechnic Oko",
        "description": (
            "Advanced coursework in distributed systems analysis, relational database normalization, "
            "high-level computer network protocols, advanced algorithms, and software testing lifecycles."
        ),
        "tags": ["Systems Analysis", "Database Design", "Algorithms", "Network Systems"]
    },
    {
        "id": "nd",
        "badge": "FOUNDATIONAL DIPLOMA",
        "badge_style": "border-secondary/40 text-secondary bg-secondary/10",
        "status": "Computer Science",
        "title": "National Diploma (ND) in Computer Science",
        "institution": "Federal Polytechnic Oko",
        "description": (
            "Intensive foundation in procedural and object-oriented programming fundamentals, computational logic, "
            "data structures, discrete mathematics, and software lifecycle principles."
        ),
        "tags": ["OOP Fundamentals", "Logic Design", "Data Structures", "Software Lifecycle"]
    },
    {
        "id": "practicum",
        "badge": "PROFESSIONAL IMMERSION",
        "badge_style": "border-tertiary/40 text-tertiary bg-tertiary/10",
        "status": "Full-Stack Practicum",
        "title": "Hands-on Diploma in Software Engineering",
        "institution": "SEDI, Nsugbe College of Education",
        "description": (
            "Rigorous project-driven immersion in production software engineering workflows, modern MVC backend "
            "development with Python/Django, database query tuning, and responsive UI integration."
        ),
        "tags": ["Production Coding", "Full-Stack Architecture", "Clean Architecture", "Practical DevOps"]
    }
]

SOCIAL_LINKS = [
    {
        "id": "email",
        "title": "Direct Email",
        "value": "bonaventure.chinoso@gmail.com",
        "href": "mailto:bonaventure.chinoso@gmail.com",
        "icon": "mail",
        "icon_bg": "bg-primary-container/10 text-primary-container",
        "action_icon": "arrow_forward"
    },
    {
        "id": "whatsapp",
        "title": "WhatsApp Instant",
        "value": "Available for quick chats",
        "href": "https://wa.me/",
        "icon": "chat",
        "icon_bg": "bg-[#0bda57]/10 text-[#0bda57]",
        "action_icon": "open_in_new"
    },
    {
        "id": "linkedin",
        "title": "LinkedIn Network",
        "value": "Connect professionally",
        "href": "https://linkedin.com",
        "icon": "badge",
        "icon_bg": "bg-primary-container/10 text-primary-container",
        "action_icon": "open_in_new"
    },
    {
        "id": "github",
        "title": "GitHub Profile",
        "value": "@bonaventurechinoso-code",
        "href": "https://github.com/bonaventurechinoso-code",
        "icon": "terminal",
        "icon_bg": "bg-surface-container-highest text-white",
        "action_icon": "open_in_new"
    }
]
