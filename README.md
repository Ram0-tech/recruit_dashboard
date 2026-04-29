# Student Recruitment Dashboard

A simple, locally-hosted web dashboard for managing student recruitment. Built using Python, Django, and Bootstrap, this application allows users to add prospective students and filter them based on their course interests.

## Features

- **Add Students**: A form to input a student's name, email, course interest, and recruitment status (Applied, Interviewing, Accepted, Rejected).
- **Search & Filter**: A dashboard list view that allows filtering students by their course interest.
- **Built-in Admin Panel**: Managed via Django's default SQLite admin system.

## Setup Instructions

1. **Activate the virtual environment**:
   ```powershell
   .\venv\Scripts\activate
   ```
2. **Apply migrations** (if not already done):
   ```powershell
   python manage.py migrate
   ```
3. **Start the development server**:
   ```powershell
   python manage.py runserver
   ```
4. **Access the application**: Navigate to `http://127.0.0.1:8000/` in your browser.

---

## AI Development Log

This project was built entirely through pair-programming with the **Antigravity AI Assistant** (powered by Gemini 3.1 Pro).

### AI Tools & Prompts Used

**AI Tool**: Antigravity Assistant

**Initial Prompt**: 
> "Build a simple web dashboard for student recruitment using Python/Django + your favorite AI tool... Requirements (1-2 hours): Django project with SQLite DB. Model: Student (fields: name, email, course_interest, status). Views/Pages: Form to add new student. List view of all students with search/filter by course_interest. Basic styling optional (Bootstrap ok). Steps to Follow: Create project... startapp students... Use AI tools for code gen... Test: Add 2-3 students, search/filter works."

**Refactoring Prompt**:
> "npx skills add https://github.com/mindrally/skills --skill django-python ... rewrite the whole program with that skill"

### Manual Changes

Very few manual code changes were required as the AI autonomously generated the models, views, forms, and templates. However, manual intervention was required for:
1. **GitHub Publishing**: Manually authenticating and running the `git remote add origin` and `git push` commands to upload the local repository to GitHub.
2. **Command Line Execution**: Bypassing standard `python` commands by explicitly invoking the virtual environment executable (`.\venv\Scripts\python.exe`) to prevent global namespace conflicts.

### Challenges Faced

1. **Git Path & Environment Issues (`spawn git ENOENT`)**: 
   When attempting to install an external AI development skill (`django-python`) via `npx`, the process failed because Git was not installed on the system. 
2. **Terminal State Synchronization**: 
   Even after the AI automatically installed Git via `winget`, the active PowerShell session did not immediately recognize the updated system `PATH`. To resolve this, we had to dynamically append the Git path to the active terminal session (`$env:Path = $env:Path + ";C:\Program Files\Git\cmd"`) to successfully clone the skill repository and push the code to GitHub.
3. **Virtual Environment Context**: 
   Running `python manage.py runserver` initially threw a `ModuleNotFoundError` for Django because the terminal had not activated the `venv`. This was resolved by directly executing the python binary from within the `venv/Scripts` directory.
