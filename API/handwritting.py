import pywhatkit as kit

text = """
    Dear Sir,
        I'm writing this letter to inform you that I have been unable to attend the meeting on the following day 04-04-2022
        regarding the following reason:
            1. I have a meeting with Mr. John Doe on the same day.
            2. I have comitted to attend the meeting on the same day.
"""
kit.text_to_handwriting("Abu Bakkar Siddik", save_to="handwriting.png")
# img = cv2.imread("handwriting.png")
# cv2.imshow("Text to Handwriting", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
