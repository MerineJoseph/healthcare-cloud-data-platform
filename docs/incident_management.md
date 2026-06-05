# Incident Management and RCA Guide

## Purpose

This document explains how pipeline incidents are identified, investigated, resolved, and documented.

## Example Incident: Duplicate Primary Key Failure

### Incident

The ETL load failed due to a duplicate primary key violation in the admissions table.

### Error

duplicate key value violates unique constraint admissions_pkey

### Root Cause

The pipeline attempted to reload the same batch of records into a table that already contained those primary keys.

### Resolution

A truncate-and-reload strategy was used for the development batch pipeline.

### Production Improvement

In production, this would be improved using:

- MERGE / UPSERT logic
- Incremental loading
- CDC processing
- Batch audit tables
- Duplicate detection before load

## Monitoring Controls

- Pipeline execution logs
- Error tracebacks
- Data quality validation checks
- Manual database verification queries

## Troubleshooting Steps

1. Check `logs/healthcare_pipeline.log`
2. Verify source files exist in `data/raw`
3. Run extraction independently
4. Run transformation independently
5. Check data quality validation
6. Verify database connectivity
7. Check duplicate records
8. Re-run the pipeline after resolution
