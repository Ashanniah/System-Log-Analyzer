from datetime import datetime
import time
from pathlib import Path

from logger import setup_logger
from parser import LogParser, LogParseError
from reports import generate_analysis_report
from utils import ensure_logs_directory

LOG_FILE = Path("sample.log")
LOG_PATH = Path("logs") / "analyzer.log"


def main() -> None:
    print("=" * 39)
    print("System Log Analyzer")
    print("=" * 39)
    print()
    print("Loading log file...")
    print()

    ensure_logs_directory(LOG_PATH.parent)
    logger = setup_logger(LOG_PATH)
    logger.info("Application Started")

    try:
        # Read and parse entries with progress feedback
        print("Reading entries...")
        start_time = time.perf_counter()
        parser = LogParser(LOG_FILE)
        entries = parser.parse()
        print(f"✓ {len(entries)} log entries loaded.")
        logger.info("Log Loaded")

        if not entries:
            raise ValueError("Log file is empty.")

        print()
        print("Analyzing log levels...")
        # Generate report and include source and execution time
        exec_time = time.perf_counter() - start_time
        report = generate_analysis_report(entries, source=LOG_FILE.name, execution_time=exec_time)
        print("✓ Completed.")
        print()
        print(report)
        logger.info("Report Generated")

        logger.info("Application Closed")
    except (FileNotFoundError, PermissionError, ValueError, LogParseError) as error:
        print("Error")
        print()
        print("Unable to load log file.")
        logger.error("%s", error)
        logger.info("Application Closed")


if __name__ == "__main__":
    main()
