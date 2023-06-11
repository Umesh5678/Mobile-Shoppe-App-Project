from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import  About_Model, About_team, Cart_Model, Chat_Model, Contact_Response_Model, Contact_model, Footer_Model_services, Login_Model, Navbar_Field, Product_Model
from .models import Signup_Form, Slider_Field
from .models import Brands_Model, Social_Site_link
# Create your views here.

def delete_session(request):
    try:
        del request.session['user_id']
    except:
        pass
    return redirect('/')


#home page  -->
def home(request):
    if(request.session.has_key('user_id')):
        
        navbar          = Navbar_Field.objects.all()
        caurosel        = Slider_Field.objects.all()
        brand           = Brands_Model.objects.all()
        footer_services = Footer_Model_services.objects.all()
        social_links    = Social_Site_link.objects.all()
        mobile          = Product_Model.objects.filter(product_type = "mobile").values()
        tablet          = Product_Model.objects.filter(product_type = "tablet").values()
        accessories     = Product_Model.objects.filter(product_type = "accessories").values()
        print(request.session['user_id'])
        user = request.session['user_id']
        obj = { 'navbar'     : navbar,
                'caurosel'   :caurosel,
                'brand'      :brand,
                'services'   :footer_services,
                'links'      :social_links,
                'user'       :user,
                'mobile'     :mobile,
                'tablet'     :tablet,
                'accessories': accessories
           }
        
        return render(request,"index.html",obj)  
    else:
        print("else")
        navbar          = Navbar_Field.objects.all()
        caurosel        = Slider_Field.objects.all()
        brand           = Brands_Model.objects.all()
        footer_services = Footer_Model_services.objects.all()
        social_links    = Social_Site_link.objects.all()
        mobile          = Product_Model.objects.filter(product_type = "mobile").values()
        tablet          = Product_Model.objects.filter(product_type = "tablet").values()
        accessories     = Product_Model.objects.filter(product_type = "accessories").values()
        obj = { 'navbar'     : navbar,
                'caurosel'   :caurosel,
                'brand'      :brand,
                'services'   :footer_services,
                'links'      :social_links,
                'mobile'     :mobile,
                'tablet'     :tablet,
                'accessories': accessories
           }
        return render(request,'index.html',obj)

         
    

def about(request):
    if(request.session.has_key('user_id')):
        navbar           = Navbar_Field.objects.all()
        caurosel         = Slider_Field.objects.all()
        footer_services  = Footer_Model_services.objects.all()
        social_links     = Social_Site_link.objects.all()
        about_page_field = About_Model.objects.all()
        team             = About_team.objects.all()
        print(request.session['user_id'])
        user = request.session['user_id']
        obj = { 'navbar'          : navbar,
                'caurosel'        :caurosel,
                'services'        :footer_services,
                'links'           :social_links,
                'about_page_field':about_page_field,
                'team'            : team,
                'user'            : user

            }
        return render(request,'about.html',obj)
    else:
        navbar           = Navbar_Field.objects.all()
        caurosel         = Slider_Field.objects.all()
        footer_services  = Footer_Model_services.objects.all()
        social_links     = Social_Site_link.objects.all()
        about_page_field = About_Model.objects.all()
        team             = About_team.objects.all()
        obj = { 'navbar'          : navbar,
                'caurosel'        :caurosel,
                'services'        :footer_services,
                'links'           :social_links,
                'about_page_field':about_page_field,
                'team'            : team

            }
        return render(request,'about.html',obj)


    

def contact(request):
    if(request.session.has_key('user_id')):
        navbar          = Navbar_Field.objects.all()
        caurosel        = Slider_Field.objects.all()
        footer_services = Footer_Model_services.objects.all()
        social_links    = Social_Site_link.objects.all()
        contact_us      = Contact_model.objects.all()
        print(request.session['user_id'])
        user = request.session['user_id']
        obj = { 'navbar'      : navbar,
                'caurosel'    :caurosel,
                'services'    :footer_services,
                'links'       :social_links,
                'contact_info':contact_us,
                'user'        :user
            }
        return render(request,'contact.html',obj)
    else:
        navbar          = Navbar_Field.objects.all()
        caurosel        = Slider_Field.objects.all()
        footer_services = Footer_Model_services.objects.all()
        social_links    = Social_Site_link.objects.all()
        contact_us      = Contact_model.objects.all()
        obj = { 'navbar'      : navbar,
                'caurosel'    :caurosel,
                'services'    :footer_services,
                'links'       :social_links,
                'contact_info':contact_us
            }
        return render(request,'contact.html',obj)


