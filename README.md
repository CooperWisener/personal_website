# Personal Website

> The personal portfolio site of Cooper Wisener — a Data Science student at the University of Wisconsin–Madison.

A lightweight **Flask** web app that serves a three-page portfolio: an *About Me* landing page, a *Projects* showcase, and a *Resume & CV* page with downloadable documents. Styled with a clean academic layout — a fixed left sidebar (photo, name, social links) and a sticky top navbar.

## Pages

- **About Me** (`/`) — intro, skills, and contact details.
- **Projects** (`/projects`) — cards for recent data science and software projects, each with a description, tech-stack tags, and a GitHub link.
- **Resume & CV** (`/resume`) — downloadable resume, full CV, and unofficial transcript, plus an education summary.

Documents are served as downloads via the `/documents/<filename>` route.

## Tech stack

- **[Flask](https://flask.palletsprojects.com/)** — routing and Jinja2 templating
- **[Gunicorn](https://gunicorn.org/)** — production WSGI server
- **HTML + CSS** — custom stylesheet, no frontend framework
- **[Font Awesome](https://fontawesome.com/)** — icons (via CDN)
- **[Render](https://render.com/)** — hosting (config in `render.yaml`)

## Running locally

Requires **Python 3.11+**.

```bash
git clone https://github.com/CooperWisener/personal_website.git
cd personal_website
pip install -r requirements.txt
python app.py
```

The dev server runs at `http://127.0.0.1:5000`.

## Deployment

The site deploys to **Render** as a web service. The configuration in [`render.yaml`](render.yaml) installs dependencies and serves the app with Gunicorn:

```bash
gunicorn app:app
```

## Project structure

```
app.py             Flask app — routes for the three pages and document downloads
render.yaml        Render deployment config
requirements.txt   Python dependencies (Flask, Gunicorn)
templates/
  base.html        Shared layout — sidebar + top navbar
  index.html       About Me page
  projects.html    Projects showcase
  resume.html      Resume & CV page
static/
  css/style.css    Site styles
  images/          Profile photo
documents/         Resume, CV, and transcript PDFs (served as downloads)
```
