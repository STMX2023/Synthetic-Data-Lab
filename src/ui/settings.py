import json
import os
from pathlib import Path

class Settings:
    def __init__(self):
        self.settings_dir = Path.home() / '.synthetic_data_lab'
        self.settings_file = self.settings_dir / 'settings.json'
        self.settings = self._load_settings()

    def _load_settings(self):
        if not self.settings_dir.exists():
            self.settings_dir.mkdir(parents=True)
        
        if not self.settings_file.exists():
            default_settings = {
                'theme': 'dark'  # Changed default theme to dark
            }
            self._save_settings(default_settings)
            return default_settings
        
        try:
            with open(self.settings_file, 'r') as f:
                return json.load(f)
        except:
            return {'theme': 'dark'}  # Changed fallback theme to dark

    def _save_settings(self, settings):
        with open(self.settings_file, 'w') as f:
            json.dump(settings, f, indent=2)

    def get_theme(self):
        return self.settings.get('theme', 'light')

    def set_theme(self, theme):
        self.settings['theme'] = theme
        self._save_settings(self.settings)
