import os
# change values and save me as dbconfig.py!

PGHOSTNAME = os.environ.get("POSTGRES_HOST", "postgis")
PGUSERNAME = os.environ.get("POSTGRES_USER", "postgres")
PGDATABASE = os.environ.get("POSTGRES_DB", "postgres")
PGPASSWORD = os.environ.get("POSTGRES_PASSWORD", "postgrespassword")
