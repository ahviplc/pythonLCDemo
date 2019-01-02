from flask_wtf import FlaskForm as Form
from wtforms.fields import StringField, TextField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import Required, Length, DataRequired


class LoginForm(Form):
    username = StringField(validators=[DataRequired(message='用户名不能为空'), Length(min=3, max=15, message="用户名长度范围3-15")])
    password = StringField(validators=[DataRequired(message='密码不能为空'), Length(min=3, max=15, message="密码长度范围3-15")])
    remember_me = BooleanField('remember me', default=False)
    submit = SubmitField('Login')


class SignUpForm(Form):
    username = StringField(validators=[DataRequired(message='用户名不能为空'), Length(min=3, max=15, message="用户名范围3-15")])
    password = StringField(validators=[DataRequired(message='密码不能为空'), Length(min=3, max=15, message="密码长度范围3-15")])
    submit = SubmitField('Sign up')


class EditForm(Form):
    username = TextField('username',
                         validators=[DataRequired(message="用户名不能为空"), Length(min=3, max=15, message="用户名长度范围3-15")])
    about_me = TextAreaField('about_me', validators=[Length(min=2, max=140, message="自我介绍长度范围2-140")])

    def __init__(self, original_username, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_username = original_username

    def validate(self):
        if not Form.validate(self):
            return False
        if self.username.data == self.original_username:
            return True
        user = User.query.filter_by(username=self.username.data).first()
        if user != None:
            return False
        return True


class ChangeForm(Form):
    title = TextField('title',
                      validators=[DataRequired(message="标题不能为空"), Length(min=1, max=120, message="标题内容长度范围1-120")])
    content = TextAreaField('content',
                            validators=[DataRequired(message="内容不能为空"),
                                        Length(min=1, max=1200, message="内容长度范围1-1200")])


class PostForm(Form):
    title = TextField('title',
                      validators=[DataRequired(message="标题不能为空"), Length(min=1, max=120, message="标题内容长度范围1-120")])
    content = TextAreaField('content',
                            validators=[DataRequired(message="内容不能为空"),
                                        Length(min=1, max=1200, message="内容长度范围1-1200")])
