"""utils_clinic.py.

Shared helper functions for the clinic anomaly-detection domain.

Used by:
- src/cintel/anomaly_detector.py (cintel-02)
- app.py
"""

from pathlib import Path

import polars as pl


def load_clinic_data(data_file: Path) -> pl.DataFrame:
    """Read pediatric clinic age/height records from a CSV file."""
    return pl.read_csv(data_file)


def detect_clinic_anomalies(
    df: pl.DataFrame,
    max_age_years: float,
    max_height_inches: float,
) -> pl.DataFrame:
    """Return rows meeting one or more defined anomaly threshold conditions."""
    return df.filter(
        (pl.col("age_years") >= max_age_years)
        | (pl.col("height_inches") >= max_height_inches)
    )
