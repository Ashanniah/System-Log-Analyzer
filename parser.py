import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

LOG_LINE_PATTERN = re.compile(r"^(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(INFO|WARNING|ERROR)\s+(.*)$")


class LogParseError(Exception):
    pass


@dataclass
class LogEntry:
    date: str
    time: str
    level: str
    message: str


class LogParser:
    def __init__(self, path: Path) -> None:
        self.path = path

    def parse(self) -> List[LogEntry]:
        lines = self._read_lines()
        parsed = []

        for line_number, raw_line in enumerate(lines, start=1):
            text = raw_line.strip()
            if not text:
                continue

            entry = self._parse_line(text, line_number)
            parsed.append(entry)

        return parsed

    def _read_lines(self) -> List[str]:
        try:
            with self.path.open("r", encoding="utf-8") as file:
                return file.readlines()
        except FileNotFoundError as error:
            raise FileNotFoundError(f"Log file not found: {self.path}") from error
        except PermissionError as error:
            raise PermissionError(f"Permission denied when opening log file: {self.path}") from error

    def _parse_line(self, line: str, line_number: int) -> LogEntry:
        match = LOG_LINE_PATTERN.match(line)
        if not match:
            raise LogParseError(f"Invalid log format on line {line_number}: {line}")

        date, time, level, message = match.groups()
        return LogEntry(date=date, time=time, level=level, message=message)
