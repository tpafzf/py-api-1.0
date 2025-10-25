"""
Export conda environment to requirements.txt for Docker/containerization
Run this in your conda environment: python tools/export_requirements.py
"""

import subprocess
import sys

def export_requirements():
    """Export conda environment packages to requirements.txt"""
    try:
        # Get list of pip-installed packages in the conda environment
        print("Exporting conda environment to requirements.txt...")
        
        result = subprocess.run(
            ['pip', 'list', '--format=freeze'],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Write to requirements.txt
        with open('requirements.txt', 'w') as f:
            f.write(result.stdout)
        
        print("✓ Successfully created requirements.txt")
        print("\nTo verify, check the contents:")
        print("  cat requirements.txt  # Linux/Mac")
        print("  type requirements.txt  # Windows")
        
        print("\nFor Docker, you can now use:")
        print("  FROM python:3.11-slim")
        print("  COPY requirements.txt .")
        print("  RUN pip install -r requirements.txt")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error exporting requirements: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    export_requirements()

