CREATE OR REPLACE VIEW vw_ward_capacity_risk AS
SELECT
    ward,
    date,
    beds_available,
    beds_occupied,
    ROUND((occupancy_rate * 100)::numeric, 2) AS occupancy_percentage,

    CASE
        WHEN occupancy_rate >= 0.95 THEN 'High Risk'
        WHEN occupancy_rate >= 0.85 THEN 'Medium Risk'
        ELSE 'Low Risk'
    END AS capacity_risk_level

FROM bed_occupancy;

CREATE OR REPLACE VIEW vw_theatre_cancellation_risk AS
SELECT
    specialty,
    COUNT(*) AS total_bookings,
    SUM(CASE WHEN is_cancelled THEN 1 ELSE 0 END) AS cancelled_bookings,
    ROUND(AVG(CASE WHEN is_cancelled THEN 1 ELSE 0 END) * 100, 2) AS cancellation_percentage,
    CASE
        WHEN AVG(CASE WHEN is_cancelled THEN 1 ELSE 0 END) >= 0.30 THEN 'High Risk'
        WHEN AVG(CASE WHEN is_cancelled THEN 1 ELSE 0 END) >= 0.15 THEN 'Medium Risk'
        ELSE 'Low Risk'
    END AS cancellation_risk_level
FROM theatre_bookings
GROUP BY specialty;


CREATE OR REPLACE VIEW vw_operational_regulatory_summary AS
SELECT
    a.ward,
    COUNT(DISTINCT a.admission_id) AS total_admissions,
    ROUND(AVG(a.length_of_stay_days)::numeric, 2) AS avg_length_of_stay_days,
    ROUND(AVG(b.occupancy_rate * 100)::numeric, 2) AS avg_occupancy_percentage,
    CASE
        WHEN AVG(b.occupancy_rate) >= 0.95 THEN 'Requires Review'
        WHEN AVG(b.occupancy_rate) >= 0.85 THEN 'Monitor'
        ELSE 'Within Expected Range'
    END AS operational_review_status
FROM admissions a
LEFT JOIN bed_occupancy b
    ON a.ward = b.ward
GROUP BY a.ward;
