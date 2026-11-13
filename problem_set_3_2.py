
# get user string to redact
def get_user_srting ():
    user_string = input("Enter a sentence or phrase to have redacted (or type 'quit' to exit): ").strip().lower()
    return user_string

# get characters to redact
def get_redaction():
    redactions_input = input('Enter letters to redact seperated by a comma: ').strip().lower()
    
    redactions_list =[]

    # Split input and strip
    for item in redactions_input.split(","):
        cleaned_input = item.strip().lower()
        if cleaned_input:
            redactions_list.append(cleaned_input)
    return redactions_list

# redaction func
def redact_message(message, redactions):
    result_chars = []
    redaction_count = 0

    for char in message:
        lower_char = char.lower()

        # manually check for redactions
        is_match = False
        for target in redactions:
            if lower_char == target:
                is_match = True
                break

        if is_match:
            result_chars.append("-")
            redaction_count += 1
        else:
            result_chars.append(char)
    
    return "".join(result_chars), redaction_count #joins items in result_char, returns string and count


def main():
    print("Use this app to redact parts of a message!")

    while True:
        user_string = get_user_srting()

        # check for exit condition
        if user_string.lower() == 'quit':
            print ('Exiting, goodbye!')
            break   
        if not user_string:
            print("Please enter a valid phrase.\n")

        redactions = get_redaction()
        # redactions process
        redacted_text, count = redact_message(user_string, redactions)


        # output   
        print(f"Number of letters redacted: {count}")
        print(f"Redacted phrase: {redacted_text}\n")

main()