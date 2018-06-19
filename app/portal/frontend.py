from flask import Blueprint, render_template, flash, redirect, url_for
from markupsafe import escape

from app.portal.service.auth_helper import Auth
from app.portal.service.userService import save_new_user
from .forms import SignupForm, LoginForm

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    return render_template('index.html')


@frontend.route('/about')
def about():
    return render_template('pages/about.html')


@frontend.route('/contact')
def contact():
    return render_template('pages/contact.html')


@frontend.route('/price')
def price():
    return render_template('pages/price.html')


@frontend.route('/service')
def service():
    return render_template('pages/service.html')


# Shows a long signup form, demonstrating form rendering.
@frontend.route('/register', methods=['GET', 'POST'])
def register():
    form = SignupForm()

    if form.validate_on_submit():
        flash('Hello, {}. You have successfully signed up'
              .format(escape(form.name.data)))
        data = {'email': form.email.data,
                'password': form.password.data,
                'username': form.username.data,
                'fullname': form.name.data}
        save_new_user(data=data)
        return redirect(url_for('frontend.index'))

    return render_template('pages/register.html', form=form)


@frontend.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        data = {'email': form.email.data,
                'password': form.password.data}
        response = Auth.login_user(data=data)
        print(response)
        return redirect(url_for('frontend.index'))

    return render_template('pages/login.html', form=form)
