import sys
from databricks_api import DatabricksAPI
from databricks_cli.repos.api import ReposApi
import time

tokenuser = sys.argv[1]

db = DatabricksAPI(
    host="https://adb-XXXXXXXXXXX.10.azuredatabricks.net/",
    token=tokenuser
)

db.repos.update_repo(
    id = XXXXXXXXXXXXXXXXX,
    branch='main'
)