from flask import render_template, request, flash, redirect, jsonify, url_for, make_response
from app.models.User import db, User
from app.controllers import userController
from app.utils.forms import RegistrationForm
from . import main_bp, errors



@main_bp.route('/', methods = ["GET", "POST"])
def home_page():
    # try:
    #     new_user = User(username='LAMOS', email='lalamove@gmail.com')
    #     db.session.add(new_user)
    #     db.session.commit()
    # except Exception as e:
    #     print(e)
    if request.method == "GET":
        return render_template('index.html')
    else:
        pass

@main_bp.route('/login', methods = ["GET", "POST"])
def login_page():
    if request.method == "GET":
        return render_template('userLogin.html')
    else:
        pass

@main_bp.route('/register', methods = ["GET","POST"])
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check db if email already in use
        if userController.check_email_valid(form.email.data):
            flash('Email address is invalid.', 'danger')
            return redirect('/register')
        if not userController.check_password_valid(form.password.data):
            flash('Password is invalid.', 'danger')
            return redirect('/register')
        # Proceed if email is not in use
        print(form.email.data, form.password.data, form.full_name.data, form.phone_number.data)
        return redirect('/login')
    return render_template('userRegisterPage.html', form=form)
    #     userController.create(
    #        user_email=form.email.data,
    #        password=form.password.data,
    #        full_name=form.full_name.data,
    #        phone_number=form.phone_number.data,
    #        profile_picture=form.profile_picture.data
    #    )




        # if request.method == "GET":
        #     return render_template('userRegisterPage.html')
        # else:
        #     userController.create(
        #         user_email=request.form['userEmail'],
        #         password=request.form['password'],
        #         full_name=request.form['userFullName'],
        #         phone_number=request.form['phone_number'],
        #         profile_picture=request.files['profilePicture']
        #     )
        #     return redirect('/login')


@errors.app_errorhandler(404)
def error_404(e):
    return render_template(
        'errorPage.html',
        error_num=404,
        error_text="Page Not Found"), 404

@errors.app_errorhandler(500)
def error_500(e):
    return render_template(
        'errorPage.html',
        error_num=500,
        error_text="Internal Server Error"), 500
