import sys
from stats import word_count, appearance_count, sorted_lst

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return str(file_contents)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]
    
    num_words = word_count(get_book_text(path_to_book))
    num_chars = appearance_count(get_book_text(path_to_book))
    lst = sorted_lst(num_chars)

    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {path_to_book}...
    ----------- Word Count ----------
    Found {num_words} total words
    --------- Character Count -------""")
    
    for item in lst:
        if item["name"].isalpha():
            print(f"{item["name"]}: {item["num"]}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()