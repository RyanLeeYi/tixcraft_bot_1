"""
Simple test to check if settings.py has syntax errors
"""
try:
    print("Attempting to import settings...")
    import settings
    print("Settings imported successfully!")
    
    print("Testing load_json function...")
    config_filepath, config_dict = settings.load_json()
    print(f"Config loaded: {config_dict is not None}")
    
    if config_dict:
        print("Testing change_maxbot_status_by_keyword...")
        settings.change_maxbot_status_by_keyword()
        print("Function executed successfully!")
    else:
        print("Config is None, cannot test the function")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
