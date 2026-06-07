# 🏥 Healthcare Cloud Data Platform

## Overview

The Healthcare Cloud Data Platform is an end-to-end data engineering project designed to simulate real-world healthcare analytics workflows. The platform ingests hospital operational data, applies data quality validation and transformation logic, loads data into analytical storage layers, and generates business-ready datasets for reporting and decision-making.

The project demonstrates modern data engineering practices including ETL pipeline development, cloud data warehousing, workflow orchestration, data quality monitoring, analytics reporting, and cloud storage integration.

---

## Business Scenario

Healthcare organisations generate large volumes of operational data from multiple systems including:

* Patient Admissions
* Bed Occupancy Management
* Theatre Bookings
* Hospital Operations

The objective of this project is to centralise healthcare operational data, improve data quality, and provide analytics-ready datasets to support hospital performance reporting and decision-making. The platform also demonstrates governance, regulatory analytics, and dimensional modelling practices commonly used in enterprise healthcare and regulated environments.

---

## Architecture

```text
Raw CSV Data
      │
      ▼
AWS S3 Raw Data Layer
      │
      ▼
Data Profiling Layer
      │
      ▼
Python ETL Pipeline
      │
      ├── Data Validation
      ├── Data Transformation
      ├── Data Quality Checks
      └── Governance Controls
      │
      ▼
PostgreSQL Data Warehouse
      │
      ▼
Star Schema Data Model
      │
      ├── Dimension Tables
      └── Fact Tables
      │
      ▼
Snowflake Cloud Warehouse
      │
      ▼
Regulatory Analytics Views
      │
      ▼
Power BI-ready Reporting Layer
```

---

## Technology Stack

### Programming

* Python
* SQL

### Data Engineering

* ETL / ELT Pipelines
* Data Modelling
* Data Governance
* Metadata Management
* Data Quality Validation
* Data Warehousing

### Databases

* PostgreSQL
* Snowflake

### Cloud

* AWS S3

### Orchestration

* Apache Airflow

### Containerisation

* Docker

### Data Processing

* Pandas
* Psycopg2
* Snowflake Connector

### Reporting & Visualisation

* SQL Analytics Views
* Power BI-ready Reporting Layer

### Version Control

* Git
* GitHub

---

## Project Structure

