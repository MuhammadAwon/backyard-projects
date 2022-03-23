# Caclulate frame per second (fps) of a video
import cv2 as cv

# Start the video
video = cv.VideoCapture('resources/grilled_steaks.mp4')

# Find OpenCV version
(major_ver, minor_ver, subminor_ver) = (cv.__version__).split('.')
print(f'OpenCV version: {major_ver}')

if int(major_ver) < 3:
    fps = video.get(cv.cv.CV_CAP_PROP_FPS)
    print(f'Frames per second: {int(fps)}')
else: 
    fps = video.get(cv.CAP_PROP_FPS)
    print(f'Frames per second: {int(fps)}')

video.release()