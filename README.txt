Steps To Setup:
1. create env.py file first
2. set APP_ENV, DATABASE, DATABASE_NAME, DATABASE_USERNAME, DATABASE_PASSWORD
3. Run the migration
    a. python -m product_importer.config.manage db init
    b. python -m product_importer.config.manage db migrate
    c. python -m product_importer.config.manage db upgrade
4. To update the migration
    a. python -m product_importer.config.manage db migrate
    b. python -m product_importer.config.manage db upgrade