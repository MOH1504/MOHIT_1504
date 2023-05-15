from django.db import models


# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    otp = models.IntegerField(default=456)
    created_at = models.DateTimeField(auto_now_add=True)
    is_login = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class Jobseeker(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=15)
    gender = models.CharField(max_length=20)
    git_url = models.CharField(max_length=100)
    linked_in = models.CharField(max_length=50,null=True,blank=True) 
    profile_pic = models.FileField(upload_to="media/images/",default="default.png")

    def __str__(self):
        return self.firstname

class Jobprovider(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country=models.CharField(max_length=50,null=True,blank=True)
    contact_no = models.CharField(max_length=15,null=True,blank=True)
    address =models.CharField(max_length=50,null=True,blank=True)
    linked_in = models.CharField(max_length=50,null=True,blank=True) 
    job_specification = models.CharField(max_length=60)
    profile_pic = models.FileField(upload_to="media/images/",default="default.png")

    def __str__(self):
        return self.company_name

class Jobskeer_details(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    jobseeker_id =  models.ForeignKey(Jobseeker, on_delete = models.CASCADE)
    skills = models.TextField(blank=True,null=True)
    current_position = models.CharField(max_length=50,blank=True,null=True)
    experiance = models.CharField(max_length=50,blank=True,null=True)
    qualification = models.CharField(max_length=50,blank=True,null=True)
    last_company_name = models.CharField(max_length=50,blank=True,null=True)
    college_name = models.CharField(max_length=50,blank=True,null=True)

    

class Jobpost(models.Model):
     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
     jobprovider_id = models.ForeignKey(Jobprovider, on_delete=models.CASCADE)
     job_title =  models.CharField(max_length=80)
     job_description =  models.TextField()
     job_type = models.CharField(max_length=50) # Full time or part time
     job_category = models.CharField(max_length=50) #job ,  project work 
     salary =  models.CharField(max_length=50) #approx salary
     skills = models.CharField(max_length=80) # skill specification
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return self.jobprovider_id.company_name

class Jobapply(models.Model):
     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
     jobseeker_id =  models.ForeignKey(Jobseeker,on_delete = models.CASCADE)
     jobseeker_details_id  =  models.ForeignKey(Jobskeer_details, on_delete = models.CASCADE)
     jobpost_id  = models.ForeignKey(Jobpost, on_delete=models.CASCADE )  
     status =  models.CharField(max_length=50 , default = "PENDING")
     
     def __str__(self):
        return self.user_id.email
