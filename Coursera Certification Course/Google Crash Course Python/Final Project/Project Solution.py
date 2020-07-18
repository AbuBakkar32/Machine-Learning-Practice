def calculate_frequencies(file_contents):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]

    # LEARNER CODE START HERE
    words = file_contents.split(" ")
    word_lists = []

    for word in words:
        for uninteresting_word in uninteresting_words:
            if word is not uninteresting_words:
                word_lists.append(word)

    for word in words:
        if not word.isalpha():
            word = ''.join([letter for letter in word if word.isalpha()])

    word_dict = {}

    for word in word_lists:
        if word not in word_dict.keys():
            word_dict[word] = word_lists.count(word)

    return word_dict


myimage = calculate_frequencies()
print(myimage)
