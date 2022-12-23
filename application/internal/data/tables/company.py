# from application import db
from application.internal.data import orm


class Company(orm.db.Model):
    """company table object"""
    __tablename__ = 'company'
    __table_args__ = ({'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8mb4'})

    id = orm.db.Column(orm.db.Integer, primary_key=True, autoincrement=True, comment='primary key id')
    uid = orm.db.Column(orm.db.String(32), nullable=False, unique=True, comment='unique id')
    name = orm.db.Column(orm.db.String(24), nullable=False, comment='公司名')
    modules = orm.db.Column(orm.db.JSON, nullable=False, default=[], comment='模块列表')
    expired = orm.db.Column(orm.db.BIGINT, nullable=False, default=0, comment='过期时间')
    config = orm.db.Column(orm.db.JSON, nullable=False, default={}, comment='配置信息')
    create_time = orm.db.Column(orm.db.BigInteger, nullable=False, default=0, comment='create time')
    update_time = orm.db.Column(orm.db.BigInteger, nullable=False, default=0, comment='update time')
