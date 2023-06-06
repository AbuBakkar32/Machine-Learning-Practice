from reactpy import component, html
from reactpy.backend.sanic import configure
from sanic import Sanic


@component
def HelloWorld():
    return html.h1("Hello, world!")


app = Sanic("MyApp")
configure(app, HelloWorld)


if __name__ == "__main__":
    app.run(port=8000)