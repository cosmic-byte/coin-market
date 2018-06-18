from flask import Blueprint, render_template, flash, redirect, url_for
from markupsafe import escape

from app.portal.service.userService import save_new_user
from .forms import SignupForm
frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    return render_template('index.html')


# Shows a long signup form, demonstrating form rendering.
@frontend.route('/register', methods=['GET', 'POST'])
def sign_up():
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
