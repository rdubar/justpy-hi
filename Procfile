#web: gunicorn --worker-tmp-dir /dev/shm app:app
web: uvicorn.run("app:app", host='0.0.0.0', port=8000, workers=8, debug=True)