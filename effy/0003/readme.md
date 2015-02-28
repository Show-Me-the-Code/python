##mongoDB connect with python

###Pre-request:
1. Has mongo installed and running.
2. Has pymongo instaled with pip

###To connect
```python
from pymongo import MongoClient
c = MongoClient()
```
That's it! dead simple -- but you may need to make sure that mongo is **running on the default port-- 27017**

python和mongo的连接出乎意料的简单。

需要的只是一个pymongo中的MongoClient来建立一个live connection！而且最赞的是，由于是nosql，根本不需考虑collection已有的数据是什么类型，key，schema什么的，直接统统insert。之前和relational sql连接的时候（postgres）则需要考虑原来的table里面的PK有没有重复，id是否要被maintain成incremental，之类的问题~炒鸡方便！

### To manipulate mongodb within python
1. to access specific database

    ```python
    db = c['effy_db']
    ```
2. to access specific collection

	```python
	cl = db['effy_collection']
	```
db, collection acts like a **dict** in python! it actually is. When a live connection is established, *database object* becomes a dictionary with key equals to its name and value equals the object itself.

To access mongo shell command for absolute beginners, see <a href=http://effyhuang.com/2014/12/06/mongo-db-command-ref/> the blog</a>.
