#!/usr/bin/env python3
"""
Build script to create a standalone executable for Vietnamese Vowels App
"""

import subprocess
import sys
import platform
import os

def install_dependencies():
    """Install required packages"""
    print("Installing dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)

def build_executable():
    """Build the standalone executable using PyInstaller"""
    print("Building standalone executable...")

    # Determine the OS for appropriate options
    system = platform.system()

    # PyInstaller command
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",  # Single executable file
        "--windowed",  # No console window (GUI app)
        "--name", "VietnameseVowels",
        "--clean",  # Clean PyInstaller cache
        "--noconfirm",  # Replace output directory without asking
    ]

    # Add icon if on Windows
    if system == "Windows":
        cmd.extend(["--icon", "NONE"])  # Could add custom .ico file

    # Add hidden imports for audio libraries
    cmd.extend([
        "--hidden-import", "gtts",
        "--hidden-import", "pygame",
        "--hidden-import", "pygame.mixer",
        "--hidden-import", "pygame.time",
    ])

    # Exclude problematic modules
    cmd.extend([
        "--exclude-module", "cryptography",
        "--exclude-module", "ssl",
    ])

    # Add the main script
    cmd.append("vietnamese_vowels.py")

    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

    print("\n" + "="*50)
    print("BUILD COMPLETE!")
    print("="*50)

    # Show output location
    if system == "Windows":
        exe_name = "VietnameseVowels.exe"
    else:
        exe_name = "VietnameseVowels"

    dist_path = os.path.join("dist", exe_name)
    print(f"\nYour executable is at: {os.path.abspath(dist_path)}")
    print("\nYou can copy this file anywhere and run it!")

def main():
    print("="*50)
    print("Vietnamese Vowels App - Build Script")
    print("="*50)

    try:
        install_dependencies()
        build_executable()
    except subprocess.CalledProcessError as e:
        print(f"\nBuild failed with error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
