from deepstack import Detection,ServerConfig,pilToBytes
import os
import cv2 
from PIL import Image

DEEPSTACK_URL = os.getenv("TEST_DEEPSTACK_URL")
IMAGES_DIR = os.getenv("TEST_IMAGES_DIR")
config = ServerConfig(DEEPSTACK_URL)

def test_detection_file():
    
    detection = Detection(config)

    res = detection.processImage(os.path.join(IMAGES_DIR,"detection.jpg"))
    
    assert len(res) == 3
    
def test_scene_url():
   
    
    detection = Detection(config)

    res = detection.processImage("https://flowergardengirl.co.uk/wp-content/uploads/2017/07/Garden-Design-chelsea-screen-raised-beds-wonderful-planting-artificial-grass-olives-trees.jpg")

    assert len(res) == 3

def test_scene_cv2():

    detection = Detection(config)

    img = cv2.imread(os.path.join(IMAGES_DIR,"detection.jpg"))

    res = detection.processImage(img)

    assert len(res) == 3

def test_scene_pil():

    detection = Detection(config)

    img = Image.open(os.path.join(IMAGES_DIR,"detection.jpg"))

    res = detection.processImage(img)

    assert len(res) == 3

def test_scene_bytes():

    detection = Detection(config)

    img = Image.open(os.path.join(IMAGES_DIR,"detection.jpg"))

    img_data = pilToBytes(img)

    res = detection.processImage(img_data)

    assert len(res) == 3

def test_scene_video():

    detection = Detection(config)

    video = os.path.join(IMAGES_DIR,"video.mp4")

    res = detection.processVideo(video,output="vid.mp4")

    savedVid = cv2.VideoCapture("vid.mp4")

    totalframecount= int(savedVid.get(cv2.CAP_PROP_FRAME_COUNT))

    assert totalframecount == 1193