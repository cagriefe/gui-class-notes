# Supports external language files. .lng

import glob  # Importing glob for file operations

class I18N:
    def __init__(self, language_code):
        if language_code in self.get_available_languages():  # Checking if the language is available
            self.translations = self.load_data_from_file(language_code)  # Loading translations from file
        else:
            raise NotImplementedError("Unsupported or missing lang file")  # Raising error for unsupported or missing language file
    
    @staticmethod
    def get_available_languages():
        language_files = glob.glob("*.lng")  # Getting all .lng files
        language_codes = []
        
        for f in language_files:
            language_code = f.replace("data_","").replace(".lng","")  # Extracting language code from file name
            language_codes.append(language_code)
            
        return language_codes  # Returning available language codes
    
    @staticmethod
    def load_data_from_file(language_code):
        language_file = f"data_{language_code}.lng"  # Constructing file name
        language_data = {}
        try:
            with open(language_file, encoding="utf-8") as f:  # Opening the language file
                for line in f:
                    (key, val) = line.strip().split("=")  # Splitting each line into key and value
                    language_data[key] = val  # Storing key-value pairs in dictionary
                    
        except FileNotFoundError:
            raise ValueError("file not exist")  # Raising error if file not found
        
        return language_data  # Returning the loaded data
    
    @staticmethod
    def get_language_name(language_code):
        language_file = f"data_{language_code}.lng"  # Constructing file name
        try:
            with open(language_file, encoding="utf-8") as f:  # Opening the language file
                for line in f:
                    (key, val) = line.strip().split("=")  # Splitting each line into key and value
                    if key == "language":
                        return val  # Returning the language name
                    
                raise ValueError("Language key not found")  # Raising error if language key not found
        except FileNotFoundError:
            raise ValueError("Language file not found")  # Raising error if file not found