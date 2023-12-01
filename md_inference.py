from cv_algorithm import match_images
import cv2


def inference(n_matches):
    # Input image paths
    img_path1 = '/Users/andy/Downloads/T36UYA_20190805T083601_B07.jp2'
    img_path2 = '/Users/andy/Downloads/T36UYA_20190805T083601_B06.jp2'

    result = match_images(img_path1, img_path2, n_matches=n_matches)

    # Display the result image
    cv2.imshow('Matching Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    inference(20)