#Contact response Model  -->


def save_response(req):
    if(req.session.has_key('user_id')):
        response = Contact_Response_Model()
        response.name = req.POST['name']
        response.email = req.POST['email']
        response.msg = req.POST['msg']
        done = response.save()
        print(done)
        
        obj = {
            'done':done
            
        }
        return redirect('/contact',obj)
    else:
        response = Contact_Response_Model()
        response.name = req.POST['name']
        response.email = req.POST['email']
        response.msg = req.POST['msg']
        done = response.save()
        obj = {
            'done':done
            
        }
        return redirect('/contact',obj)



    






def shopall(request):
    if(request.session.has_key('user_id')):
        navbar          = Navbar_Field.objects.all()
        footer_services = Footer_Model_services.objects.all()
        social_links    = Social_Site_link.objects.all()
        product         = Product_Model.objects.all()
        print(request.session['user_id'])
        user = request.session['user_id']
        obj = { 'navbar'  : navbar,
                'services':footer_services,
                'links'   :social_links,
                'product' :product,
                'user'    :user
           
           }
        return render(request,'shopall.html',obj)
    else:
        navbar          = Navbar_Field.objects.all()
        footer_services = Footer_Model_services.objects.all()
        social_links    = Social_Site_link.objects.all()
        product         = Product_Model.objects.all()
        obj = { 'navbar'    : navbar,
                'services'  :footer_services,
                'links'     :social_links,
                'product'   :product
           
           }
        return render(request,'shopall.html',obj)
        
       
     
     
    

def mobile(request):
    if(request.session.has_key('user_id')):
        navbar          = Navbar_Field.objects.all()
        footer_services = Footer_Model_services.objects.all()
        social_links    = Social_Site_link.objects.all()
        product         = Product_Model.objects.filter(product_type = "mobile").values()
        print(request.session['user_id'])
        user = request.session['user_id']
        obj = { 'navbar'    : navbar,
                'services'  :footer_services,
                'links'     :social_links,
                'product'   :product,
                'user'      :user
            
            }
        return render(request,'mobile.html',obj)
    else:
        navbar          = Navbar_Field.objects.all()
        footer_services = Footer_Model_services.objects.all()
        social_links    = Social_Site_link.objects.all()
        product         = Product_Model.objects.filter(product_type = "mobile").values()
        obj = { 'navbar'    : navbar,
                'services'  :footer_services,
                'links'     :social_links,
                'product'   :product
            
            }
        return render(request,'mobile.html',obj)
 
         
     


def tablet(request):
    if(request.session.has_key('user_id')):
        navbar          = Navbar_Field.objects.all()
        footer_services = Footer_Model_services.objects.all()
        social_links    = Social_Site_link.objects.all()
        product         = Product_Model.objects.filter(product_type = "tablet").values()
        print(request.session['user_id'])
        user = request.session['user_id']
        obj = { 'navbar'    : navbar,
                'services'  :footer_services,
                'links'     :social_links,
                'product'   :product,
                'user'      :user
            
            }
        
        return render(request,'tablet.html',obj)
    else:
        navbar          = Navbar_Field.objects.all()
        footer_services = Footer_Model_services.objects.all()
        social_links    = Social_Site_link.objects.all()
        product         = Product_Model.objects.filter(product_type = "tablet").values()
        obj = { 'navbar'    : navbar,
                'services'  :footer_services,
                'links'     :social_links,
                'product'   :product
            
            }
        return render(request,'tablet.html',obj)

         
     


