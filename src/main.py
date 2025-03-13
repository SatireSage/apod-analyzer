import logging
import os

import requests
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
)

if os.path.exists(".env"):
    load_dotenv()


def main():
    """
    Fetch and download NASA's Astronomy Picture of the Day (APOD).

    This function retrieves the APOD image from the NASA API using an API key stored
    in an environment variable. If an image URL is found, the image is downloaded
    and saved as 'apod/apod.jpg'.

    Raises:
        ValueError: Can not proceed without API key.

    Returns:
        int: 0 if the program runs successfully, non-zero for errors.
    """
    API_KEY = os.getenv("NASA_API_KEY")
    if not API_KEY:
        raise ValueError("NASA_API_KEY is not set!")
    URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

    response = requests.get(URL)
    data = response.json()
    image_url = data.get("url")
    title = data.get("title")

    if image_url:
        os.makedirs("apod", exist_ok=True)

        img_data = requests.get(image_url).content
        with open(os.path.join("apod", "apod.jpg"), "wb") as handler:
            handler.write(img_data)
        logging.info(f"Downloaded: {title} as 'apod/apod.jpg'")
    else:
        logging.warning("No image available in the response.")

    return 0


if __name__ == "__main__":
    main()
