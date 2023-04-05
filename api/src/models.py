from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

roles_users = db.Table(
    'roles_users',
    db.Column('roles_id', db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'), nullable=False, primary_key=True),
    db.Column('users_id', db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, primary_key=True),
)

class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), default=db.func.now(), onupdate=db.func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(Base):
    __tablename__ = 'users'
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    is_active = db.Column(db.Boolean(), default=True)
    roles = db.relationship('Role', cascade="all, delete", secondary=roles_users)
    profile = db.relationship('Profile', cascade="all, delete", uselist=False)
    messages_from = db.relationship('Message', foreign_keys="[Message.from_id]", backref="user_from")
    messages_to = db.relationship('Message', foreign_keys="[Message.to_id]", backref="user_to")
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def serialize_full_info(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            "roles": self.get_user_roles(),
            "profile": self.profile.serialize(),
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def get_user_roles(self):
        return list(map(lambda role: role.serialize(), self.roles))



class Role(Base):
    __tablename__ = 'roles'
    name = db.Column(db.String(100), nullable=False, unique=True)
    users = db.relationship('User', secondary=roles_users)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


class Profile(Base):
    __tablename__ = 'profiles'
    bio = db.Column(db.Text(), default="")
    facebook = db.Column(db.String(120), default="")
    twitter = db.Column(db.String(120), default="")
    instagram = db.Column(db.String(120), default="")
    github = db.Column(db.String(120), default="")
    linkedin = db.Column(db.String(120), default="")
    avatar = db.Column(db.String(200), default="")
    avatar_public_id = db.Column(db.String(120), default="")
    users_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, unique=True)

    def serialize(self):
        return {
            "id": self.id,
            "bio": self.bio,
            "users_id": self.users_id,
            "avatar": self.avatar,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


class Message(Base):
    __tablename__ = 'messages'
    message = db.Column(db.Text(), nullable=False)
    from_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    to_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    #user_from = db.relationship('User', primaryjoin=from_id, foreign_keys="[User.id]", uselist=False)
    #user_to = db.relationship('User', primaryjoin=to_id, foreign_keys="[User.id]", uselist=False)

    def serialize(self):
        return {
            "id": self.id,
            "message": self.message,
            "from_id": self.from_id,
            "to_id": self.to_id,
            "user_from": self.user_from.serialize(),
            "user_to": self.user_to.serialize(),
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }