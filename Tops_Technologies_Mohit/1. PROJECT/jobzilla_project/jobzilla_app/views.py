from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.core.mail import send_mail
from random import *


# Create your views here.
"""
Django support ORM

ORM :- object relation mapper 

get():- get method return object
    ->it will throw exception when it will return multiple object

filter():- filter method return queryset

all():-return queryset - fatch all data from the table.


"""
def home(request):
    if "email" in request.session:
        uid  = User.objects.get(email =  request.session['email'])
        if uid.role == "jobseeker" :
            jsid = Jobseeker.objects.get(user_id=uid)
            js_details = Jobskeer_details.objects.get(jobseeker_id=jsid)
            jall = Jobpost.objects.all()
            apall = Jobapply.objects.all()
            context={

                    "uid" : uid,
                    "jsid" : jsid,
                    "js_details" : js_details,
                    "jall" : jall,
                   
                }
            return render(request,"jobzilla_app/js_index.html",context)
        elif uid.role == "jobprovider" :
            jpid = Jobprovider.objects.get(user_id=uid)
          
            apall = Jobapply.objects.all()
            context={

                    "uid" : uid,
                    "jpid" : jpid,
                     "apll" : apall
                }
            return render(request,"jobzilla_app/jp_index.html",context)
    else:
        return render(request,"jobzilla_app/c_register.html")

def login(request):
    if "email" in request.session:
        return redirect("home")

    else:
        if request.POST:
            email =  request.POST['email']
            password =  request.POST['password']
            uid = User.objects.get(email = email)
            print("========.>uid",uid.email)
            if uid.role =="jobseeker" and uid.password == password:
                print("jobseeker")
                jsid = Jobseeker.objects.get(user_id=uid)
                js_details = Jobskeer_details.objects.get(jobseeker_id=jsid)
                if jsid:                
                    print(jsid.firstname)
                    print(jsid.lastname)
                    request.session['email'] = email #for session managmet
                    context={

                        "uid" : uid,
                        "jsid" : jsid,
                        "js_details" : js_details,

                    }
                    return render(request,"jobzilla_app/js_index.html",context)
            elif uid.role == "jobprovider" and uid.password == password:
                print("jobprovider")
                jpid = Jobprovider.objects.get(user_id=uid)
                # js_details = Jobskeer_details.objects.get(jobseeker_id=jsid)
                if jpid:                
                    print(jpid.firstname)
                    print(jpid.lastname)
                    request.session['email'] = email #for session managmet
                    context={

                        "uid" : uid,
                        "jpid" : jpid,
                        # "js_details" : js_details,

                    }
                    return render(request,"jobzilla_app/jp_index.html",context)
        return render(request,"jobzilla_app/c_register.html")

        
def c_register(request):
    if request.POST:
        role = request.POST['role']
        if role == "jobseeker":
            email =  request.POST['email']
            mylist = ["dsvvsdvs","sdfsdfsdfc","DSdsffdf","dsvcdscfdcc"]
            mypass = email[ 3:6 ] + choice(mylist)
            uid =User.objects.create(email=email,
                                     password= mypass,
                                     role = role 
                                    )
            jsid = Jobseeker.objects.create(user_id = uid,
                                            firstname = request.POST['firstname'],
                                            lastname = request.POST['lastname'],
                                            city = request.POST['city'],
                                            contact_no = request.POST['contect_no'],
                                            gender= request.POST['gender'])
            Jsid_details =  Jobskeer_details.objects.create(user_id= uid , jobseeker_id= jsid)
            send_mail("AUTENTICATION", "Your one time password is :-"+ mypass,"dholakiyaharsh789@gmail.com", [email] )
            context = {
                'smsg' : "Successfully account created"
            }
            print("================>jobseeker submited") 
            return render(request,"jobzilla_app/c_register.html",context)   
 
        elif role == "jobprovider":
            email =  request.POST['email']
            mylist = ["dsvvsdvs","sdfsdfsdfc","DSdsffdf","dsvcdscfdcc"]
            mypass = email[ 3:6 ] + choice(mylist)
            uid =User.objects.create(email=email,
                                     password= mypass,
                                     role = role 
                                    )
            jpid = Jobprovider.objects.create(user_id = uid,
                                              company_name = request.POST['company_name'],
                                              country = request.POST['country'],
                                              city = request.POST['city'],
                                              address = request.POST['address'],
                                              contact_no = request.POST['contact_no'],
                                           )
            send_mail("AUTENTICATION", "Your one time password is :-"+ mypass,"dholakiyaharsh789@gmail.com", [email] )
            context = {
                'smsg' : "Successfully account created"
            }
            print("================>jobseeker submited") 
            return render(request,"jobzilla_app/c_register.html",context)    
        else:
            return redirect("c_register")
               
    else:
        print("===========>not submited")
        return render(request,"jobzilla_app/c_register.html")