```text
healthcare-cloud-data-platform/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── load_snowflake.py
│   ├── pipeline.py
│   └── s3_upload.py
│
├── logs/
│
├── sql/
│   ├── create_tables.sql
│   ├── analytics_views.sql
│   ├── snowflake_create_tables.sql
│   ├── snowflake_analytics_views.sql
│   ├── star_schema.sql
│   └── regulatory_analytics_views.sql
│
├── metadata/
│   └── data_catalog.csv
│
├── docs/
│   ├── data_governance.md
│   ├── incident_management.md
│   ├── star_schema_model.md
│   └── data_profiles/
│
├── dags/
│   └── healthcare_pipeline_dag.py
│
├── tests/
│   └── test_dq_checks.py
│
├── .github/
│   └── workflows/
│        └── pipeline-checks.yml
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Data Pipeline Workflow

### 1. Data Extraction

Healthcare operational datasets are extracted from source files:

* Admissions
* Bed Occupancy
* Theatre Bookings

### 2. Data Transformation

Transformation processes include:

* Standardisation
* Derived metrics
* Length of Stay calculation
* Theatre cancellation indicators
* Occupancy calculations

### 3. Data Quality Validation

Implemented quality checks include:

* Null value validation
* Date sequence validation
* Bed occupancy capacity checks
* Dataset consistency checks

### 4. Data Profiling Layer

A dedicated profiling layer analyses source datasets before transformation.

Capabilities:

* Dataset statistics
* Missing value detection
* Duplicate detection
* Data type analysis
* Unique value analysis

Generated Reports:

* admissions_profile.md
* bed_occupancy_profile.md
* theatre_bookings_profile.md

### 4.1 Metadata & Data Governance

The platform includes a governance layer to improve auditability and data understanding.

Features:

* Data catalog
* Column-level metadata
* Sensitivity classification
* Business rule documentation
* Governance controls

Files:

* metadata/data_catalog.csv
* docs/data_governance.md

### 5. PostgreSQL Data Warehouse

Processed healthcare data is loaded into PostgreSQL for structured storage and analysis.

Tables:

* admissions
* bed_occupancy
* theatre_bookings

### 6. AWS S3 Integration

Raw healthcare datasets are stored in AWS S3 to simulate cloud-based data lake architecture.

S3 Structure:

```text
raw/
processed/
analytics/
logs/
```

### 7. Snowflake Cloud Warehouse

Healthcare datasets are loaded into Snowflake for cloud-based analytics.

Tables:

* ADMISSIONS
* BED_OCCUPANCY
* THEATRE_BOOKINGS

### 8. Analytics Layer

Business-focused analytics views are created to support reporting and decision-making.

Views:

* VW_AVG_LENGTH_OF_STAY_BY_WARD
* VW_BED_OCCUPANCY_BY_WARD
* VW_THEATRE_CANCELLATION_RATE
* VW_HOSPITAL_OPERATIONS_SUMMARY

### 8.1 Regulatory Analytics Views

The platform includes risk-based operational analytics.

Views:

* vw_ward_capacity_risk
* vw_theatre_cancellation_risk
* vw_operational_regulatory_summary

These views classify operational metrics into risk categories to support monitoring and decision-making.

### 8.2 Star Schema Data Model

The project includes a Star Schema design to support analytics and reporting workloads.

Dimension Tables:

* dim_date
* dim_ward
* dim_admission_type

Fact Tables:

* fact_admissions
* fact_bed_occupancy
* fact_theatre_bookings

Benefits:

* Analytics-ready reporting
* Improved query performance
* Consistent business definitions
* Scalable warehouse design

### 8.3 Duplicate-safe Incremental Loading

The PostgreSQL loader uses duplicate-safe loading logic with `ON CONFLICT DO NOTHING`. This implementation provides a foundation for future MERGE/UPSERT and CDC-based loading strategies commonly used in enterprise data platforms.

This allows repeated pipeline runs without duplicate primary key failures.

Primary keys:

* admissions: admission_id
* bed_occupancy: record_id
* theatre_bookings: booking_id

### 9. Workflow Orchestration

Apache Airflow orchestrates the ETL workflow:

* Extraction
* Transformation
* Validation
* Loading
* Monitoring

### 9.1 Incident Management & RCA

The project includes incident documentation and root cause analysis examples.

Covered Topics:

* Duplicate key failures
* Troubleshooting procedures
* Monitoring controls
* Resolution workflows
* Production improvement recommendations

Reference:

docs/incident_management.md

### 10. Dashboard & Reporting

Power BI-ready reporting datasets support visualisation of:

* Average Length of Stay
* Bed Occupancy Trends
* Theatre Cancellation Rates
* Hospital Operations KPIs

---

## Sample Business Metrics

### Average Length of Stay

Tracks average patient stay duration by ward.

### Bed Occupancy Rate

Measures ward utilisation and capacity.

### Theatre Cancellation Rate

Identifies surgical cancellation trends.

### Hospital Operations Summary

Provides consolidated operational performance metrics.

---

## Data Quality Framework

The platform includes automated validation checks to ensure reliable data before loading.

Checks include:

* Missing values
* Invalid date sequences
* Bed capacity violations
* Duplicate-safe loading validation

---

## Automated Testing

The platform includes automated unit tests for data quality validation logic.

Coverage:

* Null value validation
* Date sequence validation
* Bed capacity validation

Framework:

* pytest

Result:

* 6 automated tests passing

---

## CI/CD

GitHub Actions automatically validates the project on code changes.

Workflow Includes:

* Dependency installation
* Automated test execution
* Continuous integration checks

Benefits:

* Improved code quality
* Faster issue detection
* Repeatable validation process

---

## Logging & Monitoring

Pipeline execution logs are generated for:

* Extraction
* Transformation
* Validation
* Loading
* Error handling

Logging supports operational monitoring and troubleshooting.

---

## Future Enhancements

* MERGE / UPSERT Loading
* CDC (Change Data Capture) Framework
* Snowflake Stages
* COPY INTO Loading
* dbt Transformations
* Data Lineage Tracking
* AWS Glue Integration
* Role-Based Access Control

---

## Regulatory Analytics Capabilities

This platform demonstrates data engineering practices relevant to regulated environments:

* Data Profiling
* Data Governance
* Metadata Management
* Data Quality Monitoring
* Risk-based Analytics
* Dimensional Data Modelling
* Incident Management
* Root Cause Analysis
* Automated Testing
* Cloud Data Warehousing
* Incremental Loading
* CI/CD Automation

---

## Key Data Engineering Skills Demonstrated

* ETL Pipeline Development
* SQL Analytics
* Python Data Processing
* AWS S3 Integration
* Snowflake Data Warehousing
* Dimensional Data Modelling (Star Schema)
* Regulatory Analytics Engineering
* Incremental Loading Strategies
* Apache Airflow Orchestration
* Docker Containerisation
* Data Quality Engineering
* Healthcare Data Analytics
* Power BI Reporting
* Cloud Data Platform Design
* GitHub Actions CI/CD

---

## Author

**Merine Joseph**

Data Engineer | Software Engineer

GitHub: https://github.com/MerineJoseph
