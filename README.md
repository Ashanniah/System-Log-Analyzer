# System Log Analyzer

A Python command-line utility that automates application log analysis for IT operations teams.

The tool reads a sample log file, parses each entry into date/time/level/message, counts log levels, identifies recurring errors, determines the busiest hour, and generates an executive-style report.

## Project Structure

- `analyzer.py` - application entry point and workflow coordinator
- `parser.py` - log file reading and regex-based parsing
- `reports.py` - analysis logic and report generation
- `logger.py` - runtime audit logging setup
- `utils.py` - helper utilities for file and directory handling
- `sample.log` - sample input log file
- `logs/analyzer.log` - generated application log output
- `requirements.txt` - dependency notes

## Features

- Reads a log file and validates line format
- Parses `Date`, `Time`, `Level`, and `Message`
- Counts `INFO`, `WARNING`, and `ERROR` entries
- Finds recurring error messages and frequencies
- Determines the most active hour from log timestamps
- Generates a formatted analysis report
- Writes execution events to `logs/analyzer.log`
- Handles missing files, empty input, invalid formats, and permission errors gracefully

## Usage

From the project root, run:

```bash
python analyzer.py
```

## Expected Output

The analyzer prints a summary report similar to:

```text
=======================================
System Log Analyzer
=======================================

Loading log file...

=======================================
System Log Analysis Report
=======================================

Generated On       : 2026-07-09 20:15

Log Entries        : 5

Information        : 2

Warnings           : 1

Errors             : 2

Most Active Hour   : 08:00 - 08:59

Top Error

Database connection failed

2 occurrences

Recommendation

Investigate recurring database failures.
```

## Requirements

- Python 3.x
- No external dependencies required

## Notes

- The parser uses regular expressions for reliable log format validation
- The application is designed for simple CLI execution and modular extension
- Runtime activity is logged in `logs/analyzer.log`
