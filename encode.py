import cv2

def hide_image(cover_path, secret_path, output_path):
    cover = cv2.imread(cover_path)
    secret = cv2.imread(secret_path)

    secret = cv2.resize(secret, (cover.shape[1], cover.shape[0]))

    stego = (cover & 0xF0) | (secret >> 4)

    cv2.imwrite(output_path, stego)
    print("Image hidden successfully!")