import datetime as dt

from cookie.utils import SurrogatePK, Model, Column
from cookie.extensions import db


class WebHooks(SurrogatePK, Model):
    __tablename__ = 'web_hooks'
    project_name = Column(db.String(50), nullable=False)
    web_hook_url = Column(db.String(256), nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.now)
    updated_at = Column(db.DateTime, nullable=False, default=dt.datetime.now)
    active = Column(db.Boolean(), default=True, nullable=False)
    memo = Column(db.String(255), nullable=True)

    def __repr__(self) -> str:
        return '<project {name} {url}>'.format(name=self.project_name, url=self.web_hook_url)
