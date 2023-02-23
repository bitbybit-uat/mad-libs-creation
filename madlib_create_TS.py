#
# This Code was written by Timothy Strickland with help from Micha and W3 schools. 
#
number = 1
# Function to create a mad-libs story
def create_madlibs():
    global number
    # Prompt the user for a story template
    story = input("Enter a story with words you want to replace denoted by curly braces (e.g., 'Once upon a time, there was a {agile} {dolphin}.'): ")
    # Create a list of the word types used in the story
    word_types = [word_type[1:-1] for word_type in story.split() if word_type.startswith("{") and word_type.endswith("}")]
    # Prompt the user for words of each type
    words = {}
    for word_type in word_types:
        word = input(f"What word type do you want to replace {word_type} with: ")
        words[word_type] = '\"' + word + '\"'
    # Replace the blanks in the Story with the user's words
    finaltemplate = story.format(**words)
    # Save the story to a text file
    filename = f"madlibs_story{number}.txt"
    with open(filename, "w") as file:
        file.write(finaltemplate)
    print(f"Story saved to {filename}.")
    number += 1

def main():
# Call the create_madlibs function to create a new mad-libs story
    create_madlibs()
    restart = input("Type yes if you want to continue otherwise press Enter: ")
    # restart = restart.lower
    print(restart)
    if restart == "yes": 
        main()
    else:
        return

if __name__ == "__main__":
    main()
