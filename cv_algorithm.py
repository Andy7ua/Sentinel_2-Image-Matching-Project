import cv2


def match_images(img_path1, img_path2, n_matches=20):
    # Set visualization parameters
    match_color = (0, 255, 0)
    line_thickness = 3

    # Read images
    img1 = cv2.imread(img_path1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img_path2, cv2.IMREAD_GRAYSCALE)

    # Resize the larger image to the dimensions of the smaller image
    min_height = min(img1.shape[0], img2.shape[0])
    min_width = min(img1.shape[1], img2.shape[1])

    img1 = cv2.resize(img1, (min_width, min_height))
    img2 = cv2.resize(img2, (min_width, min_height))

    # Detect keypoints and compute descriptors
    orb = cv2.ORB_create()
    keypoint1, descriptor1 = orb.detectAndCompute(img1, None)
    keypoint2, descriptor2 = orb.detectAndCompute(img2, None)

    # Match keypoints
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptor1, descriptor2)
    matches = sorted(matches, key=lambda x: x.distance)  # Sort matches based on distances

    # Draw matches
    result_image = cv2.drawMatches(
        img1, keypoint1, img2, keypoint2,
        matches[:n_matches], None,
        matchColor=match_color,
        singlePointColor=(255, 0, 0),
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS,
        matchesThickness=line_thickness
    )

    return result_image


if __name__ == "__main__":
    img_path1 = '/Users/andy/Downloads/T36UYA_20190805T083601_B07.jp2'
    img_path2 = '/Users/andy/Downloads/T36UYA_20190805T083601_B06.jp2'

    output_filename = 'output_matches.jpg'  # Output filename for the matches image

    # Perform matching
    img_matches = match_images(img_path1, img_path2)

    # Save the result to an image file outside the function
    cv2.imwrite(output_filename, img_matches)
