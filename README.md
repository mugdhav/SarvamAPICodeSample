Created for the Pie & AI: Exploring Indian AI event.
Contains a Jupyter Notebook with Python program that uses Sarvam API to translate user input text from one Indian language to another.
# SarvamAI Indian Language Translator

A Python application for translating text between Indian languages using the SarvamAI API, with intelligent detection of language, gender, and formality.

## Features

- **Multi-language Support**: Translates between 23 Indian languages including Hindi, Tamil, Bengali, Telugu, and more
- **Automatic Detection**: 
  - Language detection using SarvamAI's language identification
  - Gender detection from verb forms and adjective endings
  - Formality detection based on pronouns and honorifics
- **Context-Aware Translation**: Maintains gender agreement and formality levels in translations
- **Interactive CLI**: User-friendly command-line interface with confirmation prompts
- **Smart Defaults**: Uses detected parameters or falls back to sensible defaults

## Supported Languages

The translator supports 23 Indian languages with their respective language codes:

| Language | Code | Language | Code |
|----------|------|----------|------|
| Assamese | as-IN | Malayalam | ml-IN |
| Bengali | bn-IN | Manipuri | mni-IN |
| Bodo | brx-IN | Marathi | mr-IN |
| Dogri | doi-IN | Nepali | ne-IN |
| English | en-IN | Odia | od-IN |
| Gujarati | gu-IN | Punjabi | pa-IN |
| Hindi | hi-IN | Sanskrit | sa-IN |
| Kannada | kn-IN | Santali | sat-IN |
| Kashmiri | ks-IN | Sindhi | sd-IN |
| Konkani | kok-IN | Tamil | ta-IN |
| Maithili | mai-IN | Telugu | te-IN |
| | | Urdu | ur-IN |

## Prerequisites

- Python 3.7+
- SarvamAI API key
- Required Python packages: `sarvamai`, `python-dotenv`

## Installation

1. **Install dependencies**:
   ```bash
   pip install sarvamai python-dotenv
   ```

2. **Set up environment variables**:
   Create a `.env` file in the same directory with your SarvamAI API key:
   ```
   SARVAM_API_KEY=your_api_key_here
   ```

3. **Run the translator**:
   ```bash
   python sarvam_translator.py
   ```

## Usage

### Interactive Mode

Run the script to enter interactive mode:

```bash
python sarvam_translator.py
```

The application will:
1. Display all supported languages and their codes
2. Prompt you to enter text for translation
3. Automatically detect language, gender, and formality
4. Ask for confirmation of detected parameters
5. Request target language and translate the text

### Example Session

```
=== Indian Language Translator using SarvamAI ===

Supported Languages:
  Assamese: as-IN
  Bengali: bn-IN
  ...

Enter text to translate (or 'quit' to exit): मैं अच्छा हूँ

Analyzing text...
Detected - Language: hi-IN, Gender: Male, Formality: informal
Are the detected language, gender, formal/informal tone correct? (y/n) [default: y]: y

Enter target language code: ta-IN

Translating...
நான் நன்றாக இருக்கிறேன்
Source language: hi-IN -> Target language: ta-IN
```

### Programmatic Usage

You can also use the `IndianLanguageTranslator` class in your own code:

```python
from sarvam_translator import IndianLanguageTranslator
import os

# Initialize translator
translator = IndianLanguageTranslator(api_key=os.getenv('SARVAM_API_KEY'))

# Detect language
detection = translator.detect_language("मैं अच्छा हूँ")
print(detection.language_code)  # Output: hi-IN

# Detect gender and formality
gender = translator.detect_gender("मैं अच्छा हूँ")  # Output: Male
formality = translator.detect_formality("तुम कैसे हो?")  # Output: informal

# Translate text
result = translator.translate_text(
    text="मैं अच्छा हूँ",
    source_lang="hi-IN",
    target_lang="ta-IN",
    mode="informal",
    speaker_gender="Male"
)
print(result.translated_text)
```

## Class Reference

### `IndianLanguageTranslator`

#### Methods

**`__init__(self, api_key)`**
- Initializes the translator with SarvamAI API key
- Parameters: `api_key` (str) - Your SarvamAI API subscription key

**`detect_language(self, text)`**
- Detects the language of input text using SarvamAI
- Parameters: `text` (str) - Text to analyze
- Returns: Language detection response with language_code and script_code

**`detect_gender(self, text)`**
- Detects gender from verb forms and adjective endings
- Parameters: `text` (str) - Text to analyze
- Returns: 'Male', 'Female', or None if not detectable
- Supports: Hindi patterns (both Devanagari and transliterated)

**`detect_formality(self, text)`**
- Detects formality based on pronouns and honorifics
- Parameters: `text` (str) - Text to analyze
- Returns: 'formal', 'informal', or None if not detectable
- Supports: Hindi, English, and transliterated patterns

**`translate_text(self, text, source_lang, target_lang, mode="formal", speaker_gender="Male")`**
- Translates text between Indian languages
- Parameters:
  - `text` (str) - Text to translate
  - `source_lang` (str) - Source language code (e.g., 'hi-IN')
  - `target_lang` (str) - Target language code (e.g., 'ta-IN')
  - `mode` (str) - Translation mode ('formal' or 'informal')
  - `speaker_gender` (str) - Speaker gender ('Male' or 'Female')
- Returns: Translation response from SarvamAI

**`get_supported_languages(self)`**
- Returns dictionary of supported languages and their codes
- Returns: Dict mapping language names to language codes

## Detection Patterns

### Gender Detection
- **Male patterns**: Masculine verb endings (गया, था, etc.), adjectives (अच्छा, बड़ा, etc.)
- **Female patterns**: Feminine verb endings (गई, थी, etc.), adjectives (अच्छी, बड़ी, etc.)

### Formality Detection
- **Formal patterns**: आप, जी, कृपया, श्रीमान, sir, madam, etc.
- **Informal patterns**: तू, तुम, यार, दोस्त, hey, dude, etc.

## Error Handling

- Missing API key: Displays error message and exits gracefully
- Translation errors: Returns formatted error message with details
- Invalid input: Prompts user to re-enter required information

## Configuration

The application uses environment variables for configuration:
- `SARVAM_API_KEY`: Your SarvamAI API subscription key (required)

## Notes

- The application uses SarvamAI's `sarvam-translate:v1` model
- Numerals are formatted in native script format
- Preprocessing is disabled for more direct translations
- The CLI interface provides confirmation prompts for detected parameters to ensure accuracy
