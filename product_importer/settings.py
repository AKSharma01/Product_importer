# import os
# import uuid
from env import *

# ## Setting database url for database
# os.environ['DATABASE_URL'] = DATABASE+'://'+DATABASE_PASSWORD+':'+DATABASE_USERNAME+'@localhost/'+DATABASE_NAME

# # setting up secret
# os.environ['SECRET_KEY'] = str(uuid.uuid4()).strip()

# # setting up environment
# if( APP_ENV == 'local'):
#     os.environ['APP_SETTINGS'] = 'product_importer.config.config.DevelopmentConfig'
# if(APP_ENV == 'staging'):
#     os.environ['APP_SETTINGS'] = 'product_importer.config.config.DevelopmentConfig'
# if(APP_ENV == 'production'):
#     os.environ['APP_SETTINGS'] = 'product_importer.config.config.ProductionConfig'



from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
Session = sessionmaker(bind=engine)

Base = declarative_base() 
