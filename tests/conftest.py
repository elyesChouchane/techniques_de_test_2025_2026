import pytest

def pytest_configure(config):
    config.addinivalue_line("markers", "performance: performance tests")