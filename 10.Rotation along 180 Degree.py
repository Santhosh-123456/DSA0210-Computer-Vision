import cv2
path =r"C:\Users\palas\OneDrive\Pictures\Screenshots\Screenshot 2024-02-21 090822.png"
src = cv2.imread(path)
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
sr = cv2.imread(path)
window_name = 'Image'
imag = cv2.rotate(sr, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow(window_name, imag)
cv2.waitKey(0)
