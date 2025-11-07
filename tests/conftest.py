"""Configuration pytest pour les marqueurs personnalisés."""


def pytest_configure(config):
    """Ajoute le marqueur 'performance' pour les tests de performance."""
    config.addinivalue_line("markers", "performance: tests de performance")
