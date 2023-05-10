"""
- What is a QuerySet?Write program to create a new Post object in database:
  QuerySets are created by using the objects attribute of a Django model. For example, 
  to retrieve all Post objects from the database, you would use the following code:


    from myapp.models import Post

    posts = Post.objects.all()

- To create a new Post object in the database, you can create a new instance of the Post 
  model and save it to the database using the save() method. Here's an example program:
  
    from myapp.models import Post

    post = Post(title='My First Post', content='This is the content of my first post')

    post.save()


- In this example, we create a new Post object with a title of 'My First Post' and some content. 
  We then call the save() method on the post object to save it to the database. 
"""