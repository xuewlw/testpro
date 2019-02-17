import web

urls = (
        '/hello_1', 'hello_1',
        '/hello_2/(.*)', 'hello_2'
        )
app = web.application(urls, globals())
render = web.template.render('templates', base='layout')


class hello:
    def GET(self):
        return 'Hello, world!'


class hello_1:
    def GET(self):
        return render.index_1()


class hello_2:
    def GET(self, name):
        return render.index_2(name)

if __name__ == "__main__":
    app.run()

