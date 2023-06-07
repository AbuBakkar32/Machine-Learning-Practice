from reactpy import component, html
from reactpy.backend.sanic import configure
from sanic import Sanic


@component
def HelloWorld():
    return html.div(
        html.h1("Hello, world!"),
        html.p("This is the first react py tutorial series")
    )


app = Sanic("MyApp")
configure(app, HelloWorld)

if __name__ == "__main__":
    app.run(port=8000)
