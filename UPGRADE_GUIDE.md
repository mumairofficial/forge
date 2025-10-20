# Upgrade Guide

## Python 3 Migration and Dependency Updates

This project has been updated to work with modern Python 3 (Python 3.8+) and the latest package versions. Python 2 is no longer supported.

### Breaking Changes

#### Python Version Requirement
- **Minimum Python version**: Python 3.8+
- **Python 2.x**: No longer supported
- **Recommended**: Python 3.10 or higher

#### Updated Dependencies

All dependencies have been updated to their latest versions to address security vulnerabilities and compatibility issues:

**Critical Security Updates:**
- `PyYAML`: 3.12 → 6.0.1+ (CVE fixes)
- `Flask`: 0.12.1 → 3.0.0+ (Multiple CVE fixes)
- `Jinja2`: 2.9.6 → 3.1.3+ (Security fixes)
- `requests`: 2.18.4 → 2.31.0+ (Security fixes)

**Other Major Updates:**
- `blessed`: 1.14.2 → 1.20.0+
- `eventlet`: 0.20.0 → 0.35.0+
- `flask-cors`: 3.0.2 → 4.0.0+
- `flask-socketio`: 2.8.6 → 5.3.0+
- `pytest`: 3.1.2 → 8.0.0+
- `click`: 6.7 → 8.1.7+
- `jsonschema`: 2.6.0 → 4.21.0+
- `boto3`: 1.5.5 → 1.34.0+
- And more...

#### Removed Dependencies
- `scout.py`: This package is no longer maintained and is incompatible with Python 3.12+. 
  - The telemetry functionality has been made optional
  - The application will work without it

### Code Changes

If you have extended or customized Forge, you may need to update your code:

#### 1. API Changes
- The `async` parameter in executor has been renamed to `is_async` (async became a reserved keyword in Python 3.7)
  ```python
  # Old (Python 2)
  exe = executor("name", async=True)
  
  # New (Python 3)
  exe = executor("name", is_async=True)
  ```

#### 2. Import Changes
- `StringIO` → `io.StringIO`
- `basestring` → `str`
- `long` → `int` (merged with int in Python 3)

#### 3. YAML Loading
- `yaml.load()` now requires a Loader parameter for security
  ```python
  # Old
  data = yaml.load(content)
  
  # New
  data = yaml.load(content, Loader=yaml.FullLoader)
  ```

### Installation

```bash
# Install updated dependencies
pip install -r requirements.txt

# For development
pip install -r dev-requirements.txt
```

### Testing Your Upgrade

After upgrading, test your installation:

```bash
# Check Python version
python --version  # Should be 3.8 or higher

# Try importing forge
python -c "import forge"

# Run tests (once dependencies are installed)
pytest forge/tests/
```

### Known Issues

1. **Network connectivity**: If you experience timeouts when installing packages, try:
   ```bash
   pip install --default-timeout=300 -r requirements.txt
   ```

2. **Scout.py telemetry**: The optional telemetry provided by scout.py is disabled. This doesn't affect core functionality.

### Migration Checklist

- [ ] Verify Python 3.8+ is installed
- [ ] Update dependencies: `pip install -r requirements.txt`
- [ ] Update any custom code that uses the `async` parameter
- [ ] Update any custom YAML loading code to include `Loader` parameter
- [ ] Test your forge workflows
- [ ] Update CI/CD pipelines to use Python 3.8+

### Getting Help

If you encounter issues during the upgrade:
1. Check this guide for common issues
2. Verify your Python version matches requirements
3. Ensure all dependencies installed correctly
4. Open an issue on GitHub with details about your environment
