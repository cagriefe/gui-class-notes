# early version (hardcoded)

class I18N:
    def __init__(self, language_code):
        if language_code == "en":
            self.load_text_in_english()  # Load text in English
        elif language_code == "tr":
            self.load_text_in_turkish()  # Load text in Turkish
        else:
            raise NotImplementedError("Unsupported")  # Raise error for unsupported languages
        
    def load_text_in_english(self):
        self.title = "Week 12"  # Title in English
        self.fname = "First Name"  # First name label in English
        self.lname = "Last Name"  # Last name label in English
        self.grade = "Grade"  # Grade label in English
        self.save = "Save Grade"  # Save button text in English
        
    def load_text_in_turkish(self):
        self.title = "Hafta 12"  # Title in Turkish
        self.fname = "Ad"  # First name label in Turkish
        self.lname = "Soyad"  # Last name label in Turkish
        self.grade = "Not"  # Grade label in Turkish
        self.save = "Notu kaydet"  # Save button text in Turkish