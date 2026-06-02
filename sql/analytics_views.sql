CREATE OR REPLACE VIEW vw_avg_length_of_stay_by_ward AS
SELECT
    ward,
    ROUND(AVG(length_of_stay_days)::numeric, 2) AS avg_length_of_stay_days,
    COUNT(*) AS total_admissions
FROM admissions
GROUP BY ward;


CREATE OR REPLACE VIEW vw_bed_occupancy_by_ward AS
SELECT
    date,
    ward,
    beds_available,
    beds_occupied,
    ROUND((occupancy_rate * 100)::numeric, 2) AS occupancy_percentage
FROM bed_occupancy;


CREATE OR REPLACE VIEW vw_theatre_cancellation_rate AS
SELECT
    surgery_date,
    specialty,
    COUNT(*) AS total_bookings,
    SUM(CASE WHEN is_cancelled THEN 1 ELSE 0 END) AS cancelled_bookings,
    ROUND(
        AVG(CASE WHEN is_cancelled THEN 1 ELSE 0 END)::numeric * 100,
        2
    ) AS cancellation_percentage
FROM theatre_bookings
GROUP BY surgery_date, specialty;


CREATE OR REPLACE VIEW vw_hospital_operations_summary AS
SELECT
    a.ward,
    COUNT(DISTINCT a.admission_id) AS total_admissions,
    ROUND(AVG(a.length_of_stay_days)::numeric, 2) AS avg_length_of_stay_days,
    ROUND(AVG(b.occupancy_rate * 100)::numeric, 2) AS avg_occupancy_percentage
FROM admissions a
LEFT JOIN bed_occupancy b
    ON a.ward = b.ward
GROUP BY a.ward;
