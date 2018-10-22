from flask import (
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
    make_response,
    send_from_directory,
)
from models.user import User
from utils import log
from routes import *


main = Blueprint('index', __name__)


@main.route("/")
def index():
    return render_template("index.html")