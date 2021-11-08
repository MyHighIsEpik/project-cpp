from cpp import db

question_voter = db.Table(
    'question_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True)
)

answer_voter = db.Table(
    'answer_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True)
)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('question_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))
    user_codenum = db.Column(db.String(45), db.ForeignKey('user_pcinfo.codenum', ondelete='CASCADE'), nullable=True)
    user_pcinfo = db.relationship('User_pcinfo', backref=db.backref('question_user_set'))

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))
    user_codenum = db.Column(db.String(45), db.ForeignKey('user_pcinfo.codenum', ondelete='CASCADE'), nullable=True)
    user_pcinfo = db.relationship('User_pcinfo', backref=db.backref('answer_user_set'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    nickname = db.Column(db.String(120), unique=True, nullable=False)
    codenum = db.Column(db.String(45), unique=True, nullable=False)

class User_pcinfo(db.Model):
    codenum = db.Column(db.String(45), db.ForeignKey('user.codenum', ondelete='CASCADE'), primary_key=True)
    cpu = db.Column(db.Text, nullable=True)
    graphic1 = db.Column(db.Text, nullable=True)
    graphic2 = db.Column(db.Text, nullable=True)
    fullos = db.Column(db.Text, nullable=True)
    os = db.Column(db.Integer, nullable=True)
    ram = db.Column(db.Integer, nullable=True)
    cdisk = db.Column(db.Integer, nullable=True)
    ddisk = db.Column(db.Integer, nullable=True)
    edisk = db.Column(db.Integer, nullable=True)
    fdisk = db.Column(db.Integer, nullable=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('comment_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime())
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), nullable=True)
    question = db.relationship('Question', backref=db.backref('comment_set'))
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), nullable=True)
    answer = db.relationship('Answer', backref=db.backref('comment_set'))
    user_codenum = db.Column(db.String(45), db.ForeignKey('user_pcinfo.codenum', ondelete='CASCADE'), nullable=True)
    user_pcinfo = db.relationship('User_pcinfo', backref=db.backref('comment_user_set'))

class Cadinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    cpu = db.Column(db.Text, nullable=True)
    ram = db.Column(db.Integer, nullable=True)
    osversion = db.Column(db.Text, nullable=True)
    videocard = db.Column(db.Text, nullable=True)
    diskspace = db.Column(db.Integer, nullable=True)

class Gameinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    cpu = db.Column(db.Text, nullable=True)
    ram = db.Column(db.Integer, nullable=True)
    osversion = db.Column(db.Text, nullable=True)
    videocard = db.Column(db.Text, nullable=True)
    diskspace = db.Column(db.Integer, nullable=True)

class Illustinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    cpu = db.Column(db.Text, nullable=True)
    ram = db.Column(db.Integer, nullable=True)
    osversion = db.Column(db.Text, nullable=True)
    videocard = db.Column(db.Text, nullable=True)
    diskspace = db.Column(db.Integer, nullable=True)

class Cpulist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpuname = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)

class Videocard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vcname = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)


