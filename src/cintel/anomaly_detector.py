"""anomaly_detector.py - Project script (example).

Author: Your Name Here
Date: 2026-mm-dd

Static Data

- Data is taken from a pediatric clinic's patient records.
- The data is static, meaning it does not change over time and is not updated with new records.
- The clinic works with children from birth to 16 years old.
- Each row represents a patient visit with two key measurements:
  - age_years: The patient's age in years.
  - height_inches: The patient's height in inches.

Purpose

- Read the data from a CSV (comma-separated values) file.
- Detect anomalies.
- Log the pipeline process to assist with debugging and transparency.

Paths (relative to repo root)

    INPUT FILE: data/clinic_data.csv
    OUTPUT FILE: artifacts/anomalies.csv

Terminal command to run this file from the root project folder

    uv run python -m cintel.anomaly_detector

DESIGN:

Use this file to first learn and then apply your skills.

Reusable functions that do the work are kept in a utils file.
We import functions and pass in what they need through their parentheses.
Shared utility functions can be imported into a Python
module or a reactive marimo notebook app.

SKILLS:

- Reading CSV files into Polars DataFrames.
- Defining and using constants for thresholds.
- Logging for debugging and transparency.
- Detecting anomalies based on domain-specific rules.


"""

# === DECLARE IMPORTS (packages we will use in this project) ===

# First from the Python standard library (no installation needed)
import logging
from pathlib import Path
from typing import Final

from datafun_toolkit.logger import get_logger, log_header, log_path
import polars as pl

from cintel.utils_clinic import detect_clinic_anomalies, load_clinic_data

# === CONFIGURE LOGGER ===

LOG: logging.Logger = get_logger("P2", level="DEBUG")

# === DECLARE GLOBAL CONSTANTS FOR FOLDER PATHS (directories) ===

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
ARTIFACTS_DIR: Final[Path] = ROOT_DIR / "artifacts"

# === DECLARE GLOBAL CONSTANTS FOR FILE PATHS ===

DATA_FILE: Final[Path] = DATA_DIR / "clinic_data.csv"
OUTPUT_FILE: Final[Path] = ARTIFACTS_DIR / "anomalies.csv"


# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Run the pipeline.

    log_header() logs a standard run header.
    log_path() logs repo-relative paths (privacy-safe).
    """
    log_header(LOG, "CINTEL")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    # Log the constants to help with debugging and transparency.
    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "DATA_FILE", DATA_FILE)
    log_path(LOG, "OUTPUT_FILE", OUTPUT_FILE)

    # Call the mkdir() method to ensure it exists
    # The parents=True argument allows it to create any necessary parent directories.
    # The exist_ok=True argument prevents an error if the directory already exists.
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    log_path(LOG, "ARTIFACTS_DIR", ARTIFACTS_DIR)

    # ----------------------------------------------------
    # STEP 1: READ CSV DATA FILE INTO A POLARS DATAFRAME (TABLE)
    # ----------------------------------------------------
    # load_clinic_data() just wraps polars' read_csv()
    # function. You can see what it does in utils_clinic.py.
    # It's pretty easy to get a CSV file into
    # a DataFrame (a two-dimensional table).

    df: pl.DataFrame = load_clinic_data(DATA_FILE)

    # Visually inspect the file in the data/ folder.
    # It has columns named `age_years` and `height_inches`.
    # The DataFrame height attribute returns the number of rows.
    LOG.info(f"Loaded {df.height} patient records")

    # ----------------------------------------------------
    # STEP 2: DEFINE THRESHOLDS AND DETECT ANOMALIES
    # ----------------------------------------------------
    # An anomaly is any observation that meets a defined threshold condition.
    # Domain rule for this example:
    # Observations meeting one or more threshold conditions are suspicious.
    LOG.info("Studying children's ages and heights to find anomalies...")

    # x is age in years, so 16 is the upper limit for kids
    MAX_REASONABLE_X_VALUE: Final[float] = 16.0

    # y is height in inches, so maybe 6 feet (72 inches) is a reasonable upper limit
    MAX_REASONABLE_Y_VALUE: Final[float] = 72.0

    LOG.info(f"MAX_REASONABLE_X_VALUE: {MAX_REASONABLE_X_VALUE} in years")
    LOG.info(f"MAX_REASONABLE_Y_VALUE: {MAX_REASONABLE_Y_VALUE} in inches")

    # Create a new DataFrame named anomalies_df that contains
    # only the rows where EITHER
    # the age is TOO HIGH OR the height is TOO HIGH.
    # See detect_clinic_anomalies() in utils_clinic.py
    # for exactly how that filter is built.
    anomalies_df: pl.DataFrame = detect_clinic_anomalies(
        df,
        max_age_years=MAX_REASONABLE_X_VALUE,
        max_height_inches=MAX_REASONABLE_Y_VALUE,
    )

    LOG.info(f"Count of anomalies found: {anomalies_df.height}")

    # ----------------------------------------------------
    # STEP 3: SAVE THE OUTPUT ANOMALIES AS EVIDENCE
    # ----------------------------------------------------
    # We call generated files "artifacts".
    # They are important evidence of the work we did and the results we found.
    # We will save the anomalies_df DataFrame as a CSV file in the artifacts/ folder

    # Every Polars DataFrame has a write_csv() method that saves it as a CSV file.
    # Just pass in the full Path to the file you want to create.
    anomalies_df.write_csv(OUTPUT_FILE)
    LOG.info(f"Wrote anomalies file: {OUTPUT_FILE}")

    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")
    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
