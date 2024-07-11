CREATE DATABASE simpsons;
CREATE USER simpsonsuser WITH PASSWORD 'simpsons';
GRANT ALL PRIVILEGES ON DATABASE simpsons TO simpsonsuser;
ALTER DATABASE simpsons OWNER TO simpsonsuser;