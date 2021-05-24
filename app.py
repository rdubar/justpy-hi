import justpy as jp
app = jp

def hello_world():
    wp = jp.WebPage()
    jp.Hello(a=wp)
    return wp

def main():
    jp.justpy(hello_world)

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, workers=8, debug=True)
