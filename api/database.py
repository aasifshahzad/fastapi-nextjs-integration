
from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
SECRET_KEY = "postgresql://aasifshahzad:kF5weXORDU7a@ep-white-sun-a1yogq94.ap-southeast-1.aws.neon.tech/todo?sslmode=require"

# SECRET_KEY = os.environ.get("SECRET_KEY")
print(SECRET_KEY)

def get_engine():
    engine = create_engine(SECRET_KEY, echo=False)
    print("Engine created successfully")
    return engine

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print("Database and tables created successfully")

engine = get_engine()
create_db_and_tables()