def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents    

from stats import word_count

from stats import count_characters

from stats import sorted_characters



def main():
    import sys
    print(sys.argv)

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]   
    
        

    
    text = get_book_text(path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book fount at {path}...")
    
    
    num_words = word_count(text)
    print("----------- Word Count-----------")
    print(f"Found {num_words} total words")

    char_counts = count_characters(text)
    sorted_list = sorted_characters(char_counts)

    print("--------- Character Count ---------")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
   
   


        





if __name__ == "__main__":   
    main()





    



