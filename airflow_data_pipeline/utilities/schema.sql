CREATE TABLE IF NOT EXISTS weather_info(
                locdatetime VARCHAR(40),
                location VARCHAR(40),
                updated_date VARCHAR(13),
                temperature FLOAT,
                precipitation_form FLOAT,
                precipitation_prob FLOAT,
                humidity FLOAT,
                wind_speed FLOAT,
                wind_direction FLOAT,
                cloud FLOAT,
                primary key(locdatetime,location));


CREATE TABLE IF NOT EXISTS geography(
                locdate VARCHAR(40),
                location VARCHAR(40),
                updated_date CHAR(10),
                altitudeMeridian VARCHAR(13),
                altitude_09 VARCHAR(20),
                altitude_12 VARCHAR(20),
                altitude_15 VARCHAR(20),
                altitude_18 VARCHAR(20),
                azimuth_09 VARCHAR(20),
                azimuth_12 VARCHAR(20),
                azimuth_15 VARCHAR(20),
                azimuth_18 VARCHAR(20),
                primary key(locdate,location));


