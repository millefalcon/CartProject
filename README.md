# CartProject
A simple cart app to store details of items.

# Pre-requisite
* python3
* django
* djangorestframework==3.11.0

# Getting Started
`pip install -r requirements.txt`

I have already created the superuser and published the db.

Super user credentials:
```
username: admin
password: 12345
```

# Run
`python manage.py runserver`

# APIs

1. ## account/register/

#### User registration

```
$ curl -i localhost:8000/account/register/ -d username=owen -d password=owen12345 -d email=owen@email.com
HTTP/1.1 201 Created
Date: Wed, 05 Aug 2020 11:44:06 GMT
Server: WSGIServer/0.2 CPython/3.7.3
Content-Type: application/json
Vary: Accept
Allow: POST, OPTIONS
X-Frame-Options: DENY
Content-Length: 143
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

{"id":4,"username":"owen","email":"owen@email.com","password":"pbkdf2_sha256$216000$tcSl9zUZmk7E$ffJKvcgQZ4xn3wX3qsAEtQ9KOo7FQQAnyi0s5gjX7ks="}
```

2. ## api-token-auth/

#### Request authentication token

```
$ curl -i localhost:8000/api-token-auth/ -d username=owen -d password=owen12345
HTTP/1.1 200 OK
Date: Wed, 05 Aug 2020 11:46:34 GMT
Server: WSGIServer/0.2 CPython/3.7.3
Content-Type: application/json
Allow: POST, OPTIONS
X-Frame-Options: DENY
Content-Length: 52
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

{"token":"14beba260fb72b55130f5b0a7c51b2b75a21ba73"
```

3. ## cart/add/

#### Add item using the auth token

```
$ curl -i localhost:8000/cart/add/ -d name=Milk -d description="A jar of awesome Milk" -d cost=40 -H 'Authorization: Token 14beba260fb72b55130f5b0a7c51b2b75a21ba73'
HTTP/1.1 201 Created
Date: Wed, 05 Aug 2020 11:48:43 GMT
Server: WSGIServer/0.2 CPython/3.7.3
Content-Type: application/json
Vary: Accept
Allow: POST, OPTIONS
X-Frame-Options: DENY
Content-Length: 118
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

{"id":3,"name":"Milk","description":"A jar of awesome Milk","cost":"40.00","created_at":"2020-08-05T11:48:42.880073Z"}
```

4. ## cart/list/

#### List items: Only authenticated users can list items

```
$ curl -i localhost:8000/cart/list/ -H 'Authorization: Token 14beba260fb72b55130f5b0a7c51b2b75a21ba73'
HTTP/1.1 200 OK
Date: Wed, 05 Aug 2020 11:49:28 GMT
Server: WSGIServer/0.2 CPython/3.7.3
Content-Type: application/json
Vary: Accept
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 353
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

[{"id":3,"name":"Milk","description":"A jar of awesome Milk","cost":"40.00","created_at":"2020-08-05T11:48:42.880073Z"},{"id":2,"name":"Bread","description":"A pack of awesome Bread","cost":"40.00","created_at":"2020-08-05T11:07:55.748504Z"},{"id":1,"name":"Egg","description":"An awesome egg","cost":"10.00","created_at":"2020-08-05T10:54:18.631150Z"}]
```

5. ## account/users/

#### List user: Admin only

```
curl -i localhost:8000/account/users/ -H 'Authorization: Token 85cb7d7fb2347eea23f2912ba62d058e06e07234'
HTTP/1.1 200 OK
Date: Wed, 05 Aug 2020 11:52:58 GMT
Server: WSGIServer/0.2 CPython/3.7.3
Content-Type: application/json
Vary: Accept
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 583
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

[{"id":1,"username":"admin","email":"admin@email.com","password":"pbkdf2_sha256$216000$VK203aNW1ClB$c5HH0uMVNn0VuF/DDNCWu7aFY1XAdw8KVq2CTFm+aaM="},{"id":2,"username":"foobar","email":"foobar@example.com","password":"pbkdf2_sha256$216000$QuqeDKe0UscA$iNTzew/AHGGTA5Sgwx3d8UPplZvuyx17G7VzZ8eTOgM="},{"id":3,"username":"john","email":"john@doe.com","password":"pbkdf2_sha256$216000$0pmo6ktVan2D$sEaeTzOygJTX23uAIwFPNPhKwU2vFte1Q/TFQAi5dkM="},{"id":4,"username":"owen","email":"owen@email.com","password":"pbkdf2_sha256$216000$tcSl9zUZmk7E$ffJKvcgQZ4xn3wX3qsAEtQ9KOo7FQQAnyi0s5gjX7ks="}]
```

