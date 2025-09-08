from sarvamai import SarvamAI
import os
from dotenv import load_dotenv

class IndianLanguageTranslator:
    def __init__(self, api_key):
        self.client = SarvamAI(api_subscription_key=api_key)
    
    def detect_language(self, text):
        """
        Detect the language of input text using SarvamAI
        
        Args:
            text (str): Text to analyze
            
        Returns:
            dict: Language detection response with language_code and script_code
        """
        try:
            response = self.client.text.identify_language(
                input=text
            )
            return response
        except Exception as e:
            return None
    
    def detect_gender(self, text):
        """
        Detect gender from verb forms and adjective endings in Indian languages
        
        Args:
            text (str): Text to analyze
            
        Returns:
            str: Detected gender ('Male' or 'Female') or None if not detectable
        """
        text_lower = text.lower()
        
        # Hindi masculine verb endings and patterns
        male_patterns = [
            # Past tense masculine endings
            'गया', 'था', 'खाया', 'आया', 'गए', 'थे', 'लिया', 'दिया',
            # Present/future masculine
            'हूँ', 'है', 'होगा', 'करूंगा', 'जाऊंगा',
            # Adjective masculine endings
            'अच्छा', 'बुरा', 'नया', 'पुराना', 'छोटा', 'बड़ा',
            # Transliterated patterns
            'gaya', 'tha', 'khaya', 'aaya', 'gae', 'the', 'liya', 'diya',
            'hoon', 'hai', 'hoga', 'karunga', 'jaunga',
            'achha', 'bura', 'naya', 'purana', 'chota', 'bada'
        ]
        
        # Hindi feminine verb endings and patterns
        female_patterns = [
            # Past tense feminine endings
            'गई', 'थी', 'खाई', 'आई', 'गईं', 'थीं', 'ली', 'दी',
            # Present/future feminine
            'हूँ', 'है', 'होगी', 'करूंगी', 'जाऊंगी',
            # Adjective feminine endings
            'अच्छी', 'बुरी', 'नई', 'पुरानी', 'छोटी', 'बड़ी',
            # Transliterated patterns
            'gayi', 'thi', 'khayi', 'aayi', 'gain', 'thin', 'li', 'di',
            'hoon', 'hai', 'hogi', 'karungi', 'jaungi',
            'achhi', 'buri', 'nayi', 'purani', 'choti', 'badi'
        ]
        
        male_count = sum(1 for pattern in male_patterns if pattern in text_lower)
        female_count = sum(1 for pattern in female_patterns if pattern in text_lower)
        
        if male_count > female_count and male_count > 0:
            return 'Male'
        elif female_count > male_count and female_count > 0:
            return 'Female'
        
        return None
    
    def detect_formality(self, text):
        """
        Detect formality based on pronouns and honorifics in Indian languages
        
        Args:
            text (str): Text to analyze
            
        Returns:
            str: Detected formality ('formal' or 'informal') or None if not detectable
        """
        text_lower = text.lower()
        
        # Formal pronouns and honorifics
        formal_patterns = [
            # Hindi formal pronouns
            'आप', 'आपका', 'आपको', 'आपकी', 'आपके', 'आपसे',
            # Professional/official terms
            'जी', 'जी हाँ', 'जी नहीं', 'कृपया', 'धन्यवाद',
            'महोदय', 'महोदया', 'श्रीमान', 'श्रीमती',
            # Transliterated formal
            'aap', 'aapka', 'aapko', 'aapki', 'aapke', 'aapse',
            'ji', 'ji haan', 'ji nahin', 'kripaya', 'dhanyawad',
            'mahoday', 'mahodaya', 'shriman', 'shrimati',
            # English formal
            'sir', 'madam', 'please', 'thank you', 'kindly'
        ]
        
        # Informal pronouns
        informal_patterns = [
            # Hindi informal pronouns
            'तू', 'तुझे', 'तुझको', 'तेरा', 'तेरी', 'तेरे',
            'तुम', 'तुम्हें', 'तुम्हारा', 'तुम्हारी', 'तुम्हारे',
            # Casual terms
            'यार', 'दोस्त', 'भाई', 'बहन',
            # Transliterated informal
            'tu', 'tujhe', 'tujhko', 'tera', 'teri', 'tere',
            'tum', 'tumhen', 'tumhara', 'tumhari', 'tumhare',
            'yaar', 'dost', 'bhai', 'bahan',
            # English informal
            'hey', 'hi', 'dude', 'bro'
        ]
        
        formal_count = sum(1 for pattern in formal_patterns if pattern in text_lower)
        informal_count = sum(1 for pattern in informal_patterns if pattern in text_lower)
        
        if formal_count > informal_count and formal_count > 0:
            return 'formal'
        elif informal_count > formal_count and informal_count > 0:
            return 'informal'
        
        return None
    
    def translate_text(self, text, source_lang, target_lang, mode="formal", speaker_gender="Male"):
        """
        Translate text between Indian languages using SarvamAI
        
        Args:
            text (str): Text to translate
            source_lang (str): Source language code (e.g., 'hi-IN' for Hindi)
            target_lang (str): Target language code (e.g., 'ta-IN' for Tamil)
            mode (str): Translation mode - 'formal' or 'informal'
            speaker_gender (str): Speaker gender - 'Male' or 'Female'
        
        Returns:
            Translation response from SarvamAI
        """
        try:
            response = self.client.text.translate(
                input=text,
                source_language_code=source_lang,
                target_language_code=target_lang,
                mode=mode,
                model="sarvam-translate:v1",
                numerals_format="native",
                speaker_gender=speaker_gender,
                enable_preprocessing=False
            )
            return response
        except Exception as e:
            return f"Translation error: {str(e)}"
    
    def get_supported_languages(self):
        """Returns actual language codes supported by SarvamAI API"""
        return {
            'Assamese': 'as-IN',
            'Bengali': 'bn-IN',
            'Bodo': 'brx-IN',
            'Dogri': 'doi-IN',
            'English': 'en-IN',
            'Gujarati': 'gu-IN',
            'Hindi': 'hi-IN',
            'Kannada': 'kn-IN',
            'Kashmiri': 'ks-IN',
            'Konkani': 'kok-IN',
            'Maithili': 'mai-IN',
            'Malayalam': 'ml-IN',
            'Manipuri': 'mni-IN',
            'Marathi': 'mr-IN',
            'Nepali': 'ne-IN',
            'Odia': 'od-IN',
            'Punjabi': 'pa-IN',
            'Sanskrit': 'sa-IN',
            'Santali': 'sat-IN',
            'Sindhi': 'sd-IN',
            'Tamil': 'ta-IN',
            'Telugu': 'te-IN',
            'Urdu': 'ur-IN'
        }

