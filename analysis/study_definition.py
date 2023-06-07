from cohortextractor import (
    StudyDefinition,
    patients,
)

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1970-01-01", "latest": "today"},
        "int": {"distribution": "normal", "mean": 25, "stddev": 5},
        "rate": "uniform",
        "incidence": 0.2,
    },
    index_date="2020-01-01",
    population=patients.all(),
    ons_cis_matches=patients.with_an_ons_cis_record("number_of_matches_in_period"),
)
