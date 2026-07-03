# REST API Ingestion

## Objective

The Healthcare Cloud Data Platform was extended to support REST API-based data ingestion in addition to existing file-based (CSV) ingestion. This enhancement demonstrates how operational healthcare data from external systems can be integrated into the ETL pipeline using JSON processing, schema validation, transformation, and data loading.

---

## Business Scenario

Modern healthcare organisations receive data from multiple sources, including:

- Electronic Medical Record (EMR) systems
- Hospital Information Systems (HIS)
- Referral Management Systems
- Third-party healthcare providers
- REST APIs

To simulate a real-world integration scenario, this project introduces a Patient Referrals dataset delivered through a REST API response.

---

## Why REST APIs?

Many enterprise healthcare platforms exchange operational data through REST APIs instead of flat files.

Supporting REST API ingestion enables:

- Integration with external healthcare systems
- Near real-time data exchange
- Automated data collection
- Reduced manual file handling
- Scalable enterprise integration

---

## Architecture

```text
REST API (JSON)
        │
        ▼
API Extraction (Python)
        │
        ▼
Raw CSV Landing
        │
        ▼
Transformation
        │
        ▼
Data Quality Validation
        │
        ▼
Processed CSV
        │
        ▼
PostgreSQL Data Warehouse
        │
        ▼
Analytics & Reporting
```

---

## API Dataset

Dataset:

Patient Referrals

Fields:

- referral_id
- patient_id
- referral_source
- referral_date
- priority
- status

The API response is simulated using a JSON file stored within the project.

---

## Extraction Process

The API extraction layer:

- Reads JSON responses
- Converts JSON into a Pandas DataFrame
- Validates the required schema
- Writes extracted data into the Raw Data Layer
- Logs extraction status

The extraction logic is implemented in:

```text
etl/api_extract.py
```

---

## Schema Validation

Before processing, the pipeline validates the presence of required fields.

Required fields include:

- referral_id
- patient_id
- referral_source
- referral_date
- priority
- status

If mandatory fields are missing, the pipeline raises an exception and records the failure in the log.

---

## Transformation

Transformation activities include:

- Date conversion
- Standardising string values
- Removing whitespace
- Preparing the dataset for downstream loading

The transformed dataset is stored as:

```text
data/processed/patient_referrals_processed.csv
```

---

## PostgreSQL Loading

The processed dataset is loaded into PostgreSQL using the project's duplicate-safe incremental loading framework.

The target table is:

```text
patient_referrals
```

Duplicate records are prevented using the primary key during loading.

---

## Logging

The API ingestion process records:

- Successful extraction
- Missing files
- Invalid JSON
- Schema validation failures
- Processing errors

Logs are written to:

```text
logs/healthcare_pipeline.log
```

---

## Error Handling

The ingestion module includes handling for:

- Missing API response files
- Invalid JSON format
- Missing mandatory fields
- Unexpected runtime exceptions

Errors are logged before being raised for investigation.

---

## Current Limitations

The current implementation simulates an external REST API using a local JSON response file.

The following enterprise capabilities are not yet implemented:

- API authentication
- OAuth tokens
- Pagination
- Retry mechanisms
- Rate limiting
- Automatic scheduling
- Direct Snowflake loading

These features are common in production environments and can be incorporated in future iterations.

---

## Future Enhancements

Potential future improvements include:

- Live REST API integration
- Secure API authentication
- Pagination support
- Retry and timeout handling
- Rate limit management
- Snowflake integration for API datasets
- Airflow orchestration of API extraction
- Data lineage and monitoring
