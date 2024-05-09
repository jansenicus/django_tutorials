Install and create virtual environment
```bash
pyenv install 3.12.2
python -m venv .venv
```

Activate virtual environment
```bash
./.venv/bin/Activate.ps1
```

Install package requirements
```bash
pip install -r requirements
```

Change directory
```bash
cd myproject
python manage.py createsuperuser
python manage.py migrate
python manage.py runserver
```
