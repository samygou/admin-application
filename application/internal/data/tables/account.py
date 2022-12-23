from flask_login import UserMixin

# from application import db
from application.internal.data import orm


class Account(UserMixin, orm.db.Model):
    """account db manager"""
    __tablename__ = 'accounts'
    __table_args__ = ({'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8mb4'})

    id = orm.db.Column(orm.db.Integer, primary_key=True, autoincrement=True, comment='primary key id')
    uid = orm.db.Column(orm.db.String(64), nullable=False, unique=True, comment='唯一id')
    username = orm.db.Column(orm.db.String(16), nullable=False, comment='用户名')
    phone = orm.db.Column(orm.db.String(16), nullable=False, unique=True, comment='手机号')
    remark = orm.db.Column(orm.db.String(32), nullable=False, default='', comment='备注')
    create_time = orm.db.Column(orm.db.BigInteger, nullable=False, default=0, comment='create time')
    update_time = orm.db.Column(orm.db.BigInteger, nullable=False, default=0, comment='update time')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
