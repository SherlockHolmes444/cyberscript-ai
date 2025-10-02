# document_loader.py
import os

def load_document(file_path):
    """
    Loads the content from a text-based file.
    """
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            return f"Error: The file '{file_path}' does not exist."
        
        # Handle different file types. For now, we treat all as text.
        # (This is where you could later add PDF or DOCX parsing)
        if file_path.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        else:
            # For non-.txt files, we still try to read them as text.
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
            return content
            
    except Exception as e:
        return f"An error occurred while loading the document: {e}"

# A simple test to see if our function works
if __name__ == "__main__":
    # Create a sample text file for testing
    sample_text = "This is a sample log entry. IP address 192.168.1.1 attempted a connection at 2023-10-02."
    with open('sample_log.txt', 'w') as f:
        f.write(sample_text)
    
    # Test the loader
    content = load_document('sample_log.txt')
    print("Loaded content:", content)