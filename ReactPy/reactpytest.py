from reactpy import component, html, run


@component
def App():
    return html.div(
        html.h1("Hello, world!"),
        html.p("This is a paragraph."),
        html.button("Click me!")
    )


run(App)
