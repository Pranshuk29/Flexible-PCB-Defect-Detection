import subprocess
import sys

image_path = sys.argv[1]

cmd = [
    "python", "yolov5/detect.py",
    "--weights", "results/after_flex/flexPCB/weights/best.pt",
    "--img", "640",
    "--source", image_path,
    "--project", "results/inference",
    "--name", "flex_test"
]

subprocess.run(cmd)
