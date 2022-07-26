<p align="center">
    <img src="https://raw.githubusercontent.com/Farhaduneci/DjangoTailwindTemplate/main/.github_components/Icon.png" width="140">
    <h3 align="center">Django :heavy_plus_sign: TailWindCSS</h3>
</p>

<br>

Django Starter Project, Including [TailWindCSS](https://tailwindcss.com/) and all other useful modules used in my projects.

## :toolbox: Features

- Django 4.0 & Python 3.10
- Styling with [TailWindCSS](https://tailwindcss.com/)
- Static File Combine with [Django Compressor](https://django-compressor.readthedocs.io/en/)

## :scroll: How to Run

Clone the repository and follow the steps bellow:

### 1. Install the requirments

```shell
python3 -m pip install -r requirments.txt
```

### 2. Create an application

Create a new Django app in your project

```shell
python3 manage.py startapp myapp
```

> Append your local application to `INSTALLED_APPS` inside `settings.py`

#### Create your URL, Template and views

You can extend your templates from `base.html`

#### 3. Run your local server

Start TailWindCSS by running the following command in your terminal:

```shell
python3 manage.py tailwind start
```

Then you simply need to run Django's local server:

```shell
python3 manage.py runserver
```

### 4. Start Exploring :rocket

That's all you need to do for having a ready-to-develop Django project with some :battery: included.

## :octocat: Contributing

Contributions, issues and feature requests are welcome! See [CONTRIBUTING](https://github.com/farhaduneci/DjangoTailwindTemplate/blob/main/CONTRIBUTING.md).

## :star2: Support

Give the repository a :star: if you found it helpful please.

## :shield: License

This project is being licensed under the [MIT License](https://github.com/farhaduneci/DjangoTailwindTemplate/blob/main/LICENSE).

## :paperclip: Refrences

- The project logo is an :art: from [Ahebwe Oscar](https://morioh.com/@607d9be4925efb1381779f48)
- I recommend you to have a :eyes: at [DjangoX](https://github.com/wsvincent/djangox), one of the best starter project repos for Django. This repository uses Bootstrap and inspired me to create what you are looking at now.
