import os
from flexsim_augmentation import generate_flex_dataset

# Step 1: create augmented flexible PCB dataset
generate_flex_dataset("data/deepPCB/images", "data/flexPCB/images")

print("FlexPCB dataset created successfully.")

# Step 2: copy labels (DeepPCB labels work fine)
import shutil

if not os.path.exists("data/flexPCB/labels"):
    os.makedirs("data/flexPCB/labels")

for file in os.listdir("data/deepPCB/labels"):
    src = os.path.join("data/deepPCB/labels", file)
    dst = os.path.join("data/flexPCB/labels", file)
    shutil.copy(src, dst)

print("Labels copied from DeepPCB → FlexPCB dataset.")
