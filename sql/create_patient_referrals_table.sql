CREATE TABLE IF NOT EXISTS patient_referrals (
    referral_id VARCHAR(20) PRIMARY KEY,
    patient_id VARCHAR(20),
    referral_source VARCHAR(100),
    referral_date DATE,
    priority VARCHAR(20),
    status VARCHAR(30)
);
