from peewee import *
import datetime

db=MySQLDatabase('blog',user='root',passwd='sqldb123')

class blogs(Model):
	username=CharField()
	title=CharField()
	content=TextField()
	posttime=DateTimeField(default=datetime.datetime.now)

	class Meta:
		database=db

