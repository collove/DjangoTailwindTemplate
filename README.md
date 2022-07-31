<p align="center">
    <img src="https://raw.githubusercontent.com/Farhaduneci/DjangoTailwindTemplate/main/.images/Icon.png">
</p>
<p align="center">
  <img src="https://repobeats.axiom.co/api/embed/395952b048f3ea06d8d2f7501940b3a1a283943c.svg">
</p>
<br>

> This project is still in its early stages of development. Any
> contributions to the repo is very welcomed. :white_heart:

Django Starter Project, Including [TailWindCSS](https://tailwindcss.com/) and all other useful modules used in my projects.

## :toolbox: Features

- Django 4.0 & Python 3.10
- Styling with [TailWindCSS](https://tailwindcss.com/)
- Complete user authentication (Log-in/Log-out, ...) via [Django Allauth](https://github.com/pennersr/django-allauth)
- Static file combine with [Django Compressor](https://django-compressor.readthedocs.io/en/)
- Strict separation of settings from code by using [Python Decouple](https://pypi.org/project/python-decouple/)
- TailWind-styled crispy forms via [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)

## :film_projector: Demo

![Demo](https://raw.githubusercontent.com/Farhaduneci/DjangoTailwindTemplate/main/.images/Demo.png)

## :scroll: How to Run

Clone the repository and follow the steps bellow:

### 1. Create a new virtual environment `.venv` for your project

```shell
virtualenv .venv && source .venv/bin/activate
```

### 2. Install the requirements

```shell
python3 -m pip install -r requirements.txt
```

```shell
python3 manage.py tailwind install
```

### 3. Create both `./config/local_settings.py` and `.env` files and write the following contents in them

```shell
touch ./config/local_settings.py && touch .env
```

```python
# local_settings.py
DEBUG = True
ALLOWED_HOSTS = []
```

Generate a new Django `SECRET_KEY` using [Djecrety](https://djecrety.ir/) and paste it in the `.env` file in the root path of the project as follows

```shell
SECRET_KEY=<COPIED SECRET_KEY HERE>
```

### 4. Create an application

Create a new Django app in your project

```shell
python3 manage.py startapp myapp
```

> Append your local application to `INSTALLED_APPS` inside `settings.py`

#### Create your URL, Template and views

You can extend your templates from `base/_base.html`

### 5. Migrate :butterfly:

You need to create migration files (if you have any changes in your
models) and run `migrate` command to apply them.

```shell
python3 manage.py makemigrations
```

```shell
python3 manage.py migrate
```

### 6. Run your local server

Start TailWindCSS by running the following command in your terminal:

```shell
python3 manage.py tailwind start
```

Then you simply need to run Django's local server:

```shell
python3 manage.py runserver
```

### 7. Start Exploring :rocket:

That's all you need to do for having a ready-to-develop Django project with some :battery: included.

## :question: How to use Crispy Forms

Current version (crispy-tailwind/0.5) allows the `|crispy` filter to be used to style your
form. In your template:

1. Load the filter: `{% load tailwind_filters %}`
2. Apply the crispy filter: `{{ form|crispy }}`

You can also use the `{% crispy %}` tag to allow usage of crispy-forms'
`FormHelper` and `Layout`. In your template:

1. Load the crispy tag: `{% load crispy_forms_tags %}`
2. Add `FormHelper` to your form and use crispy-forms to set-up your form
3. Use the crispy tag `{% crispy form %}` in your template

> Visit [Crispy Forms Documentation](https://django-crispy-forms.readthedocs.io/en/latest/index.html)
> and [crispy-tailwind](https://github.com/django-crispy-forms/crispy-tailwind)
> repository for more information.

## :rainbow: Next Steps

- Add [gunicorn](https://pypi.org/project/gunicorn/) as the production web server.
- Update the [EMAIL_BACKEND](https://docs.djangoproject.com/en/4.0/topics/email/#module-django.core.mail) and connect with a mail provider.
- Make the [admin more secure](https://opensource.com/article/18/1/10-tips-making-django-admin-more-secure).
- `django-allauth` supports [social authentication](https://django-allauth.readthedocs.io/en/latest/providers.html) if you need that.

## :tickets: Contributing

Contributions, issues and feature requests are welcome! See [CONTRIBUTING](https://github.com/farhaduneci/DjangoTailwindTemplate/blob/main/CONTRIBUTING.md).

## :star2: Support

Give the repository a :star: if you found it helpful please.

## :shield: License

This project is being licensed under the [MIT License](https://github.com/farhaduneci/DjangoTailwindTemplate/blob/main/LICENSE).

## :paperclip: Links

- I recommend you to have a :eyes: at [DjangoX](https://github.com/wsvincent/djangox), one of the best starter project repos for Django. This repository uses Bootstrap and inspired me to create what you are looking at now.
