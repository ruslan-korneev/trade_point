# Test Task

# Deploy App
```bash
# clone repo
git clone git@github.com:shaggy-axel/trade_point.git && cd trade_point/

# create virtualenv and activate
python3 -m venv .venv
. .venv/bin/activate

# install requirements
pip install -U pip
pip install -r requirements.txt

# migrate, create superuser and some test users, runserver
python src/manage.py migrate
python src/manage.py create_test_employees
python src/manage.py runserver
```
