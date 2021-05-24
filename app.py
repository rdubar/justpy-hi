import justpy as jp

def app():
    wp = jp.WebPage()
    jp.Hello(a=wp)
    return wp

def main():
    jp.justpy(app)
    app = jp

if __name__ == "__main__":
    main()
