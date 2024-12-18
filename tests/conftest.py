"""
This module contains pytest hooks and custom fixtures for test collection and setup.
"""
from __future__ import annotations
import json
import pytest

class ManifestDirectory(pytest.Directory):
    """
    Custom pytest directory collector that reads a `manifest.json` file
    and collects test files defined in it instead of the default behavior.
    """
    def collect(self):
        """
        Collects test files listed in the `manifest.json` and yields them for pytest collection.
        """
        manifest_path = self.path / "manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        ihook = self.ihook
        for file in manifest["files"]:
            yield from ihook.pytest_collect_file(
                file_path=self.path / file, parent=self
            )

@pytest.hookimpl
def pytest_collect_directory(path, parent):
    """
    Custom pytest hook to collect test files from a directory if it contains
    a `manifest.json` file, otherwise falls back to default behavior.
    """
    if path.joinpath("manifest.json").is_file():
        return ManifestDirectory.from_parent(parent=parent, path=path)
    return None

@pytest.fixture(scope="session", autouse=True)
def callattr_ahead_of_alltests(request):
    """
    This fixture ensures that the `callme` method is called on each test class
    before any tests are executed, but only once per session.
    """
    print("callattr_ahead_of_alltests called")
    seen = {None}
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        if cls not in seen:
            if hasattr(cls.obj, "callme"):
                cls.obj.callme()  # Call the `callme` method if it exists
            seen.add(cls)
