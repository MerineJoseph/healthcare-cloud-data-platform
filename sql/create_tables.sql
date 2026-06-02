CREATE TABLE admissions (
    admission_id TEXT PRIMARY KEY,
    patient_id TEXT,
    ward TEXT,
    admission_datetime TIMESTAMP,
    discharge_datetime TIMESTAMP,
    admission_type TEXT,
    length_of_stay_days FLOAT
);

CREATE TABLE bed_occupancy (
    record_id TEXT PRIMARY KEY,
    date DATE,
    ward TEXT,
    beds_available INT,
    beds_occupied INT,
    occupancy_rate FLOAT
);

CREATE TABLE theatre_bookings (
    booking_id TEXT PRIMARY KEY,
    patient_id TEXT,
    surgery_date DATE,
    specialty TEXT,
    status TEXT,
    is_cancelled BOOLEAN
);
