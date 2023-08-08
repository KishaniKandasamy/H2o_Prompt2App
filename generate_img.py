import pandas as pd
import numpy as np
import requests
import random
import json

query_list = ["Agriculture",
              "Construction",
              "Consumer Goods",
              "Education",
              "Energy",
              "Financial Services",
              "Food and Beverage",
              "Healthcare",
              "Information Technology",
              "Insurance",
              "Manufacturing",
              "Media",
              "Pharmaceuticals",
              "Retail",
              "Telecommunications",
              "Others"
              ]
pexels_key = "zI8lQXkhZ4ejxJeJyj7nwblNjtZUzO5N9eTkSHmNhIEo30H29X8NlQLn"


# fetch images
def search_pexels(query, pexels_key):
    url = f"https://api.pexels.com/v1/search?query={query}&per_page=10&page=1"
    headers = {"Authorization": pexels_key}
    response = requests.get(url, headers=headers)

    images = []
    if response.status_code == 200:
        data = json.loads(response.text)
        photos = data["photos"]
        for photo in photos:
            photo_url = photo["src"]["large"]
            images.append(photo_url)

    else:
        print("Error occurred:", response.text)
    return images


def create_image_dict(query_list):
    img_dict = {}
    for query in query_list:
        images = search_pexels(query, pexels_key)
        img_dict = {**img_dict, query: images}

    return img_dict


final_dict = create_image_dict(query_list)
print(f"final_dict..{final_dict}")

with open("images.json", "w") as file:
    json.dump(final_dict, file)
