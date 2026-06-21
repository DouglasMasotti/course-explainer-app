# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies (uses uv)
uv pip install -r requirements.txt

# Run development server (debug mode, auto-reload)
python src/app.py
# → http://127.0.0.1:5000

# Run all tests
python -m unittest discover -s tests

# Run a specific test case
python -m unittest tests.test_app.AppTestCase.test_index
```

## Architecture

Flask app with a flat `src/` layout — no blueprints.

- `src/app.py` — creates the Flask app, registers two routes: `GET /` → `index()` and `GET /course/<course_id>` → `course(course_id)`
- `src/views.py` — view functions; renders templates
- `src/models.py` — `Course` class and a hardcoded `courses` list (3 items)
- `src/templates/` — Jinja2 templates
- `tests/test_app.py` — inserts `src/` into `sys.path` to import `app` directly

## Known Bugs

The codebase has several issues that any change to course display will need to address:

1. **`models.py` is unused** — `views.py` never imports it; `course()` only passes `course_id` (a string) to the template, not a `Course` object.

2. **`course.html` expects a `course` object** — the template references `course.title`, `course.description`, `course.instructor`, `course.duration`, and iterates `course.topics`. The `Course` model has no `topics` attribute, and the view doesn't pass a `Course` at all.

3. **`course.html` template inheritance is broken** — the file has a full `<html>...</html>` structure AND `{% extends 'layout.html' %}` inside `<body>`, which is invalid Jinja2 (extends must be the first tag).

4. **`index.html` uses `{% include %}` instead of `{% extends %}`** — inlines `layout.html` rather than extending it, inconsistent with how `course.html` is intended to work.
