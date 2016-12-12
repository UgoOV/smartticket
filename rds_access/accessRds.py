import logging
import sys

import pymysql

import rds_config

# rds settings
rds_host = "52.31.201.94"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name,
                           passwd=password, db=db_name, connect_timeout=5)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()

logger.info("SUCCESS: Connection to RDS mysql instance succeeded")


class AccessRDS:
    def __init__(self):
        self

    def getBonsPlansInfosRow(self):
        """
        This function fetches content from mysql RDS instance
        """

        with conn.cursor() as cur:
            cur.execute(
                'insert into userbonsplans (analytics_category, burned, offreDesc) values("[10000]", 1, "test")')


AccessRDS().getBonsPlansInfosRow()
