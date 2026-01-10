# Python with MongoDB

Python is a backend technology and it can be connected with different data base applications. It can be connected to both SQL and noSQL databases. In this section, we connect Python with MongoDB database which is noSQL database. 

## MongoDB

MongoDB is a NoSQL database. MongoDB stores data in a JSON like document which make MongoDB very flexible and scalable. Let us see the different terminologies of SQL and NoSQL databases. The following table will make the difference between SQL versus NoSQL databases.

### SQL versus NoSQL

![SQL versus NoSQL](../images/mongoDB/sql-vs-nosql.png)

In this section, we will focus on a NoSQL database MongoDB. Lets sign up on [mongoDB](https://www.mongodb.com/) by click on the sign in button then click register on the next page.

![MongoDB Sign up pages](../images/mongoDB/mongodb-signup-page.png)

Complete the fields and click continue

![Mongodb register](../images/mongoDB/mongodb-register.png)

Select the free plan

![Mongodb free plan](../images/mongoDB/mongodb-free.png)

Choose the proximate free region and give any name for you cluster.

![Mongodb cluster name](../images/mongoDB/mongodb-cluster-name.png)

Now, a free sandbox is created

![Mongodb sandbox](../images/mongoDB/mongodb-sandbox.png)

All local host access

![Mongodb allow ip access](../images/mongoDB/mongodb-allow-ip-access.png)

Add user and password

![Mongodb add user](../images/mongoDB/mongodb-add-user.png)

Create a mongoDB uri link

![Mongodb create uri](../images/mongoDB/mongodb-create-uri.png)

Select Python 3.6 or above driver

![Mongodb python driver](../images/mongoDB/mongodb-python-driver.png)

### Getting Connection String(MongoDB URI)

Copy the connection string link and you will get something like this:

```sh
mongodb+srv://asabeneh:<password>@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

Do not worry about the url, it is a means to connect your application with mongoDB.
Let us replace the password placeholder with the password you used to add a user.

**Example:**

```sh
mongodb+srv://asabeneh:123123123@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

Now, I replaced everything and the password is 123123 and the name of the database is *thirty_days_python*. This is just an example, your password must be stronger than the example password.

Python needs a mongoDB driver to access mongoDB database. We will use _pymongo_ with _dnspython_ to connect our application with mongoDB base . Inside your project directory install pymongo and dnspython.

```sh
pip install pymongo dnspython
```
