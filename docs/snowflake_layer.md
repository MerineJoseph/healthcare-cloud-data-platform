# Snowflake Cloud Warehouse Layer

## Purpose

Snowflake is used as the cloud data warehouse for storing cleaned healthcare operational data.

## Tables

- ADMISSIONS
- BED_OCCUPANCY
- THEATRE_BOOKINGS

## Analytics Views

- VW_AVG_LENGTH_OF_STAY_BY_WARD
- VW_BED_OCCUPANCY_BY_WARD
- VW_THEATRE_CANCELLATION_RATE
- VW_HOSPITAL_OPERATIONS_SUMMARY

## Business Value

The Snowflake layer enables scalable analytics for hospital operations, including patient flow, bed utilisation, theatre cancellations, and ward-level performance.

## Production Improvements

- Use S3 external stages
- Use COPY INTO for bulk loading
- Add MERGE logic for incremental loads
- Use Snowflake tasks for scheduled transformations
- Add role-based access control
