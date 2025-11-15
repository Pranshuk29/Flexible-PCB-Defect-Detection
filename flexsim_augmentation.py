import cv2
import numpy as np
import os
from albumentations import (
    Compose, RandomBrightnessContrast, HueSaturationValue,
    MotionBlur, GaussNoise, ElasticTransform, Perspective,
    RandomShadow, RandomGamma
)
from tqdm import tqdm

def flex_augment(image):
    aug = Compose([
        Perspective(scale=(0.05, 0.10), p=0.8),  # bending → looks like curved FPCB
        ElasticTransform(alpha=50, sigma=8, alpha_affine=5, p=0.7), # mimics flex wrinkles
        RandomBrightnessContrast(p=0.7),
        RandomGamma(p=0.5),
        RandomShadow(num_shadows_upper=2, p=0.5),
        MotionBlur(p=0.3),
        HueSaturationValue(hue_shift_limit=10, sat_shift_limit=20, val_shift_limit=15, p=0.6)
    ])

    augmented = aug(image=image)
    return augmented["image"]


def generate_flex_dataset(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    images = [f for f in os.listdir(input_dir) if f.endswith('.png') or f.endswith('.jpg')]

    print(f"[INFO] Generating flexible-PCB dataset…")
    for img_name in tqdm(images):
        img_path = os.path.join(input_dir, img_name)
        img = cv2.imread(img_path)

        out_img = flex_augment(img)
        cv2.imwrite(os.path.join(output_dir, img_name), out_img)

    print("[DONE] Flexible dataset created at:", output_dir)


if __name__ == "__main__":
    generate_flex_dataset("data/deepPCB/images", "data/flexPCB/images")
