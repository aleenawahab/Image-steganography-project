import cv2

def extract_image(stego_path, output_path):
    stego = cv2.imread(stego_path)

    extracted = (stego & 0x0F) << 4

    cv2.imwrite(output_path, extracted)
    print("Image extracted successfully!")