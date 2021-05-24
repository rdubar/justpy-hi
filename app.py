import justpy as jp
app = jp

def hello():
    wp = jp.WebPage()
    jp.Hello(a=wp)
    return wp

def main():
    jp.justpy(hello)
    app = jp

if __name__ == "__main__":
    main()
