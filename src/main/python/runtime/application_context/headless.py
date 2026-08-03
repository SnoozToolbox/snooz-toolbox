"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2023
See the file LICENCE for full license details.

Headless ApplicationContext for running Snooz without GUI dependencies.
This allows execution on Compute Canada and other headless servers.
"""
from runtime.application_context.base import BaseResourceApplicationContext


class HeadlessApplicationContext(BaseResourceApplicationContext):
    """Headless version of ApplicationContext that doesn't require Qt."""
    
    @property
    def app(self):
        """Return None for headless mode - no QApplication needed."""
        return None

