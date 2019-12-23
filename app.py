from sanic import response
from sanic import Sanic
from sanic import request
from sanic.response import text
from sanic.response import json
from sanic import Blueprint
import motor.motor_asyncio
from routes import bp

app = Sanic('hanieh')
app.blueprint(bp)
# app.config.AUTH_LOGIN_ENDPOINT = 'login'
UPLOAD_FOLDER = './public/images'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)