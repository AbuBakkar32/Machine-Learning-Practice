import time

String = 'Welcome Abu Bakkar Siddik'
wordcount = len(String.split())
print(String)
while True:
    t0 = time.time()
    input_text = str(input('Enter the Sentence:'))
    t1 = time.time()
    accuracy = len(set(input_text.split()) & set(String.split()))
    accuracy = accuracy / wordcount
    time_taken = t1 - t0
    wpm = wordcount / time_taken
    print("WPM", wpm, "Accuracy", accuracy, "Time taken", time_taken)
