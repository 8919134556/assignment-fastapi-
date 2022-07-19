from sqlalchemy import Column, Integer, String
from database import Base


class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    house_no = Column(String)
    street_name = Column(String)
    city = Column(String)
    state = Column(String)
    pincode = Column(Integer)
    country = Column(String)