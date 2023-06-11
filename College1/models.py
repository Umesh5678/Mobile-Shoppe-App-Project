from django.db import models

# Create your models here.


#navbar field  --->
class Navbar_Field(models.Model):
    sitelogo    = models.CharField(max_length=15)
    nav_field_1 = models.CharField(max_length=15)
    nav_field_2 = models.CharField(max_length=15)
    nav_field_3 = models.CharField(max_length=15)
    nav_field_4 = models.CharField(max_length=15)
    nav_field_5 = models.CharField(max_length=15)
    nav_field_6 = models.CharField(max_length=15)
    nav_field_7 = models.CharField(max_length=15)
    login_icon  = models.ImageField(upload_to="static/image1/navbar/")
    cart_icon   = models.ImageField(upload_to="static/image1/navbar/")


#slider images  -->
class Slider_Field(models.Model):
    caroasel_tag   = models.TextField()
    caroasel_image = models.ImageField(upload_to="static/image1/courasel_images/")
    caroasel_text  = models.CharField(max_length=40)


#brand section --->
class Brands_Model(models.Model):
    image = models.ImageField(upload_to="static/image1/brand_images/")



#footer part ---> 
class Footer_Model_services(models.Model):
    services = models.CharField(max_length=50)

class Social_Site_link(models.Model):
    link_name = models.CharField(max_length=20)


    

#about page -->

class About_Model(models.Model):
    image = models.ImageField(upload_to="static/image1/about_page/")
    para1 = models.TextField()
    para2 = models.TextField()

class About_team(models.Model):
    image = models.ImageField(upload_to="static/image1/about_page/team_images")
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=200)



#contact us page  -->

class Contact_model(models.Model):
    address = models.TextField()
    tel_no  = models.CharField(max_length=15)
    info_link = models.TextField()
    opening_hours = models.TextField()

class Contact_Response_Model(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    msg = models.TextField()
    

#mobile products   --->

class Product_Model(models.Model):
    product_type = models.CharField(max_length=20,null=True)
    product_image = models.ImageField(upload_to="static/image1/mobile_images/")
    product_name  = models.CharField(max_length=50)
    product_rate  = models.FloatField()
    product_color  = models.CharField(max_length=20,null=True)
    product_description = models.TextField(null=True)
    product_info  = models.TextField(null=True)
    product_policy = models.TextField(null=True)
    product_shipping = models.TextField(null=True)
    product_feature1 = models.CharField(max_length=100,null=True)
    product_feature2 = models.CharField(max_length=100,null=True)
    product_feature3 = models.CharField(max_length=100,null=True)
    product_feature4 = models.CharField(max_length=100,null=True)
    product_quantity = models.IntegerField(null=True)
    product_add_date = models.DateField(null=True)


#cart Model  -->

class Cart_Model(models.Model):
    product_type        = models.CharField(max_length=20)
    product_image       = models.ImageField(upload_to="static/image1/temp/")
    product_name        = models.CharField(max_length=50)
    product_rate        = models.FloatField()
    product_color       = models.CharField(max_length=20)
    product_description = models.TextField()
    product_info        = models.TextField()
    product_policy      = models.TextField()
    product_shipping    = models.TextField()
    product_feature1    = models.CharField(max_length=100)
    product_feature2    = models.CharField(max_length=100)
    product_feature3    = models.CharField(max_length=100)
    product_feature4    = models.CharField(max_length=100)
    # product_quantity = models.IntegerField(null=True)
    
    



    



#login page  -->

class Login_Model(models.Model):
    image = models.ImageField(upload_to="static/image1/login_page/")
    

#signup page -->
class Signup_Form(models.Model):
    email        = models.EmailField(max_length=50)
    password     = models.CharField(max_length=20)
    re_password  = models.CharField(max_length=20)
    country      = models.CharField(max_length=15)
    fname        = models.CharField(max_length=15)
    lname        = models.CharField(max_length=15)
    address      = models.TextField()


#chat Model  --->

class Chat_Model(models.Model):
    message = models.CharField(max_length=500 ,null=True)



    


    