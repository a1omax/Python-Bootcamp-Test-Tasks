import os.path

from TikTokApi import TikTokApi
from moviepy.editor import *
from moviepy.editor import VideoFileClip


BASE_DIR = os.path.dirname(__file__)
SAVE_DIR = "home/user/"


def convert_to_gif(url: str, name: str, **kwargs) -> str:
    """
    url — Takes valid of tiktok video that strats with `https://www.tiktok.com/`,
    name — name of future file,
    optional — path
    Downloads it as mp4 and converts it into a gif file.
    Returns a path of saved gif
    """

    path = kwargs.pop("path", os.path.join(BASE_DIR, SAVE_DIR).replace('\\', '/'))

    if not os.path.exists(path):
        os.makedirs(path)
    name_with_replaced_gaps = name.replace(" ", "-")
    file_path = os.path.join(path, name_with_replaced_gaps)

    mp4_path = path + "temp.mp4"

    list_file = os.listdir(path)
    list_same_named_files = list(filter(lambda filename: filename.startswith(name_with_replaced_gaps), list_file))
    if list_same_named_files:
        last_file_name = sorted(list_same_named_files)[-1]
        index = int(last_file_name.split("-")[-1].replace('.gif', ""))
        index += 1
    else:
        index = 1

    gif_path = f"{file_path}-{index}.gif"

    try:
        with TikTokApi() as api:

            video = api.video(url=url)

            video_data = video.bytes()

            with open(mp4_path, "wb") as f:

                f.write(video_data)

            video_clip = VideoFileClip(mp4_path, audio=False)
            video_clip.write_gif(gif_path)

            os.remove(mp4_path)
    except Exception as e:
        print(e, "\nReturning gif_path without created file")

    return gif_path


if __name__ == "__main__":
    EXAMPLE_URL = "https://www.tiktok.com/@acatcalledcartier/video/7085346217395244289?is_copy_url=1&is_from_webapp=v1&q=kiiten&t=1659365556501"
    path_to_gif = convert_to_gif(EXAMPLE_URL, "TikTok example")

    print(f"{path_to_gif}")
