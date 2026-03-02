import re
import sys

def count_words_in_latex(file_path):
    """
    Count words in a LaTeX document, excluding:
    - Everything before the first \section
    - Bibliography section
    - LaTeX commands
    - Math mode content
    - Tables and figure environments
    """
    
    with open('./EE.tex', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the start of the main content (first \section)
    section_match = re.search(r'\\section\{', content)
    if section_match:
        content = content[section_match.start():]
    
    # Remove bibliography section (everything from \section{Bibliography} to \end{document})
    bib_match = re.search(r'\\section\{Bibliography\}', content, re.IGNORECASE)
    if bib_match:
        content = content[:bib_match.start()]
    
    # Remove comments
    content = re.sub(r'%.*', '', content)
    
    # Remove math mode content (both inline $ $ and display \[ \])
    content = re.sub(r'\$.*?\$', '', content)
    content = re.sub(r'\\\[.*?\\\]', '', content, flags=re.DOTALL)
    
    # Remove table environments
    content = re.sub(r'\\begin\{table\}.*?\\end\{table\}', '', content, flags=re.DOTALL)
    content = re.sub(r'\\begin\{tabular.*?}.*?\\end\{tabular.*?}', '', content, flags=re.DOTALL)
    content = re.sub(r'\\begin\{tabularx\}.*?\\end\{tabularx\}', '', content, flags=re.DOTALL)
    
    # Remove figure environments
    content = re.sub(r'\\begin\{figure\}.*?\\end\{figure\}', '', content, flags=re.DOTALL)
    content = re.sub(r'\\begin\{minipage\}.*?\\end\{minipage\}', '', content, flags=re.DOTALL)
    
    # Remove common LaTeX commands but keep their content where appropriate
    content = re.sub(r'\\section\{([^}]*)\}', r'\1', content)
    content = re.sub(r'\\subsection\{([^}]*)\}', r'\1', content)
    content = re.sub(r'\\subsubsection\{([^}]*)\}', r'\1', content)
    content = re.sub(r'\\textbf\{([^}]*)\}', r'\1', content)
    content = re.sub(r'\\textit\{([^}]*)\}', r'\1', content)
    content = re.sub(r'\\emph\{([^}]*)\}', r'\1', content)
    
    # Remove other LaTeX commands (like \vspace, \newpage, etc.)
    content = re.sub(r'\\[a-zA-Z]+(\[.*?\])?(\{.*?\})?', ' ', content)
    
    # Remove remaining curly braces
    content = re.sub(r'[{}]', ' ', content)
    
    # Remove extra whitespace and newlines
    content = re.sub(r'\s+', ' ', content)
    
    # Split into words and count
    words = content.strip().split()
    word_count = len(words)
    
    return word_count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        # Default file path for testing
        file_path = "/home/claude/document.tex"
    
    try:
        word_count = count_words_in_latex(file_path)
        print(f"Word count (excluding title page and bibliography): {word_count}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")