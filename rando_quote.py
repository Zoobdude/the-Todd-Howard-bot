import random

def put_quotes_around_random_word(input_message: str) -> str:
    input_message_list = input_message.split(" ")
    
    if "" in input_message_list:
        input_message_list = list(filter(None, input_message_list))
    
    random_index = random.randint(0, len(input_message_list)-1)
    input_message_list[random_index] = ('"'+input_message_list[random_index]+'"')
    
    return " ".join(input_message_list)

if __name__ == "__main__":
    print(put_quotes_around_random_word(input("Enter a message: ")))