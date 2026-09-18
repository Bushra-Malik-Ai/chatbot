from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base


class User(Base):
    """Directory records — the people the chatbot manages. NOT the same as
    an admin account. Being in this table does not grant chatbot access."""
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, default="")
    city = Column(String, default="")


class AdminUser(Base):
    """Accounts allowed to log in and operate the chatbot. Separate from
    User on purpose: directory membership and chatbot access are different
    permissions."""
    __tablename__ = "admin_users"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)


class AuditLog(Base):
    """Every chat command that was attempted, who sent it, and the outcome.
    Required for any tool that mutates data on someone's behalf."""
    __tablename__ = "audit_log"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    actor_email = Column(String, nullable=False)
    message = Column(String, nullable=False)
    success = Column(Integer, nullable=False)
    result = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
