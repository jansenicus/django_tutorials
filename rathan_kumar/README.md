[Build Python Django Real Project: Django Web Development | Udemy](https://www.udemy.com/course/python-django-real-project-for-freshers-freelancers/)

```bash
pyenv install 3.9.18
pyenv local 3.9.18
# if using VS Code terminal, press CTRL+P for Command Pallette
# and type '>Python: Clear Cache and Reload Window'
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
django-admin startproject carzone .
```