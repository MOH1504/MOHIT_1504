"""
Why Django should be used for web-development? Explain how you
can create a project in Django? 

-Django is a popular Python web framework that is designed to make web development easier and faster. 
Here are some reasons why you should use Django for web development:

1. Rapid development: Django provides a lot of built-in features and tools that help developers to 
   create web applications quickly.

2. Security: Django comes with built-in security features that help developers to protect their web 
   applications from common web vulnerabilities such as SQL injection, cross-site scripting, and CSRF attacks.

3. Scalability: Django is highly scalable and can handle large amounts of traffic and data.

4. Community: Django has a large and active community of developers who provide support and contribute to 
   the development of the framework.
   
Now, let's see how you can create a project in Django:

1. Install Django: The first step is to install Django on your system. You can do this by running the command 
   pip install Django on your terminal or command prompt.

2. Create a new project: Once Django is installed, you can create a new project by running the command 
   django-admin startproject project_name where project_name is the name of your project.

3. Create an app: An app is a modular component of a Django project that performs a specific function. 
   To create an app, run the command python manage.py startapp app_name where app_name is the name of your app.

4. Define models: Models are used to define the structure of your database tables. You can define models in 
   the models.py file of your app.

5. Define views: Views are used to define the logic for handling HTTP requests. You can define views in the 
   views.py file of your app.

6. Define URLs: URLs are used to map HTTP requests to views. You can define URLs in the urls.py file of your app.

7. Run the server: Finally, you can run the development server by running the command python manage.py runserver. 
    This will start the server at http://localhost:8000/. You can access your app by visiting this URL in your web browser.


"""