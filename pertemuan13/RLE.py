def rle_compress(text):
    compressed_text = ''
    count = 1

    # Traverse the text starting from the second character
    for i in range(1, len(text)):
        # If current character is same as previous character, increase the count
        if text[i] == text[i - 1]:
            count += 1
        else:
            # If current character is different, append the previous character and its count to the compressed text
            compressed_text += text[i - 1] + str(count)
            count = 1

    # Append the last character and its count to the compressed text
    compressed_text += text[-1] + str(count)

    return compressed_text

# Example usage
text = "CHHAAAAAEEELLLLLL"
compressed_text = rle_compress(text)
print("Compressed text:", compressed_text)
