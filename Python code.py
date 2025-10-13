import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# ---------- ROI Detection (intensity-based) ----------
def detect_roi(image, thresh_factor=0.5):
    mean_intensity = np.mean(image)
    roi_mask = (image > mean_intensity * (1 + thresh_factor)).astype(np.uint8)
    roi_mask = cv2.medianBlur(roi_mask, 9)
    return roi_mask

# ---------- Uniform Partition ----------
def uniform_partition(image, n_blocks):
    H, W = image.shape[:2]
    num_blocks_side = int(np.sqrt(n_blocks))
    w = W // num_blocks_side
    h = H // num_blocks_side
    regions = [(x * w, y * h, w, h)
               for y in range(num_blocks_side)
               for x in range(num_blocks_side)]
    return regions

# ---------- ROI-preserving Compact Encoding (global ROI enhancement) ----------
def compact_encode_roi_smooth(image, regions, roi_mask):
    # Step 1: Enhance ROI globally
    clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(8, 8))
    roi_enhanced = clahe.apply(image)

    sharpen_kernel = np.array([
        [0, -0.2, 0],
        [-0.2, 1.8, -0.2],
        [0, -0.2, 0]
    ])
    roi_enhanced = cv2.filter2D(roi_enhanced, -1, sharpen_kernel)

    # Blend ROI with original image (inside ROI mask only)
    roi_blended = np.where(roi_mask == 1,
                           cv2.addWeighted(image, 0.4, roi_enhanced, 0.6, 0),
                           image)

    # Step 2: Compress RONI per block
    encoded = roi_blended.copy()
    for (x, y, w, h) in regions:
        region = roi_blended[y:y+h, x:x+w]
        roi_ratio = np.mean(roi_mask[y:y+h, x:x+w])
        if roi_ratio <= 0.05:  # non-ROI region
            blurred = cv2.GaussianBlur(region, (9, 9), 0)
            region_encoded = np.uint8(np.round(blurred / 32) * 32)
            encoded[y:y+h, x:x+w] = region_encoded

    return encoded

# ---------- Main Folder Processing ----------
if __name__ == "__main__":
    input_folder = r"C:\Users\hetvi\Desktop\eceproject\yes"  
    output_folder = r"C:\Users\hetvi\Desktop\eceproject\output"

    C = 100  # number of partitions

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")):
            continue

        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            print(f"⚠️ Skipping unreadable image: {filename}")
            continue

        print(f"\nProcessing {filename} ...")

        # ROI detection and processing
        roi_mask = detect_roi(img, thresh_factor=0.3)
        regions = uniform_partition(img, C)
        lossy_encoded = compact_encode_roi_smooth(img, regions, roi_mask)

        # Save compressed output
        output_path = os.path.join(output_folder, f"encoded_{filename}")
        cv2.imwrite(output_path, lossy_encoded, [int(cv2.IMWRITE_JPEG_QUALITY), 20])

        # Print compression info
        original_size = os.path.getsize(img_path) / 1024
        compressed_size = os.path.getsize(output_path) / 1024
        compression_ratio = original_size / compressed_size if compressed_size else 0

        print(f"✅ Saved: {output_path}")
        print(f"   Original Size: {original_size:.2f} KB")
        print(f"   Compressed Size: {compressed_size:.2f} KB")
        print(f"   Compression Ratio: {compression_ratio:.2f}")

    print("\n🎉 All images processed successfully! ROI preserved and enhanced.")
