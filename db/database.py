from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/web4db"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)