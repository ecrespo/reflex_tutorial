from sqlmodel import create_engine

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

def connect():
    engine = create_engine(sqlite_url, echo=False)
    return engine
