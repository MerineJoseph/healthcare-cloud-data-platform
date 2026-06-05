# Data Governance Layer

## Purpose

This project includes a lightweight data governance layer to document dataset definitions, column meanings, sensitivity classifications, and business validation rules.

## Governance Controls Implemented

- Data catalog for source datasets
- Column-level descriptions
- Sensitive data classification
- Business rule documentation
- Data quality validation checks
- Logging for pipeline execution
- Analytics views for controlled reporting outputs

## Sensitive Data Handling

Patient identifiers are treated as confidential fields. This project uses synthetic sample data only and does not contain real patient information.

## Business Rules

Examples:

- admission_id must be unique and not null
- admission_datetime must be before discharge_datetime
- beds_occupied cannot exceed beds_available
- cancelled and did not attend theatre bookings are flagged as cancellations
- patient_id is treated as confidential

## Relevance to Regulated Data Environments

This governance layer supports consistent interpretation, auditability, and reliable transformation of operational data into analytics-ready outputs. It demonstrates how data assets can be documented and controlled before being used for reporting or decision-making.
