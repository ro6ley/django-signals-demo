[![HitCount](http://hits.dwyl.io/ro6ley/django-signals-demo.svg)](http://hits.dwyl.io/ro6ley/django-signals-demo)

# Django Signals - A Sample Project

A demo Django project showcasing the use of Django Signals

This repository contains the code for this [blogpost](https://stackabuse.com/using-django-signals-to-simplify-and-decouple-code/) on [StackAbuse](https://stackabuse.com/).

## Getting Started

### Prerequisites

Kindly ensure you have the following installed on your machine:

- [ ] [Python 3](https://realpython.com/installing-python/)
- [ ] [Pipenv](https://pipenv.readthedocs.io/en/latest/)
- [ ] [Git]()
- [ ] An IDE or Editor of your choice

### Running the Application

1. Clone the repository
```
$ git clone https://github.com/ro6ley/django-signals-demo.git
```

2. Check into the cloned repository
```
$ cd django-signals-demo
```

3. If you are using Pipenv, setup the virtual environment and start it as follows:
```
$ pipenv install && pipenv shell
```

4. Install the requirements
```
$ pip install -r requirements.txt
```

4. Run the application
```
$ cd jobs_board

$ python manage.py createsuperuser

$ python manage.py runserver
```

5. Log in to the admin dhasboard and populate Jobs at http://localhost:8000/admin

6. Navigate to http://localhost:8000/jobs and subscribe

7. Check the console for events logging


## Contribution

Please feel free to raise issues using this [template](./.github/ISSUE_TEMPLATE.md) and I'll get back to you.

You can also fork the repository, make changes and submit a Pull Request using this [template](./.github/PULL_REQUEST_TEMPLATE.md).
