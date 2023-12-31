from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .helpers import get_barber_by_id, allowed_file, save_picture
from .models import Barber_detail
from werkzeug.utils import secure_filename
from . import db
import os

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", user=current_user)

@views.route('/test')
def hometest():
    return render_template("hometest.html", user=current_user)

@views.route('/profile/<int:barber_id>')
def profile(barber_id):
    barber = get_barber_by_id(barber_id)

    # Check if the barber's picture is set. if not, render a default.
    if not barber.barber_detail.picture_filename:
        barber.barber_detail.picture_filename = 'default.jpg'

    return render_template("profile.html", barber=barber, user=current_user)


@views.route('/barbers')
def barbers():
    barbers = Barber_detail.query.all()
    return render_template("barber_list.html", user=current_user, barbers=barbers)

@views.route('/reviews')
def reviews():
    barbers = Barber_detail.query.all()
    return render_template("reviews.html", user=current_user, barbers=barbers)


