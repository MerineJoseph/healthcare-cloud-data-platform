# Star Schema Data Model

## Purpose

This project includes a dimensional data model to support analytics-ready reporting and structured business intelligence.

## Model Design

The model separates descriptive business entities into dimension tables and measurable events into fact tables.

## Dimension Tables

### dim_date
Stores date attributes used across admissions, bed occupancy, and theatre bookings.

### dim_ward
Stores ward-level descriptive information.

### dim_admission_type
Stores admission category information such as Emergency, Planned, and Referral.

## Fact Tables

### fact_admissions
Stores patient admission events and length of stay metrics.

### fact_bed_occupancy
Stores ward-level bed capacity and occupancy metrics.

### fact_theatre_bookings
Stores theatre booking events and cancellation indicators.

## Benefits

- Improves analytics performance
- Supports consistent reporting definitions
- Separates descriptive attributes from measurable events
- Enables scalable reporting and business intelligence
- Demonstrates dimensional modelling practices used in data warehousing
