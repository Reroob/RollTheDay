# db_stats.py
import sys
import os
from pathlib import Path

# Add the project root to Python path if not already there
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from sqlalchemy import inspect, text
from sqlmodel import Session
from app.core.db import engine  # <-- reuse your existing engine


def get_sqlalchemy_pool_stats():
    """Print what SQLAlchemy thinks about its pool usage."""
    pool = engine.pool
    print(f"Pool size: {pool.size()}")
    print(f"Pool checked out: {pool.checkedout()}")
    print(f"Pool overflow: {pool.overflow()}")
    print(f"Pool checked in: {pool.checkedin()}")


def get_postgres_connection_stats():
    """Query pg_stat_activity to see real DB-level connections."""
    try:
        with Session(engine) as session:
            result = session.exec(
                text("""
                    SELECT datname, usename, state, count(*) 
                    FROM pg_stat_activity 
                    GROUP BY datname, usename, state
                    ORDER BY datname, usename, state;
                """)
            )
            rows = result.all()
            for row in rows:
                print(row)
    except Exception as e:
        print(f"Error querying postgres stats: {e}")


if __name__ == "__main__":
    print("=== SQLAlchemy pool stats ===")
    get_sqlalchemy_pool_stats()

    print("\n=== Postgres connection stats ===")
    get_postgres_connection_stats()