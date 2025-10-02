# ai_processor.py
from transformers import pipeline

class AIProcessor:
    def __init__(self):
        # Load a free, offline model for summarization
        print("Loading AI model... This may take a minute for the first time.")
        self.summarizer = pipeline("summarization", model="Falconsai/text_summarization")
        # Load a model for Named Entity Recognition (to find names, places, etc.)
        self.ner_tagger = pipeline("ner", model="Davlan/bert-base-multilingual-cased-ner-hrl")
        print("AI models loaded successfully!")

    def summarize_text(self, text):
        """Summarizes long text into a short paragraph."""
        if len(text) < 50:
            return "Text is too short to summarize effectively."
        try:
            summary = self.summarizer(text, max_length=150, min_length=30, do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            return f"Summarization failed: {e}"

    def extract_entities(self, text):
        """Extracts and categorizes key information like persons, organizations, and locations."""
        try:
            entities = self.ner_tagger(text)
            # Group entities by type
            grouped_entities = {}
            for entity in entities:
                entity_type = entity['entity']
                entity_word = entity['word']
                if entity_type not in grouped_entities:
                    grouped_entities[entity_type] = []
                if entity_word not in grouped_entities[entity_type]: # Avoid duplicates
                    grouped_entities[entity_type].append(entity_word)
            return grouped_entities
        except Exception as e:
            return f"Entity extraction failed: {e}"

if __name__ == "__main__":
    # Test the AI processor
    ai = AIProcessor()
    sample_text = "Earlier today, John Smith from Apple Inc. visited our London office. He met with Dr. Emily Jones to discuss a new security project. The meeting was productive and they agreed to follow up next week from their base in California."
    
    print("--- Summary ---")
    print(ai.summarize_text(sample_text))
    print("\n--- Extracted Entities ---")
    print(ai.extract_entities(sample_text))