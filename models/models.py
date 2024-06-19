from sqlalchemy import MetaData, Integer, String, TIMESTAMP, DATE, ForeignKey, JSON, Column
import datetime
from sqlalchemy.orm import DeclarativeBase

metadata = MetaData()

class Base(DeclarativeBase): pass

class Roles(Base):
    __tablename__ = 'roles'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)
    
class Users(Base):
    __tablename__= 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column( String, nullable=False)
    username = Column( String , nullable=False)
    password = Column( String, nullable=False)
    register_time = Column( TIMESTAMP, default=datetime.datetime.now)
    role_id = Column( Integer, ForeignKey('roles.id') )
# roles = Table(
#     "roles",
#     metaData,
#     Column('id', Integer , primary_key=True),
#     Column('name', String , nullable=False),
#     Column('permissions', JSON),
# )

# users = Table(
#     "users",
#     metaData,
#     Column('id', Integer , primary_key=True),
#     Column('email', String, nullable=False),
#     Column('username', String , nullable=False),
#     Column('password', String, nullable=False),
#     Column('register_time', TIMESTAMP, default=datetime.utsnow),
#     Column('role_id', Integer, ForeignKey('roles.id') )
# )



