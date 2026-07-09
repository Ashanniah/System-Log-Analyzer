from collections import Counter
from datetime import datetime
from typing import List

from parser import LogEntry


def count_levels(entries: List[LogEntry]) -> Counter:
    return Counter(entry.level for entry in entries)


def top_errors(entries: List[LogEntry], limit: int = 3) -> Counter:
    error_messages = [entry.message for entry in entries if entry.level == "ERROR"]
    return Counter(error_messages).most_common(limit)


def busiest_hour(entries: List[LogEntry]) -> tuple[str, int]:
    hours = [entry.time[:2] for entry in entries]
    counts = Counter(hours)
    most_common = counts.most_common(1)
    if not most_common:
        return "00", 0
    return most_common[0]


def generate_analysis_report(entries: List[LogEntry], source: str = "sample.log", execution_time: float = 0.0, status: str = "COMPLETED") -> str:
    counts = count_levels(entries)
    info_count = counts.get("INFO", 0)
    warning_count = counts.get("WARNING", 0)
    error_count = counts.get("ERROR", 0)

    total = len(entries)
    def pct(n: int) -> str:
        if total == 0:
            return "0%"
        return f"{round((n/total)*100)}%"

    hour, event_count = busiest_hour(entries)
    top_error_list = top_errors(entries, limit=3)

    if not top_error_list:
        top_error_text = "No errors found."
    else:
        top_error_text = "\n\n".join(
            f"{message}\n\n{count} occurrence{'s' if count != 1 else ''}" for message, count in top_error_list
        )

    generated_on = datetime.now().strftime("%Y-%m-%d %H:%M")
    report_lines = [
        "=" * 39,
        "System Log Analysis Report",
        "=" * 39,
        "",
        f"Generated On       : {generated_on}",
        f"Source             : {source}",
        "",
        f"Log Entries        : {total}",
        "",
        f"Information        : {info_count} ({pct(info_count)})",
        "",
        f"Warnings           : {warning_count} ({pct(warning_count)})",
        "",
        f"Errors             : {error_count} ({pct(error_count)})",
        "",
        f"Most Active Hour   : {hour}:00 - {hour}:59",
        "",
        f"Execution Time     : {execution_time:.3f} seconds",
        "",
        f"Analysis Status    : {status}",
        "",
        "Top Error",
        "",
        top_error_text,
        "",
        "Recommendations",
        "",
        "1. Investigate recurring database connection failures.",
        "2. Review database availability during peak activity.",
        "3. Monitor application logs for repeated errors and add alerting where appropriate.",
    ]

    return "\n".join(report_lines)
