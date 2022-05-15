## Author
> Faith Kwamboka OKong'o

# Kwash Blog
This is an application that allows users to post blogs and read blogs. Users are also able to leave comments, like, unlike and delete comments.
The application also allows users to subscribe and receive notifications about new blog posts.

![blog_1](https://user-images.githubusercontent.com/100117264/168476877-2956b6d5-6bcb-4398-828d-0724988f1044.png)


## User Stories
* As a user, I would like to subscribe  and receive a welcoming email as well as notifications about new blog posts.
* As a user, I would like to see the blogs other people have posted.
* As a user, I would like to vote on the blog they liked and give it a downvote or upvote.
* As a user, I would like to be signed in for me to leave a comment
* As a user, I would like to receive a welcoming email once I sign up.
* As a user, I would like to view the blogs I have created in my profile page.
* As a user, I would like to comment on the different blogs and leave feedback.
* As a user, I would like to submit a blog.
* As a user, I would like to view the different categories. 

## BDD(Behaviour Driven Development)
>Login Inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  | Account username, ``eg kwash``|
| Password  | Account password, ``eg kwash123``|

>Signup inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  | Account username, ``eg kwash``|
| Email  | User email, ``eg kwash@gmail.com``|
| Password  | Account password, ``eg kwash``|
| Confirm Password  | Account password, ``eg kwash123``|

> Blogs inputs

| Inputs | Description  |
|---|---|
|  Heading | Blog eg; ``Life``  |
|  Blog text| The actual blog body|
| Comment| A comment on the Blog|

## Technologies used
* Python3
* Flask
* Html5
* Css3
* Bootstrap4

## Installations

The following command installs all the application requirements
>``pip freeze -r requirements.txt``

## Setup
Run 
``https://github.com/FaithKwamboka/Kwash_Blog.git``

or download the zip file from github.

After extracting the files, 

1. Navigate to the project folder
>`` cd name_of_folder`` 

2. Creating a virtual environment
>``virtualenv virtual.``

3. Activating the virtual environment
>``source virtual/bin/activate.``

4. Running the application
>``python3 manage.py server``

5. Running tests

 > ``python3 manage.py test.``

## [License]()

## Collaborate
For any collaborations, reach me on [okongofaith3@gmail.com]()