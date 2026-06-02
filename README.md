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

The objective of this project is to centralise healthcare operational data, improve data quality, and provide analytics-ready datasets to support hospital performance reporting and decision-making.

---

## Architecture

```text
Raw CSV Data
      │
      ▼
AWS S3 Raw Data Layer
      │
      ▼
Python ETL Pipeline
      │
      ├── Data Validation
      ├── Data Transformation
      └── Data Quality Checks
      │
      ▼
PostgreSQL Data Warehouse
      │
      ▼
Snowflake Cloud Warehouse
      │
      ▼
Analytics SQL Views
      │
      ▼
Power BI Dashboard
```

---

## Technology Stack

### Programming

* Python
* SQL

### Data Engineering

* ETL / ELT Pipelines
* Data Modelling
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
* Power BI

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
├── docs/
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
│   └── snowflake_analytics_views.sql
│
├── airflow/
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

### 4. PostgreSQL Data Warehouse

Processed healthcare data is loaded into PostgreSQL for structured storage and analysis.

Tables:

* admissions
* bed_occupancy
* theatre_bookings

### 5. AWS S3 Integration

Raw healthcare datasets are stored in AWS S3 to simulate cloud-based data lake architecture.

S3 Structure:

```text
raw/
processed/
analytics/
logs/
```

### 6. Snowflake Cloud Warehouse

Healthcare datasets are loaded into Snowflake for cloud-based analytics.

Tables:

* ADMISSIONS
* BED_OCCUPANCY
* THEATRE_BOOKINGS

### 7. Analytics Layer

Business-focused analytics views are created to support reporting and decision-making.

Views:

* VW_AVG_LENGTH_OF_STAY_BY_WARD
* VW_BED_OCCUPANCY_BY_WARD
* VW_THEATRE_CANCELLATION_RATE
* VW_HOSPITAL_OPERATIONS_SUMMARY

### 8. Workflow Orchestration

Apache Airflow orchestrates the ETL workflow:

* Extraction
* Transformation
* Validation
* Loading
* Monitoring

### 9. Dashboard & Reporting

Power BI dashboards visualise:

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

The platform includes automated validation checks:

* Missing values
* Invalid dates
* Capacity violations
* Data consistency verification

This ensures reliable analytics and trustworthy reporting outputs.

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

* Incremental Loading
* CDC (Change Data Capture)
* Snowflake Stages
* COPY INTO Loading
* dbt Transformations
* Data Lineage Tracking
* Automated Testing
* CI/CD Pipelines
* AWS Glue Integration
* Role-Based Access Control

---

## Key Data Engineering Skills Demonstrated

* ETL Pipeline Development
* SQL Analytics
* Python Data Processing
* AWS S3 Integration
* Snowflake Data Warehousing
* Apache Airflow Orchestration
* Docker Containerisation
* Data Quality Engineering
* Healthcare Data Analytics
* Power BI Reporting
* Cloud Data Platform Design

---

## Author

**Merine Joseph**

Data Engineer | Software Engineer

GitHub: https://github.com/MerineJoseph

