import base64

def decode_base64(data):
    try:
        return base64.b64decode(data).decode('utf-8')
    except:
        return None

def decode_until_plain(data):
    decoded_data = data
    while True:
        new_data = decode_base64(decoded_data)
        if new_data is None or new_data == decoded_data:
            break
        decoded_data = new_data
    return decoded_data

def main():
    # Read the content of the input file
    with open('input.txt', 'r') as file:
        encoded_data = file.read()

    # Decode until plain text
    decoded_result = decode_until_plain(encoded_data)

    # Print the final result
    print(decoded_result)

if __name__ == "__main__":
    main()
