# Project Instructions

## WEDNESDAY: Complete Workflow Phase 1-3

Follow the instructions in
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/).

Complete:

1. Phase 1. **Start & Run** – copy the project and confirm it runs
2. Phase 2. **Change Authorship** – update the project to your name and GitHub account
2. Phase 3. **Read & Understand** – review the project structure and code

## FRIDAY/SUNDAY: Complete Workflow Phases 4-5

Complete:

1. Phase 4. **Make a Technical Modification**
2. Phase 5. **Apply the Skills to a New Problem**

## Topic

**Static anomaly detection** using simple domain thresholds.

In this project, you will detect anomalies in static tabular data by defining and applying reasonable maximum thresholds.

## Learning Objectives

After completing this project, you should be able to:

- Define what an anomaly is within a specific domain context.
- Explain how domain knowledge influences anomaly detection.
- Read a CSV file into a DataFrame.
- Apply boolean filtering to detect threshold violations.
- Write anomaly results to an artifacts file.
- Run and validate a professional Python project using `uv`.

## Example Code

The example file is located in `src/cintel/`.

It demonstrates:

- reading a CSV file into a DataFrame
- defining simple maximum thresholds
- detecting rows where values exceed those thresholds
- logging the pipeline process
- writing anomalies to an artifacts CSV file

Make sure you have read and successfully run the example before creating your own version.

## Dataset

The example dataset is located in the `data/` folder.

Each row represents one observation and includes:

- `age_years` - age in years
- `height_inches` - height in inches

The example data represents a **pediatric clinic**.

Your version of the dataset is already provided.
It represents an **adult clinic**.

- `data/static_data_yourname.csv`

## Your Phase 4: Technical Modification Task

Since this is the first time, we'll help you plan the technical modification task.

Using the example as a guide:

1. Copy `src/cintel/anomaly_detector_case.py`.
2. Rename the copy to `src/cintel/anomaly_detector_yourname.py` (all lowercase, no spaces).
3. Update your Python file so it reads from `data/static_data_yourname.csv`.
4. Define reasonable maximum thresholds for:
   - age (in years)
   - height (in inches)
5. Detect anomalies using your thresholds.
6. Output anomalies to your custom artifacts file.
7. Ensure your script logs meaningful output.

Use your new Python file with the provided `_case` dataset first.

This phase is mainly about confirming that:

- your copied file runs
- your renamed module runs correctly
- you understand how the file name, module name, and run command connect

### Phase 5: Apply the Skills

Use your Python file with `data/static_data_yourname.csv`.

This dataset represents an adult clinic, so your **thresholds should be different** from the pediatric example.

Then update your code and documentation in `docs/` to explain:

- what population your file represents
- what thresholds you chose
- why those thresholds are reasonable
- what anomalies you found

Your logic should remain simple.
You do not need to introduce advanced statistical methods in this module.

## What to Look For

- Which rows clearly violate your thresholds?
- Are there borderline cases?
- How do adult thresholds differ from pediatric thresholds?
- Would your thresholds change with more domain knowledge?
- How might this process change if the data were updated continuously?

This discussion connects static anomaly detection to **continuous intelligence systems**, where observations arrive repeatedly over time and anomalies may signal changes in system behavior.

## Optional (Advanced)

If you would like to apply these skills to a real dataset instead of the provided example data, see suggested datasets:

https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/