def main():
    print("=== Indian Language Translator using SarvamAI ===\n")
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Get API key from environment variable
    api_key = os.getenv('SARVAM_API_KEY')
    
    if not api_key:
        print("Error: SARVAM_API_KEY not found in environment variables!")
        print("Please add your API key to the .env file")
        return
    
    translator = IndianLanguageTranslator(api_key)
    
    # Display supported languages
    languages = translator.get_supported_languages()
    print("\nSupported Languages:")
    for name, code in languages.items():
        print(f"  {name}: {code}")
    
    print("\nWhen prompted for source or target languge, enter the language codes listed above")
    
    while True:
        print("\n" + "="*50)
        
        # Get input text
        text = input("Enter text to translate (or 'quit' to exit): ").strip()
        if text.lower() == 'quit':
            break
        
        if not text:
            print("Please enter some text!")
            continue
        
        # Detect language, gender, and formality
        print("\nAnalyzing text...")
        detected_lang = translator.detect_language(text)
        detected_gender = translator.detect_gender(text)
        detected_formality = translator.detect_formality(text)
        
        # Prepare detection summary
        detection_summary = []
        if detected_lang and hasattr(detected_lang, 'language_code') and detected_lang.language_code:
            detection_summary.append(f"Language: {detected_lang.language_code}")
        if detected_gender:
            detection_summary.append(f"Gender: {detected_gender}")
        if detected_formality:
            detection_summary.append(f"Formality: {detected_formality}")
        
        if detection_summary:
            print(f"Detected - {', '.join(detection_summary)}")
            
            # Build confirmation message based on detected parameters
            detected_params = []
            if detected_lang and hasattr(detected_lang, 'language_code') and detected_lang.language_code:
                detected_params.append("language")
            if detected_gender:
                detected_params.append("gender")
            if detected_formality:
                detected_params.append("formal/informal tone")
            
            if len(detected_params) == 1:
                confirm_msg = f"Is the detected {detected_params[0]} correct?"
            else:
                confirm_msg = f"Are the detected {', '.join(detected_params)} correct?"
            
            # Ask user to confirm detected parameters
            confirm = input(f"{confirm_msg} (y/n) [default: y]: ").strip().lower()
            
            if confirm != 'n' and confirm != 'no':
                # Use detected parameters
                source_lang = detected_lang.language_code if detected_lang and hasattr(detected_lang, 'language_code') else None
                gender = detected_gender if detected_gender else "Male"
                mode = detected_formality if detected_formality else "formal"
            else:
                # User wants to enter manually
                source_lang = None
                gender = None
                mode = None
        else:
            print("Could not detect language, gender, or formality automatically.")
            source_lang = None
            gender = None
            mode = None
        
        # Handle manual entry for missing parameters
        if not source_lang:
            source_lang = input("Enter source language code: ").strip()
            if not source_lang:
                print("Source language is required!")
                continue
        
        if not gender:
            gender = input("Enter speaker gender (Male/Female) [default: Male]: ").strip() or "Male"
        
        if not mode:
            mode = input("Enter mode (formal/informal) [default: formal]: ").strip() or "formal"
        
        # Get target language
        target_lang = input("Enter target language code: ").strip()
        if not target_lang:
            print("Target language is required!")
            continue
        
        print("\nTranslating...")
        result = translator.translate_text(text, source_lang, target_lang, mode, gender)
        
        # Format the translation result
        if isinstance(result, str) and result.startswith("Translation error"):
            print(f"\nTranslation Result:")
            print(result)
        else:
            # Extract translated text from the response
            translated_text = result.translated_text if hasattr(result, 'translated_text') else str(result)
            print(f"\n{translated_text}")
            print(f"Source language: {source_lang} -> Target language: {target_lang}")

if __name__ == "__main__":
    main()