# import pymysql

# pymysql.install_as_MySQLdb()

import web
from collections import Iterable


db = web.database(
    dbn='mysql',
    user='root',
    pw='123456',
    db='blog'
)


'''
# result = db.query('select * from user where id=1;')
result = db.select('user')
print(type(result))
for user in result:
    print(user.name)



results = list(db.query("select * from user"))
print(results[0]['name'])
'''

urls = ('/', 'index')
app = web.application(urls, globals())
render = web.template.render('templates')


class index:
    def GET(self):
        udata = web.input()
        print(udata)
        todos = db.select('user')
        isinstance([], Iterable)
        print(todos)

        return render.index(todos)


if __name__ == "__main__":
    app.run()

# print(dict(db.select('blog')))
# users = list(db.select('blog'))

# print(users[0]['summary'])

# entries = db.select('blog')


