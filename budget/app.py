import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/')
def root():
    print(os.environ['APP_SETTINGS'])
    return "Hello Budget!"

if __name__ == '__main__':
    app.run()
