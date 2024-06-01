import cv2
import numpy as np
import urllib.request
import requests


def main():
    # url1 = "https://pbs.twimg.com/media/GNItBCnXQAApfuB?format=jpg&name=small"
    # url2 = "https://bafybeidnmoryqmho7qqw32y4mc5icqdtwwokfin7zactq7qbapknlg3s5a.ipfs.cf-ipfs.com/"
    # url2 = "https://i.imgur.com/E7O8FBS.jpeg"
    url1 = "https://images.wallpapersden.com/image/download/4k-a-different-world_bWVqaG6UmZqaraWkpJRmbmdlrWZlbWU.jpg"
    # url2 = "https://wallpapercave.com/wp/n9D8rLR.jpg"
    url2 = "https://i.imgur.com/XZy1f2c.jpeg"
    print(compare_images(url1, url2))


def compare_images(url1: str, url2: str) -> str:
    THRESHOLD = 6.1
    # see if url is a valid image
    if not is_url_image(url1):
        return f"{url1} is not a valid image url."
    elif not is_url_image(url2):
        return f"{url2} is not a valid image url."
    else:
        if url1 == url2:
            return "True"

        req1 = urllib.request.Request(url1, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req1) as url:
            s = url.read()
            arr = np.asarray(bytearray(s), dtype=np.uint8)
            image1 = cv2.imdecode(arr, -1)

        req2 = urllib.request.Request(url2, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req2) as url:
            s = url.read()
            arr = np.asarray(bytearray(s), dtype=np.uint8)
            image2 = cv2.imdecode(arr, -1)

        # see if the resolution is the same
        if image1.shape != image2.shape:
            return "Images are not the same resolution."

        max = cv2.max(image1, image2)
        max[max == 0] = 0.0000001
        difference = cv2.absdiff(image1, image2)
        cv2.imwrite("difference2.png", difference)
        diff_percentage = (np.sum(difference) / np.sum(max)) * 100
        if diff_percentage <= THRESHOLD:
            return "True"
        else:
            return "False"


def is_url_image(url):
    # if url ends with an image extension then it is an image
    if (
        url.endswith(".png")
        or url.endswith(".jpg")
        or url.endswith(".jpeg")
        or url.endswith(".gif")
    ):
        return True
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        mimetype = response.headers["content-type"]
        return mimetype and mimetype.startswith("image")
    return False


if __name__ == "__main__":
    main()
