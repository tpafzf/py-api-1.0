"""
Test script to verify nfl-data-py installation
"""

try:
    import nfl_data_py as nfl
    import pandas as pd
    import numpy as np
    
    print("✓ Successfully imported nfl_data_py")
    print("✓ Successfully imported pandas")
    print("✓ Successfully imported numpy")
    print("\nLibrary versions:")
    print(f"  - pandas: {pd.__version__}")
    print(f"  - numpy: {np.__version__}")
    
    # Test basic functionality - get list of available seasons
    print("\n✓ Testing nfl-data-py functionality...")
    print("  Available functions in nfl_data_py:")
    functions = [func for func in dir(nfl) if not func.startswith('_')]
    for func in functions[:10]:  # Show first 10 functions
        print(f"    - {func}")
    if len(functions) > 10:
        print(f"    ... and {len(functions) - 10} more")
    
    print("\n✅ All tests passed! nfl-data-py is ready to use.")
    print("\nYou can now use functions like:")
    print("  - nfl.import_seasonal_data([2023])")
    print("  - nfl.import_weekly_data([2023])")
    print("  - nfl.import_players()")
    
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("Please make sure you're running this in your conda environment (madden-env)")
except Exception as e:
    print(f"❌ Error: {e}")