def companies_panel(request):
    call = Jobprovider.objects.all()
    context= {
        'call' : call,
    }
    return render(request,"jobzilla_app/companies.html",context)

def user_profile(request):
    if "email" in request.session:
        uid  = User.objects.get(email =  request.session['email'])
        if uid.role == "jobseeker" :
            jsid = Jobseeker.objects.get(user_id=uid)
            js_details = Jobskeer_details.objects.get(jobseeker_id=jsid)
            context={

                    "uid" : uid,
                    "jsid" : jsid,
                    "js_details" : js_details,
                }
            return render(request,"jobzilla_app/profile-edit.html",context)
    else:
          return redirect('login')
    
def user_profile_jp(request):
     if "email" in request.session:
        uid  = User.objects.get(email =  request.session['email'])
        if uid.role == "jobprovider" :
            jpid = Jobprovider.objects.get(user_id=uid)

            context={

                    "uid" : uid,
                    "jpid" : jpid,
            }
          
            return render(request,"jobzilla_app/profile-edit-jp.html",context)

def logout(request):
    if "email" in request.session:
        print("logout") 
        del request.session['email']
        return render(request,"jobzilla_app/c_register.html")
    else:
        return redirect('login')
    


def change_profile_js(request):
    if "email" in request.session:
        uid  = User.objects.get(email =  request.session['email'])
        if uid.role == "jobseeker" :
            jsid = Jobseeker.objects.get(user_id=uid)
            js_details = Jobskeer_details.objects.get(jobseeker_id=jsid)
        if request.POST:
            jsid.firstname = request.POST['firstname']
            jsid.lastname = request.POST['lastname']
            if "profilepic" in request.FILES:
                pic =  request.FILES['profilepic']
                jsid.profile_pic =  pic
                jsid.save()
            jsid.save()  
            
            context={

                        "uid" : uid,
                        "jsid" : jsid,
                        "js_details" : js_details,
                    }
            return render(request,"jobzilla_app/profile-edit.html",context)
    

def change_profile_jp(request):
    if "email" in request.session:
        uid  = User.objects.get(email =  request.session['email'])
        if uid.role == "jobprovider" :
            jpid = Jobprovider.objects.get(user_id=uid)
            #js_details = Jobskeer_details.objects.get(jobseeker_id=jsid)
        if request.POST:
            jpid.company_name = request.POST['company_name']
           
            if "profilepic" in request.FILES:
                pic =  request.FILES['profilepic']
                jpid.profile_pic =  pic
                jpid.save()
            jpid.save()  
            
            context={

                        "uid" : uid,
                        "jpid" : jpid,
                      #  "js_details" : js_details,
                    }
            return render(request,"jobzilla_app/profile-edit-jp.html",context)

def change_account_js(request):
    if "email" in request.session:
        uid  = User.objects.get(email =  request.session['email'])
        if uid.role == "jobseeker" :
            jsid = Jobseeker.objects.get(user_id=uid)
            js_details = Jobskeer_details.objects.get(jobseeker_id=jsid)
            if request.POST:
                jsid.git_url = request.POST['githuburl']
                jsid.linked_in =request.POST['linkedin']
                jsid.save()
                context={
                            "uid" : uid,
                            "jsid" : jsid,
                            "js_details" : js_details,
                    }
                print("====> js git url updation ",jsid.git_url)
                return render(request,"jobzilla_app/profile-edit.html",context)   

def change_account_jp(request):
    if "email" in request.session:
        uid  = User.objects.get(email =  request.session['email'])
        if uid.role == "jobprovider" :
            jpid = Jobprovider.objects.get(user_id=uid)
            #js_details = Jobskeer_details.objects.get(jobseeker_id=jsid)
            if request.POST:
                jpid.country= request.POST['country']
                jpid.linked_in =request.POST['linkedin']
                jpid.save()
                
              
                context={
                            "uid" : uid,
                            "jpid" : jpid,
                            #"js_details" : js_details,
                    }
               
                return render(request,"jobzilla_app/profile-edit-jp.html",context)    
 
def job_apply(request,id):
    if "email" in request.session:
        uid  = User.objects.get(email =  request.session['email'])
        if uid.role == "jobseeker" :
            jsid = Jobseeker.objects.get(user_id=uid)
            js_details = Jobskeer_details.objects.get(jobseeker_id=jsid)
            job_post_id= Jobpost.objects.get(id = id)
            print("=========================>jobpost id",job_post_id)
            print("==========>id",id)
            jaid =  Jobapply.objects.create(user_id= uid,jobseeker_id= jsid, jobseeker_details_id=js_details,  jobpost_id=  job_post_id,status="Apply")
       
        return redirect("home")

def change_password_js(request):
    if "email" in request.session:
        uid  = User.objects.get(email =  request.session['email'])
        if uid.role == "jobseeker" :
            jsid = Jobseeker.objects.get(user_id=uid)
            js_details = Jobskeer_details.objects.get(jobseeker_id=jsid)
            if request.POST:
                currentpassword = request.POST['currentpassword']
                newpassword = request.POST['newpassword']

                if uid.password == currentpassword:
                    uid.password = newpassword
                    uid.save()
                    return redirect("logout")
                else:
                    pass

                context={
                            "uid" : uid,
                            "jsid" : jsid,
                            "js_details" : js_details,
                    }
                return render(request,"jobzilla_app/profile-edit-jp.html",context)
            else:
               
                context={
                            "uid" : uid,
                            "jsid" : jsid,
                            "js_details" : js_details,
                    }
                return render(request,"jobzilla_app/profile-edit-jp.html",context)
    
def change_password_jp(request):
     if "email" in request.session:
        uid  = User.objects.get(email =  request.session['email'])
        if uid.role == "jobprovider" :
            jpid = Jobprovider.objects.get(user_id=uid)
           
            if request.POST:
                currentpassword = request.POST['currentpassword']
                newpassword = request.POST['newpassword']

                if uid.password == currentpassword:
                    uid.password = newpassword
                    uid.save()
                    return redirect("logout")
                else:
                    pass

                context={
                            "uid" : uid,
                            "jpid" : jpid,
                           
                    }
                return render(request,"jobzilla_app/profile-edit-jp.html",context)
            else:
               
                context={
                            "uid" : uid,
                            "jpid" : jpid,
                   
                    }
                return render(request,"jobzilla_app/profile-edit-jp.html",context)
    
def forgot_password(request):
    if request.POST: 
        email = request.POST['email']
        otp = randint(1111,9999)

        try:
            uid = User.objects.get(email = email)
            uid.otp = otp
            uid.save()
            send_mail("Forgot password","Your otp is "+str(otp),"dholakiyaharsh789@gmail.com",[email])
            context = {
                'email' : email
            }

            return render(request,"jobzilla_app/change-password.html",context)
        except:
            context = {
                "emsg" : "Invalid email address"
            }
            return render(request,"jobzilla_app/forgot-password.html",context)
    return render(request,"jobzilla_app/forgot-password.html")
    
def change_password(request):
    if request.POST:
        email = request.POST['email']
        otp = request.POST['otp']
        newpassword = request.POST['newpassword']
        confirmpassword = request.POST['confirmpassword']
        print("--------------->>>email",email)
        uid = User.objects.get(email = email)
        print("--------------->>>email",email)
        if str(uid.otp) == otp:
            if newpassword == confirmpassword:
                uid.password = newpassword
                uid.save()
                context = {
                    "email" : email,
                    "smsg" : "Password successfully changed"
                }
                return render(request,"jobzilla_app/c_register.html",context)
            else:
                emsg = "Invalid password"
                context = {
                    "email" : email,
                    "emsg" : emsg
                }
                return render(request,"jobzilla_app/change-password.html",context)
        else:
            emsg = "Invalid Otp"
            context = {
                    "email" : email,
                    "emsg" : emsg
            }
            return render(request,"jobzilla_app/change-password.html",context)
        