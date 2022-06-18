from sqlalchemy.orm import Session

import api.orm as orm


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(orm.Item).offset(skip).limit(limit).all()
