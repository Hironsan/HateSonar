#!/usr/bin/env python
"""
Verification script for Python 3.9+ migration.
Run this after installing dependencies to verify the migration was successful.
"""

import sys

def check_python_version():
    """Check if Python version is 3.9 or higher."""
    print(f"Python version: {sys.version}")
    if sys.version_info < (3, 9):
        print("❌ ERROR: Python 3.9+ is required!")
        return False
    print("✅ Python version OK")
    return True

def check_imports():
    """Check if all required imports work."""
    try:
        import joblib
        print(f"✅ joblib {joblib.__version__}")
    except ImportError as e:
        print(f"❌ Failed to import joblib: {e}")
        return False
    
    try:
        import numpy
        print(f"✅ numpy {numpy.__version__}")
    except ImportError as e:
        print(f"❌ Failed to import numpy: {e}")
        return False
    
    try:
        import pandas
        print(f"✅ pandas {pandas.__version__}")
    except ImportError as e:
        print(f"❌ Failed to import pandas: {e}")
        return False
    
    try:
        import sklearn
        print(f"✅ scikit-learn {sklearn.__version__}")
    except ImportError as e:
        print(f"❌ Failed to import sklearn: {e}")
        return False
    
    try:
        import scipy
        print(f"✅ scipy {scipy.__version__}")
    except ImportError as e:
        print(f"❌ Failed to import scipy: {e}")
        return False
    
    return True

def check_hatesonar():
    """Check if hatesonar can be imported and works."""
    try:
        from hatesonar import Sonar
        print("✅ HateSonar imported successfully")
        
        # Try to create an instance
        sonar = Sonar()
        print("✅ Sonar instance created successfully")
        
        # Try a simple prediction
        result = sonar.ping(text="This is a test")
        print("✅ Sonar.ping() works correctly")
        print(f"   Result keys: {result.keys()}")
        
        return True
    except Exception as e:
        print(f"❌ Failed to test HateSonar: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all verification checks."""
    print("=" * 60)
    print("HateSonar Python 3.9+ Migration Verification")
    print("=" * 60)
    print()
    
    print("Step 1: Checking Python version...")
    version_ok = check_python_version()
    print()
    
    if not version_ok:
        print("Please install Python 3.9 or higher and try again.")
        sys.exit(1)
    
    print("Step 2: Checking dependencies...")
    imports_ok = check_imports()
    print()
    
    if not imports_ok:
        print("Please install dependencies: pip install -e .")
        sys.exit(1)
    
    print("Step 3: Testing HateSonar...")
    hatesonar_ok = check_hatesonar()
    print()
    
    if hatesonar_ok:
        print("=" * 60)
        print("✅ All checks passed! Migration successful!")
        print("=" * 60)
    else:
        print("=" * 60)
        print("❌ Some checks failed. Please review the errors above.")
        print("=" * 60)
        sys.exit(1)

if __name__ == "__main__":
    main()
