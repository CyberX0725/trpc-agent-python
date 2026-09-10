#!/usr/bin/env python3
import sys
from examples.skills_code_review_agent.db import Base, ReviewDbRepository


def initialize_database(db_url: str = "sqlite:///review_agent.db"):
    """
    Initialize the development database schema by creating missing tables.

    This is not a versioned migration system. ``--reset`` destructively drops
    all prototype tables and is intended only for disposable local data.
    """
    print(f"Initializing database schema at: {db_url}")
    
    # Check if we want a clean reset
    if "--reset" in sys.argv:
        print("Warning: Reset option detected. Dropping all existing tables...")
        # Get raw engine to drop
        repo = ReviewDbRepository(db_url)
        Base.metadata.drop_all(repo.engine)
        print("Tables dropped.")
        
    repo = ReviewDbRepository(db_url)
    print("Database tables successfully initialized.")
    print("Tables created:")
    for table_name in Base.metadata.tables:
        print(f"  - {table_name}")

if __name__ == "__main__":
    db_path = "sqlite:///review_agent.db"
    initialize_database(db_path)
