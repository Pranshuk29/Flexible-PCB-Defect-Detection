import os
import subprocess

print("Starting YOLOv5 training on FlexPCB dataset…")

cmd = [
    "python", "yolov5/train.py",
    "--img", "640",
    "--batch", "8",
    "--epochs", "80",
    "--data", "data/data.yaml",
    "--weights", "yolov5s.pt",
    "--project", "results/after_flex",
    "--name", "flexPCB"
]

subprocess.run(cmd)
