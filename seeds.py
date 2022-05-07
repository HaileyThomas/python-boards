from app.models import User, Post, Comment, Vote
from app.db import Session, Base, engine

# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# insert users
db.add_all([
    User(username="Test1", email="test1@gmail.com", password="password1234"),
    User(username="test2", email="test2@gmail.com", password="password1234"),
    User(username="Test3", email="test3@gmail.com", password="password1234"),
    User(username="test4", email="test4@gmail.com", password="password1234"),
    User(username="Test5", email="test5@gmail.com", password="password1234"),
])

db.commit()

# insert posts
db.add_all([
    Post(title='Who loves Pythons?!',
         post_text='I know I sure do! What about you?', user_id=1),
    Post(title='How many snakes do you have?',
         post_text='I have 5!', user_id=1),
    Post(title='Are you scared of snakes?', post_text='Not me!', user_id=2),
    Post(title='Hello!', post_text='I everyone! I love pythons!', user_id=3),
    Post(title='General Care', post_text='What are your tips?', user_id=4),
])

db.commit()

# insert comments
db.add_all([
    Comment(comment_text='I have 3 but want more', user_id=1, post_id=2),
    Comment(comment_text='None yet sadly', user_id=3, post_id=2),
    Comment(comment_text='Hi there', user_id=2, post_id=4),
    Comment(comment_text='not at all!', user_id=2, post_id=3),
    Comment(comment_text='whats upppp', user_id=5, post_id=4),
])

db.commit()

# insert votes
db.add_all([
    Vote(user_id=1, post_id=2),
    Vote(user_id=1, post_id=4),
    Vote(user_id=2, post_id=4),
    Vote(user_id=3, post_id=4),
    Vote(user_id=4, post_id=2),
])

db.commit()

db.close()
