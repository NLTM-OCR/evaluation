from .assamese import normalize_assamese
from .bengali import normalize_bengali
from .bodo import normalize_bodo
from .dogri import normalize_dogri
from .gujarati import normalize_gujarati
from .hindi import normalize_hindi
from .kannada import normalize_kannada
from .kashmiri import normalize_kashmiri
from .konkani import normalize_konkani
from .maithili import normalize_maithili
from .malayalam import normalize_malayalam
from .manipuri import normalize_manipuri
from .marathi import normalize_marathi
from .nepali import normalize_nepali
from .oriya import normalize_oriya
from .punjabi import normalize_punjabi
from .sanskrit import normalize_sanskrit
from .santali import normalize_santali
from .sindhi import normalize_sindhi
from .tamil import normalize_tamil
from .telugu import normalize_telugu


class Normalize:
    def __init__(self, language: str):
        self.language = language.lower().strip()
        func = f'normalize_{self.language}'
        if func not in globals():
            self.func = lambda x:x
        else:
            self.func = globals()[func]

    
    def run(self, text: str) -> str:
        try:
            text = text.strip()
            # replace 2 spaces in the text with a single space always
            while '  ' in text:
                text = text.replace('  ', ' ')
            return self.func(text).strip()
        except:
            return text