def accessories(request):
    if(request.session.has_key('user_id')):
        navbar          = Navbar_Field.objects.all()
        footer_services = Footer_Model_services.objects.all()
        social_links    = Social_Site_link.objects.all()
        product         = Product_Model.objects.filter(product_type = "accessories").values()
        print(request.session['user_id'])
        user = request.session['user_id']
        obj = { 'navbar'    : navbar,
                'services'  :footer_services,
                'links'     :social_links,
                'product'   :product,
                'user'      :user
            
            }
        return render(request,'accessories.html',obj)
    else:
        navbar          = Navbar_Field.objects.all()
        footer_services = Footer_Model_services.objects.all()
        social_links    = Social_Site_link.objects.all()
        product         = Product_Model.objects.filter(product_type = "accessories").values()
        obj = { 'navbar'    : navbar,
                'services'  :footer_services,
                'links'     :social_links,
                'product'   :product
            
            }
        return render(request,'accessories.html',obj)
     
    


     


     

def product_details(request):
    if(request.session.has_key('user_id')):
        navbar          = Navbar_Field.objects.all()
        footer_services = Footer_Model_services.objects.all()
        social_links    = Social_Site_link.objects.all()
        product         = Product_Model.objects.get(id=request.GET['id'])
        print(request.session['user_id'])
        user = request.session['user_id']
        obj = { 'navbar'    : navbar,
                'services'  :footer_services,
                'links'     :social_links,
                'products'  :product,
                'user'      :user
            }
        return render(request,'product_details.html',obj)
    else:
        navbar          = Navbar_Field.objects.all()
        footer_services = Footer_Model_services.objects.all()
        social_links    = Social_Site_link.objects.all()
        product         = Product_Model.objects.get(id=request.GET['id'])
        obj = { 'navbar'    : navbar,
                'services'  :footer_services,
                'links'     :social_links,
                'products'  :product
            }
        return render(request,'product_details.html',obj)

    



def login(request):

    login = Login_Model.objects.all()
    obj = { 'login_details': login
           }
    return render(request,'login.html',obj)

def dologin(req):
     userdet = Signup_Form.objects.filter(
                                            email = req.POST['email'],
                                            password = req.POST['password']
                                            )
     if(len(userdet)>0):
        print(userdet[0].email)
        print(userdet[0].id)
        req.session['user_id'] = userdet[0].email
        return redirect('/')
     else:
        return HttpResponse("<script> alert('login failed'); history.back(); </script> ")
    
   


def signup(request):
    return render(request,'signup.html')

#for stored signup information in database :
def signup_Form(request):
    
    
    new_bill = Signup_Form(
        email       = request.POST['email'],
        password    = request.POST['password'],
        re_password = request.POST['rpassword'],
        country     = request.POST['country'],
        fname       = request.POST['fname'],
        lname       = request.POST['lname'],
        address     = request.POST['address']
        
    )

    message = {'message':True}
    done = {'done':True}


    if new_bill.password  != new_bill.re_password:
            
            return render(request,'signup.html',message)
    else:
         new_bill.save()
         return HttpResponse("<script>alert('Successfully Registred ');location.href='/login'</script>")
         


def cart(req):
    if(req.session.has_key('user_id')):
        print(req.session['user_id'])
        
        user = req.session['user_id']
        temp =Product_Model.objects.get(id=req.GET['id'])
        print(temp)
        
        
        cart = Cart_Model(     
                            product_type        = temp.product_type ,
                            product_image       = temp.product_image,
                            product_name        = temp.product_name,
                            product_rate        = temp.product_rate,
                            product_color       = temp.product_color,
                            product_description = temp.product_description,
                            product_info        = temp.product_info,
                            product_policy      = temp.product_policy,
                            product_shipping    = temp.product_shipping,
                            product_feature1    = temp.product_feature1,
                            product_feature2    = temp.product_feature2,
                            product_feature3    = temp.product_feature3,
                            product_feature4    = temp.product_feature4   
                        )
        
        cart.save()
        if user :
            cart = Cart_Model.objects.all()
            
        
            obj = {
                'cart': cart,
                'user': user
            }
            return render(req,'cart.html',obj)
        
    else:
        return HttpResponse("<script>alert('You Need to login to Add Product in Cart ! ');location.href='/login'</script>")


def chat_msg(req):
    message = Chat_Model(
        message = req.POST['chat_msg']
    )
    
    message.save()
    return HttpResponse("<script>alert('Thanks for contact Successfully stored your responsed !  we will get back to you soon! ');location.href='/'</script>")

    
  