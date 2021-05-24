#web: gunicorn --worker-tmp-dir /dev/shm app:app
uvicorn.run("app:app", host='127.0.0.1', port=8000, workers=8, debug=True)