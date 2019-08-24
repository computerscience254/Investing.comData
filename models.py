from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,backref)
from sqlalchemy.ext.declarative import declarative_base
from config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    data = relationship('HistoricalData', cascade="all, delete-orphan", backref="name")

    def __repr__(self):
        return '<User %r>' % self.name

class HistoricalData(Base):
    __tablename__ = 'data'
    uuid = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    open_price = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    vol = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey('company.id'), nullable=False)

    def __repr__(self):
        return '<Title %r>' % self.company_id

