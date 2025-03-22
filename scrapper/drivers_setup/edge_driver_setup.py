"""
This module provides a function to configure and return a Selenium WebDriver for Microsoft Edge.

Classes:
    LogLevel (Enum): Defines log level settings for Selenium.

Functions:
    configure_edge_webdriver(webdriver_executable_path: str) -> webdriver.Edge:
        Configures the Selenium WebDriver with optimized settings and returns it.

Example usage:
    driver = configure_edge_webdriver("path/to/msedgedriver.exe")
"""

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from enum import Enum

class LogLevel(Enum):
    """Enum for defining log level settings in Selenium."""
    OFF = "0"
    ERROR = "1"
    WARNING = "2"
    INFO = "3"

def configure_edge_webdriver(webdriver_executable_path: str) -> webdriver.Edge:
    """
    Configures and returns a Selenium WebDriver for Microsoft Edge with optimized settings.

    Args:
        webdriver_executable_path (str): Path to the Microsoft Edge WebDriver executable.

    Returns:
        webdriver.Edge: Configured Microsoft Edge WebDriver instance.
    """
    edge_browser_options = Options()
    edge_browser_options.add_argument("--headless")
    edge_browser_options.add_argument("--disable-extensions")
    edge_browser_options.add_argument("--start-maximized")
    edge_browser_options.add_argument("--log-level=3")
    edge_browser_options.add_argument(f"--log-level={LogLevel.WARNING.value}")

    edge_service = Service(executable_path=webdriver_executable_path)
    edge_driver = webdriver.Edge(service=edge_service, options=edge_browser_options)

    return edge_driver
