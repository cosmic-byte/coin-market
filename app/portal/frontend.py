from flask import Blueprint, render_template, flash, redirect, url_for
from markupsafe import escape

from .forms import SignupForm
frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    return render_template('index.html')


# Shows a long signup form, demonstrating form rendering.
@frontend.route('/sign-up/', methods=('GET', 'POST'))
def sign_up():
    form = SignupForm()

    if form.validate_on_submit():
        # We don't have anything fancy in our application, so we are just
        # flashing a message when a user completes the form successfully.
        #
        # Note that the default flashed messages rendering allows HTML, so
        # we need to escape things if we input user values:
        flash('Hello, {}. You have successfully signed up'
              .format(escape(form.name.data)))

        # In a real application, you may wish to avoid this tedious redirect.
        return redirect(url_for('.index'))

    return render_template('index.html', form=form)
