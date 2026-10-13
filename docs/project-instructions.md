# Project Instructions

## Goal

Apply **static anomaly detection** to identify unusual
observations using domain-specific rules and thresholds.

## A. Set Up Machine

Complete [Workflow A: Set Up Machine](https://denisecase.github.io/pro-analytics-02/workflow-a-set-up-machine/)
if your machine is not ready.

## B. Explore Example Project

Follow [Workflow B: Explore Example Project](https://denisecase.github.io/pro-analytics-02/workflow-b-explore-example-project/).

Explore how the example:

- Reads pediatric clinic data using Polars.
- Defines reasonable upper thresholds for age and height.
- Uses Boolean conditions to identify anomalous records.
- Saves the detected anomalies as a CSV artifact.

Review the example data, code, and results.

## C. Start New Project

Follow [Workflow C: Start New Project](https://denisecase.github.io/pro-analytics-02/workflow-c-start-new-project/).

IMPORTANT: New repository name:
**cintel-02-static-anomalies-custom**.

VERIFY: You have completed git add-commit-push to GitHub at least twice.

## D. Apply Skills

Follow [Workflow D: Apply Skills](https://denisecase.github.io/pro-analytics-02/workflow-d-apply-skills/).

**Your problem:** Identify potentially unusual records
in an adult clinic dataset.

Use the provided `data/clinic_data.csv`
as the starting dataset for your independent project.

### Progression 1. Your Project Works Like the Example

Ensure your new custom project runs like the example.

Verify that key files have been updated to use **your GitHub account** and
the **new custom repository name**.

### Progression 2. Make a Technical Modification

Change one detection threshold or condition.

Run the pipeline again and observe how the
detected anomalies change.

### Progression 3. Apply to a New Problem

Apply your pipeline to the adult clinic dataset.

- Define thresholds appropriate for the adult population.
- Explain why the thresholds are reasonable.
- Identify observations that violate the rules.
- Save the anomalies to an artifact.
- Interpret the results.

Anomalies are not necessarily errors.
They are observations that may require investigation.

## E. Finalize Project

Follow [Workflow E: Finalize Project](https://denisecase.github.io/pro-analytics-02/workflow-e-finalize/).

Use `docs/index.md` to report:

- Data and population.
- Detection rules and thresholds.
- Anomalies found.
- A visual displaying the results.
- Interpretation and limitations.

Include a clickable link to your repository and artifacts.

## Success

- [ ] README.md project-specific links use **your GitHub account**
- [ ] README.md project-specific links use **your custom repository name**.
- [ ] docs/index.md project-specific links use **your GitHub account**
- [ ] docs/index.md project-specific links use **your custom repository name**.
- [ ] pyproject.toml `name` has been changed to use **your custom repository name**.
- [ ] The `src/cintel` folder reflects your authorship and custom work.
- [ ] All necessary commands are provided and work successfully.
- [ ] Links to the Professional Python Guide (pro-analytics-02) remain unchanged.
- [ ] Commit history shows **at least** the git add-commit-push history required in the instructions.

---

[◄ Back to Home](index.md)
