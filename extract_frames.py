import pafy
# pafy uses a module / library called youtube_dl so it's necessary to install it first.
import cv2

url = "https://www.youtube.com/watch?v=L1gDIzIY-6k"

Pafy_obj = pafy.new(url)
Stream_obj = Pafy_obj.getbestvideo(preftype="webm")
# print(Stream_obj.url)

capture_obj = cv2.VideoCapture(Stream_obj.url)
ret = True
index = 1
while ret:
    ret, frame = capture_obj.read()
    print(cv2.imwrite(r"d:\frames\{}.png".format(index), frame))  # do not specify path with hebrew
    index += 1
    # cv2.imshow("Window Title Here", frame)
    # cv2.waitKey(0)
# cv2.destroyAllWindows()