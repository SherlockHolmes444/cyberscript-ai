# main.py
from document_loader import load_document
from ai_processor import AIProcessor

def main():
    ai_tool = AIProcessor()
    print("\n=== Welcome to CyberScriptAI ===")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Analyze a text file")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ").strip()
        
        if choice == '1':
            file_path = input("Enter the full path to your text file: ").strip().strip('"')
            print(f"\nLoading file: {file_path}")
            document_content = load_document(file_path)
            
            if document_content.startswith("Error:"):
                print(document_content)
                continue
                
            print("\n" + "="*50)
            print("SUMMARY:")
            print("="*50)
            summary = ai_tool.summarize_text(document_content)
            print(summary)
            
            print("\n" + "="*50)
            print("EXTRACTED KEY INFORMATION:")
            print("="*50)
            entities = ai_tool.extract_entities(document_content)
            for entity_type, words in entities.items():
                print(f"{entity_type}: {', '.join(words)}")
                
        elif choice == '2':
            print("Thank you for using CyberScriptAI. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()