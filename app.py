import justpy as jp
app = jp

def hello_world():
    wp = jp.WebPage()
    jp.Hello(a=wp)
    return wp

jp.justpy(hello_world)