from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth.models import UserManager,AbstractBaseUser,PermissionsMixin
# Create your models here.
class users(UserManager):
    def _create_user(self,email,password,**extrafields):
        if not email:
            raise ValueError("Please enter an valid e-mail id")
        email = self.normalize_email(email)
        user = self.model(email=email,**extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email, password=None,**extrafields):
        extrafields.setdefault("is_staff",False)
        extrafields.setdefault("is_superuser",False)
        return self._create_user(email,password,**extrafields)
    def update_password(self,email,password):
        user = self.get(email=email)
        user.set_password(password)
        user.save(using=self._db)
    def create_superuser(self,email, password= None,**extrafields):
        extrafields.setdefault("is_staff",True)
        extrafields.setdefault("is_superuser",True)
        return self._create_user(email,password,**extrafields)
class BooleanCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(BooleanCharField, self).__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value == 'y':
            return True
        elif value == 'n':
            return False
        return None

    def to_python(self, value):
        if value == 'y':
            return True
        elif value == 'n':
            return False
        return None

    def get_prep_value(self, value):
        if value:
            return 'y'
        return 'n'

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(primary_key=True)

    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    date_field=models.DateTimeField(default=timezone.now)
    last_login=models.DateField(blank=True,null=True)

    objects=users()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

class Userdata(models.Model):
    usermail = models.ForeignKey(User, verbose_name=_("User Infromation"), on_delete=models.CASCADE)
    GENDER_CHOICES = (
        ('M', 'Homme'),
        ('F', 'Femme'),
    )
    name = models.CharField(_("Name"), max_length=50)
    rollnumber =models.CharField(_("RollNo."), max_length=10,unique=True)
    gender = models.CharField(_("Gender"), max_length=1,choices=GENDER_CHOICES)
    branch = models.CharField(_("Branch"), max_length=10)
    section = models.CharField(_("Section"), max_length=50)
    libraryid = models.CharField(_("Library ID"), max_length=50)
class Book(models.Model):
    AccessionNumber = models.CharField(max_length = 100,primary_key = True)
    TitleId = models.CharField(max_length=10,null = True)
    TitleName = models.CharField(max_length=250,null = True)
    AllowLend = models.BooleanField(max_length=1,default=True)
    AuthorName = models.CharField(max_length=100,blank = True,null = True)
    AuthorId = models.CharField(max_length=10,blank = True,null = True)
    SupplierName = models.CharField(max_length=100,blank = True,null = True)
    ClassificaNumber = models.CharField(max_length=20,blank = True,null = True)

    def __str__(self):
        return self.TitleName
    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
class BookLending(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    lending_time = models.DateTimeField(default=timezone.now)
    return_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f'{self.user.email} -> {self.book.TitleName}'