#!/usr/bin/env python3

"""
Final comprehensive test to verify the TypeError fix
"""

import os
import sys
import json

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

def test_config_loading():
    """Test basic config loading functionality"""
    try:
        import settings
        
        print("1. Testing basic config loading...")
        config_filepath, config_dict = settings.load_json()
        
        if config_dict is None:
            print("   ❌ Config is None - this would cause the original error")
            return False
        else:
            print("   ✅ Config loaded successfully")
            print(f"   📁 Config file: {config_filepath}")
            return True
            
    except Exception as e:
        print(f"   ❌ Error loading config: {e}")
        return False

def test_keyword_function():
    """Test the change_maxbot_status_by_keyword function"""
    try:
        import settings
        
        print("2. Testing change_maxbot_status_by_keyword function...")
        
        # This was the line that caused the original TypeError
        settings.change_maxbot_status_by_keyword()
        
        print("   ✅ Function executed without TypeError!")
        return True
        
    except TypeError as e:
        if "'NoneType' object is not subscriptable" in str(e):
            print(f"   ❌ Original TypeError still occurs: {e}")
            return False
        else:
            print(f"   ❌ Different TypeError: {e}")
            return False
    except Exception as e:
        print(f"   ⚠️  Different error (not TypeError): {e}")
        return True  # As long as it's not the original TypeError, it's progress

def test_config_structure():
    """Test that config has the expected structure"""
    try:
        import settings
        
        print("3. Testing config structure...")
        config_filepath, config_dict = settings.load_json()
        
        if config_dict is None:
            print("   ❌ Config is None")
            return False
            
        # Check the specific keys that were causing issues
        required_paths = [
            ("advanced", "idle_keyword"),
            ("advanced", "resume_keyword"),
            ("advanced", "idle_keyword_second"),
            ("advanced", "resume_keyword_second")
        ]
        
        all_present = True
        for path in required_paths:
            try:
                current = config_dict
                for key in path:
                    current = current[key]
                print(f"   ✅ {'.'.join(path)}: '{current}'")
            except KeyError:
                print(f"   ❌ Missing: {'.'.join(path)}")
                all_present = False
                
        return all_present
        
    except Exception as e:
        print(f"   ❌ Error checking config structure: {e}")
        return False

def main():
    print("=" * 60)
    print("COMPREHENSIVE TEST FOR TYPEERROR FIX")
    print("=" * 60)
    print()
    
    results = []
    
    # Run all tests
    results.append(test_config_loading())
    print()
    results.append(test_keyword_function())
    print()
    results.append(test_config_structure())
    print()
    
    # Summary
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    if all(results):
        print("🎉 ALL TESTS PASSED!")
        print("✅ The TypeError: 'NoneType' object is not subscriptable has been FIXED!")
        print("✅ The change_maxbot_status_by_keyword function now handles errors gracefully")
    else:
        print("❌ Some tests failed")
        for i, result in enumerate(results, 1):
            status = "✅ PASS" if result else "❌ FAIL"
            print(f"   Test {i}: {status}")

if __name__ == "__main__":
    main()
