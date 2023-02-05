# vChat

## Description 
A Group video calling application using the Agora Web SDK with a Django backend.

##  How to use this source code

#### 1 - Clone repo
```
git clone https://github.com/Dhruvin711/vChat
```

#### 2 - Install requirements
```
cd vChat
pip install -r requirements.txt
```

#### 3 - Update Agora credentals
In order to use this project, replace the agora credentials like `appId` & `appCertificate` in `views.py` and `streams.js` with your agora credentials.

###### views.py
```
def getToken(request):
    appId = "YOUR_APP_ID"
    appCertificate = "YOUR_APP_CERTIFICATE"
    ......
```

###### streams.js
```
....
const APP_ID = 'YOUR_APP_ID'
....
```


#### 4 - Start server
```
python manage.py runserver
```
