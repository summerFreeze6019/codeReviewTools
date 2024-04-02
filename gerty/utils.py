import importlib.util
import sys

def import_from_path(path: str, module_name: str):
    """
    A simple importlib helper to test out some importlib functionality. 
    """
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
