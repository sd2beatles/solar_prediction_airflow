from google.cloud import storage
from pathlib import Path
from decouple import config

class UnconfiguredEnvironment(Exception):
    pass


'''
|-dags
  |-preprocess
   - connection.py
   - load_data.py
   - preprocess.py
  .env

'''

BASE_DIR=Path(__file__).parent.parent
print(BASE_DIR)

try:
    client=storage.Client()
except KeyError as e:
    raise UnconfiguredEnvironment("Raised issues on the goolge credential \
        environmental variable.")




    