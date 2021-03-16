## News feed with fake news tagging using django
When a news/article is posted in this community the django post_save signal of the particular post is captured by the receiver and give as input to Machine learning model to predict the class.
![alt text](https://github.com/sreehari1997/django-blog/blob/master/screenshots/home.png?raw=true)
### Architecture
![alt text](https://github.com/sreehari1997/django-blog/blob/master/screenshots/block_diagram.png?raw=true)


### Heroku
This app is hosted on heroku without the fake news detection feature.
https://radiant-savannah-77061.herokuapp.com/