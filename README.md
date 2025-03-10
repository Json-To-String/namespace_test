# namespace_test
Testing making a repository a namespace package

# should aim for:
https://packaging.python.org/en/latest/guides/packaging-namespace-packages/#pkgutil-style-namespace-packages

```
mynamespace-subpackage-a/
├── pyproject.toml # AND/OR setup.py, setup.cfg
└── src/
    └── mynamespace/ # namespace package/
        ├── ( No __init__.py here.)
        └── subpackage_a/
            ├── # Regular import packages have an __init__.py.
            ├── __init__.py
            └── module.py
```