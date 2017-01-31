import numpy as np
import imutils
import cv2

def detect_and_describe(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    descriptor = cv2.xfeatures2d.SIFT_create()
    (kps, features) = descriptor.detectAndCompute(image, None)
    kps = np.float32([kp.pt for kp in kps])
    return (kps, features)

def match_keypoints(kpsA, kpsB, featuresA, featuresB, ratio, reproj_tresh):
    matcher = cv2.DescriptorMatcher_create("BruteForce")
    raw_matches = matcher.knnMatch(featuresA, featuresB, 2)
    matches = []

    for raw_match in raw_matches:
        if len(raw_match) == 2 and raw_match[0].distance < raw_match[1].distance * ratio:
            matches.append((raw_match[0].trainIdx, raw_match[0].queryIdx))

    if len(matches) > 4:
        ptsA = np.float32([kpsA[i] for (_, i) in matches])
        ptsB = np.float32([kpsB[i] for (i, _) in matches])
        (H, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, reproj_tresh)
        return (matches, H, status)

    return None

def draw_matches(imageA, imageB, kpsA, kpsB, matches, status):
    (hA, wA) = imageA.shape[:2]
    (hB, wB) = imageB.shape[:2]
    vis = np.zeros((max(hA, hB), wA + wB, 3), dtype="uint8")
    vis[0:hA, 0:wA] = imageA
    vis[0:hB, wA:] = imageB

    for ((trainIdx, queryIdx), s) in zip(matches, status):
        if s == 1:
            ptA = (int(kpsA[queryIdx][0]), int(kpsA[queryIdx][1]))
            ptB = (int(kpsB[trainIdx][0]) + wA, int(kpsB[trainIdx][1]))
            cv2.line(vis, ptA, ptB, (0, 255, 0), 1)

    return vis

def stitch(images, ratio=0.75, reproj_tresh=4.0, showMatches=False):
    imageB, imageA = images
    (kpsA, featuresA) = detect_and_describe(imageA)
    (kpsB, featuresB) = detect_and_describe(imageB)

    matching = match_keypoints(kpsA, kpsB, featuresA, featuresB, ratio, reproj_tresh)
    if matching is None:
        return None

    (matches, H, status) = matching
    result = cv2.warpPerspective(imageA, H, (imageA.shape[1] + imageB.shape[1], imageA.shape[0]))
    result[0:imageB.shape[0], 0:imageB.shape[1]] = imageB
    if showMatches:
        vis = draw_matches(imageA, imageB, kpsA, kpsB, matches, status)
        return (result, vis)
    return vis

def main():
    imageA = cv2.imread("img1.jpg")
    imageB = cv2.imread("img2.jpg")
    (result, vis) = stitch([imageA, imageB], showMatches=True)
    cv2.imwrite("vis.jpg", vis)
    cv2.imwrite("result.jpg", result)

if __name__ == "__main__":
    main()
