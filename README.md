# Celiac's Choice - API

This is the README that provides information about the API in the Celiac's Choice project.

You can acess the API [here.](https://celiacs-api-bf52b941b62a.herokuapp.com/)

The application is developed using the Django Rest framework for the Back end and React for the Front end. 

This is the Back end part of the project, the Front end part can be found [here](https://github.com/SofiaNords/celiacs-choice).

## Table of Content

- [Celiac's Choice - API](#celiacs-choice---api)
- [Table of Content](#table-of-content)
- [Entity Relationship Diagram](#entity-relationship-diagram)
- [Technologies Used](#technologies-used)
    - [Languagaes Used](#languages-used)
    - [Database Used](#database-used)
    - [Frameworks Libraries Tools & Programs Used](#frameworks-libraries-tools--programs)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)


## Entity Relationship Diagram


## Technologies Used

Generic Views where used as a shortcut for common usage patterns.

### Languages Used

- Python


### Database Used



### Frameworks, Libraries, Tools & Programs

- [Cloudinary](https://cloudinary.com/) - Used to store images
- [Django](https://www.djangoproject.com/) - Used for rapid, reusable and secure development
- [django-allauth](https://docs.allauth.org/) - Used for authentication, registration and account management
- [Django-Filter](https://django-filter.readthedocs.io/en/stable/) - Used to add filters in search feature
- [Django REST Framework](https://www.django-rest-framework.org/) - Used for buildning Web API
- [Django REST Framework Simple-JWT](https://django-rest-framework-simplejwt.readthedocs.io/) - Used for securing DJANGO APIs using JSON Web Tokens
- [django-cors-headers](https://pypi.org/project/django-cors-headers/) - Used to handle web requests to the application
- [dj-database-url](https://pypi.org/project/dj-database-url/) - Used to configure the application and define the database connection in an url
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/) - Used for handling authentication securely
- [Git](https://git-scm.com/) - Used for version control
- [GitHub](https://github.com/) - Used to store the code
- [GitPod](https://www.gitpod.io/) - Used as the IDE for development
- [Gunicorn](https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/gunicorn/) - Used as the Web Server to run Django on Heroku
- [Heroku](https://dashboard.heroku.com/) - Used to deploy the API
- [Psycopg](https://pypi.org/project/psycopg2/) - Used as a database adapter to support the connection to database

## Testing

## Bugs

I realised that the comment I entered on one post was visible on all posts.
After troubleshooting in the frontend, I got a tip from Tutor Support to look in the backend.
It turned out that I missed to put DjangoFilterBackend in my Comment View.
After fixing this, the comments worked as they should. The comment was only visible on the 
post it was added to.

## Deployment