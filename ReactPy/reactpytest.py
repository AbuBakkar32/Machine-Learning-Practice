from reactpy import ReactPy, Component, render, useState, useEffect, html, run

class App(Component):
    def __init__(self):
        super().__init__()
        self.state = useState(0)

    def render(self):
        return html.div(
            html.h1('Hello World!'),
            html.p(f'You clicked {self.state} times'),
            html.button(
                {
                    'onClick': lambda: self.setState(self.state + 1)
                },
                'Click me'
            )
        )


if __name__ == '__main__':
    run(App)