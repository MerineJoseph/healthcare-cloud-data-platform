DROP TABLE IF EXISTS fact_theatre_bookings;
DROP TABLE IF EXISTS fact_bed_occupancy;
DROP TABLE IF EXISTS fact_admissions;
DROP TABLE IF EXISTS dim_admission_type;
DROP TABLE IF EXISTS dim_ward;
DROP TABLE IF EXISTS dim_date;

CREATE TABLE dim_date (
    date_key DATE PRIMARY KEY,
    year INTEGER,
    month INTEGER,
    day INTEGER
);

CREATE TABLE dim_ward (
    ward_key SERIAL PRIMARY KEY,
    ward_name TEXT UNIQUE NOT NULL
);

CREATE TABLE dim_admission_type (
    admission_type_key SERIAL PRIMARY KEY,
    admission_type_name TEXT UNIQUE NOT NULL
);

CREATE TABLE fact_admissions (
    admission_id TEXT PRIMARY KEY,
    patient_id TEXT,
    ward_key INTEGER REFERENCES dim_ward(ward_key),
    admission_type_key INTEGER REFERENCES dim_admission_type(admission_type_key),
    admission_date_key DATE REFERENCES dim_date(date_key),
    discharge_date_key DATE REFERENCES dim_date(date_key),
    length_of_stay_days NUMERIC
);

CREATE TABLE fact_bed_occupancy (
    record_id TEXT PRIMARY KEY,
    date_key DATE REFERENCES dim_date(date_key),
    ward_key INTEGER REFERENCES dim_ward(ward_key),
    beds_available INTEGER,
    beds_occupied INTEGER,
    occupancy_rate NUMERIC
);

CREATE TABLE fact_theatre_bookings (
    booking_id TEXT PRIMARY KEY,
    patient_id TEXT,
    surgery_date_key DATE REFERENCES dim_date(date_key),
    specialty TEXT,
    status TEXT,
    is_cancelled BOOLEAN
);

INSERT INTO dim_date (date_key, year, month, day)
SELECT DISTINCT date_value::date,
       EXTRACT(YEAR FROM date_value)::integer,
       EXTRACT(MONTH FROM date_value)::integer,
       EXTRACT(DAY FROM date_value)::integer
FROM (
    SELECT admission_datetime::date AS date_value FROM admissions
    UNION
    SELECT discharge_datetime::date AS date_value FROM admissions
    UNION
    SELECT date AS date_value FROM bed_occupancy
    UNION
    SELECT surgery_date AS date_value FROM theatre_bookings
) dates;

INSERT INTO dim_ward (ward_name)
SELECT DISTINCT ward FROM admissions
UNION
SELECT DISTINCT ward FROM bed_occupancy;

INSERT INTO dim_admission_type (admission_type_name)
SELECT DISTINCT admission_type FROM admissions;

INSERT INTO fact_admissions (
    admission_id,
    patient_id,
    ward_key,
    admission_type_key,
    admission_date_key,
    discharge_date_key,
    length_of_stay_days
)
SELECT
    a.admission_id,
    a.patient_id,
    w.ward_key,
    at.admission_type_key,
    a.admission_datetime::date,
    a.discharge_datetime::date,
    a.length_of_stay_days
FROM admissions a
JOIN dim_ward w
    ON a.ward = w.ward_name
JOIN dim_admission_type at
    ON a.admission_type = at.admission_type_name;

INSERT INTO fact_bed_occupancy (
    record_id,
    date_key,
    ward_key,
    beds_available,
    beds_occupied,
    occupancy_rate
)
SELECT
    b.record_id,
    b.date,
    w.ward_key,
    b.beds_available,
    b.beds_occupied,
    b.occupancy_rate
FROM bed_occupancy b
JOIN dim_ward w
    ON b.ward = w.ward_name;

INSERT INTO fact_theatre_bookings (
    booking_id,
    patient_id,
    surgery_date_key,
    specialty,
    status,
    is_cancelled
)
SELECT
    booking_id,
    patient_id,
    surgery_date,
    specialty,
    status,
    is_cancelled
FROM theatre_bookings;
