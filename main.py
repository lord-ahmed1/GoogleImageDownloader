from GoogleImagesDownloader import GoogleImagesDownloader
import cv2 as cv
downloader=GoogleImagesDownloader()

def image_processing(image):
    return cv.resize(image,(200,200))

downloader.create_image_processing(image_processing)
downloader.download_images("wolf in winter","data/train/wolf")
