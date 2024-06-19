from .models import User
from django.contrib.auth.hashers import check_password
print(User.objects.filter(email="k2@k.net"))

def get_data(mail):
    data= User.objects.all()
    for i in data:
        if i.email==mail:
            return True
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
userdata = client['library']
collection = userdata['lmsapp_user']
def auth(mail,passw):
    data = (list(collection.find({'email':mail},projection={'password':1,'email':1,'_id':0})))
    if data:
        return (check_password(passw,data[0]['password']))
    return False
    


