#!/usr/bin/env python
"""
Environment check script for Forge
This script verifies that your environment meets the requirements for running Forge.
"""

import sys
import platform

def check_python_version():
    """Check if Python version meets requirements"""
    print("Checking Python version...")
    version = sys.version_info
    print(f"  Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("  ❌ FAIL: Python 3.8 or higher is required")
        return False
    else:
        print("  ✓ PASS: Python version is compatible")
        return True

def check_imports():
    """Check if critical dependencies can be imported"""
    print("\nChecking critical dependencies...")
    
    required_modules = [
        ('yaml', 'PyYAML'),
        ('jinja2', 'Jinja2'),
        ('click', 'click'),
        ('requests', 'requests'),
        ('flask', 'Flask'),
    ]
    
    all_ok = True
    for module_name, package_name in required_modules:
        try:
            __import__(module_name)
            print(f"  ✓ {package_name}")
        except ImportError:
            print(f"  ❌ {package_name} - not installed")
            all_ok = False
    
    return all_ok

def check_forge_import():
    """Try importing the forge module"""
    print("\nChecking forge module...")
    try:
        sys.path.insert(0, '.')
        import forge
        print(f"  ✓ Forge module imported successfully")
        print(f"  Version: {forge.__version__}")
        return True
    except Exception as e:
        print(f"  ❌ Failed to import forge: {e}")
        return False

def main():
    print("=" * 60)
    print("Forge Environment Check")
    print("=" * 60)
    print()
    
    checks = [
        check_python_version(),
        check_imports(),
    ]
    
    # Only try to import forge if basic checks pass
    if all(checks):
        checks.append(check_forge_import())
    
    print()
    print("=" * 60)
    if all(checks):
        print("✓ All checks passed! Your environment is ready for Forge.")
    else:
        print("❌ Some checks failed. Please install missing dependencies:")
        print("   pip install -r requirements.txt")
    print("=" * 60)
    
    return 0 if all(checks) else 1

if __name__ == '__main__':
    sys.exit(main())
