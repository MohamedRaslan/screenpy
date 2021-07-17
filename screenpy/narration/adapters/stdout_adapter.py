"""
Logs the Narrator's narration using Python's standard logging library.
"""

import logging
from contextlib import contextmanager
from functools import wraps
from typing import Any, Callable, Generator, Optional

from screenpy import settings
from screenpy.narration import narrator

# pylint: disable=unused-argument


class StdOutAdapter:
    """Adapt the Narrator's microphone to allow narration to stdout."""

    chain_direction = narrator.BACKWARD
    logger = logging.getLogger("screenpy")

    def __init__(self, indent_manager: Optional["IndentManager"] = None) -> None:
        if indent_manager is None:
            indent_manager = IndentManager()
        self.indent = indent_manager

    def act(
        self, func: Callable, line: str, gravitas: Optional[str] = None
    ) -> Generator:
        """Wrap the act, to log the stylized title."""

        @wraps(func)
        def func_wrapper(*args: Any, **kwargs: Any) -> Callable:
            """Wrap the func, so we log at the correct time."""
            self.logger.info(f"ACT {line.upper()}")
            return func(*args, **kwargs)

        yield func_wrapper

    def scene(
        self, func: Callable, line: str, gravitas: Optional[str] = None
    ) -> Generator:
        """Wrap the scene, to log the stylized title."""

        @wraps(func)
        def func_wrapper(*args: Any, **kwargs: Any) -> Callable:
            """Wrap the func, so we log at the correct time."""
            self.logger.info(f"Scene: {line.title()}")
            return func(*args, **kwargs)

        yield func_wrapper

    def beat(self, func: Callable, line: str) -> Generator:
        """Wrap the beat, to log the line, and increase the indent level."""

        @wraps(func)
        def func_wrapper(*args: Any, **kwargs: Any) -> Callable:
            """Wrap the func, so we log at the correct time."""
            self.logger.info(f"{self.indent}{line}")
            with self.indent.next_level():
                return func(*args, **kwargs)

        yield func_wrapper

    def aside(self, func: Callable, line: str) -> Generator:
        """Wrap the aside, to log the line."""

        @wraps(func)
        def func_wrapper(*args: Any, **kwargs: Any) -> Callable:
            """Wrap the func, so we log at the correct time."""
            self.logger.info(f"{self.indent}{line}")
            return func(*args, **kwargs)

        yield func_wrapper


class IndentManager:
    """Handle the indentation for CLI logging."""

    def __init__(self) -> None:
        self.level = 0
        self.indent = settings.INDENT_SIZE
        self.whitespace = self.indent * settings.INDENT_CHAR
        self.enabled = settings.INDENT_LOGS

    def add_level(self) -> None:
        """Increase the indentation level."""
        self.level += 1

    def remove_level(self) -> None:
        """Decrease the indentation level."""
        if self.level > 0:
            self.level -= 1

    @contextmanager
    def next_level(self) -> Generator:
        """Move to the next level of indentation, with context."""
        self.add_level()
        try:
            yield self.level
        finally:
            self.remove_level()

    def __str__(self) -> str:
        """Allow this manager to be used directly for string formatting."""
        if self.enabled:
            return f"{self.level * self.whitespace}"
        return ""
