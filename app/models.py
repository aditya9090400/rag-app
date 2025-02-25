from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    embeddings = Column(JSONB, nullable=True)  # Store embeddings as JSON

class UserQuery(Base):
    __tablename__ = "user_queries"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text)
    retrieved_docs = Column(JSONB)
    answer = Column(Text)
