# Incremental Loading Strategy

## Purpose

This project includes duplicate-safe loading logic to prevent repeated pipeline runs from failing when records already exist in the target database.

## Previous Issue

During development, repeated pipeline execution caused duplicate primary key errors such as:

```text
duplicate key value violates unique constraint admissions_pkey
