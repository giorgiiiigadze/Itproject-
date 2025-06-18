import sys

empty_dict = {}
filename = 'text.txt'

def choose_language(first_language, second_language): 
    # ეს ფუნქცია ამოწმებს არჩეულ ენებს და თუ შეესაბამება ქართულ-ინგლისურს,
    # კითხულობს ტექსტურ ფაილს და ქმნის ლექსიკონს (სიტყვების წყვილების მიხედვით)
    try:
        with open(filename, 'r', encoding='utf-8') as file: # ფაილის გახსნა კოდირებით UTF-8
            lines = [line.strip() for line in file]

            for characters in lines:
                
                splited_characters = characters.split('-') # ხაზის გაყოფა "-" ზე
                if len(splited_characters) == 2: 

                    key = splited_characters[0].strip()

                    value = splited_characters[1].strip() 

                    if first_language == 'georgian' and second_language == 'english':
                        empty_dict[key] = value

                    elif first_language == 'english' and second_language == 'georgian':
                        empty_dict[value] = key

                    else:
                        print("No language found with that name!")
                        sys.exit()

    except FileNotFoundError:
        print("File could not be found")
    except Exception as e: # შეცდომის დამუშავება
        print(e)

def translate_word(first_language_word):
    # ეს ფუნქცია ცდილობს თარგმნოს სიტყვა და თუ ვერ პოულობს, სთავაზობს მომხმარებელს დაამატოს იგი
    if first_language_word in empty_dict:
        print(f"Translated word for {first_language_word} into {second_language} is: {empty_dict.get(first_language_word)}")

    elif len(first_language_word) == 0:
        print("Word must be more that 1 characters")
        sys.exit()

    elif first_language_word.isdigit():
        print("Word must only contain letters")
        sys.exit()
        
    else:
        print("Word not found inside dictanary") # სიტყვა ვერ მოიძებნა ლექსიკონში
        add_word_input = input("Would you like to add this word into the dictanary?(YES / NO):").strip().lower()
        
        
        if add_word_input == 'yes':
            new_word = input(f"Enter {second_language} translated word for {first_language_word}:").strip()
            # ვამოწმებთ რომელი ენა გვაქ არჩეული, რომ იმის მიხედვით ჩავწეროთ ფაილში
            try:
                if first_language == 'georgian':
                    line = f'{first_language_word}-{new_word}\n'
                elif first_language == 'english':
                    line = f'{new_word}-{first_language_word}\n'

                with open(filename, 'a', encoding='utf-8') as file:
                    file.write(line) # ახალი წყვილის დამატება ფაილში
                    
            except Exception as e:
                print(e)
            print("Word has been added to the dictanary!")
            
        elif add_word_input == 'no':
            print("Program has stopped working") # პროგრამის დასრულება
            sys.exit()
        else:
            print("Please enter valid information")  # არასწორი ინფორმაცია
            sys.exit()

if __name__ == '__main__':
    # პროგრამის მთავარი ნაწილი: იძახებს ენების არჩევას და თარგმნის ფუნქციას
    try:
        first_language = input("Enter the first language:").strip().lower()#პირველი ენა
        second_language = input("Enter the second language:").strip().lower() # მეორე ენა
    except KeyboardInterrupt:
        print('\nInput cancelled, "KeyboardInterrupt" Error')# შეყვანის შეწყვეტის დამუშავება
        sys.exit()
    
    choose_language(first_language, second_language)
    
    try:
        first_language_word = input(f"Enter a {first_language} word:").strip()  # სათარგმნი სიტყვა
    except KeyboardInterrupt:
        print('\nInput cancelled, "KeyboardInterrupt" Error')
        sys.exit()
    
    translate_word(first_language_word)
