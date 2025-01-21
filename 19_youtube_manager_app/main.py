import json

file_path = "./19_youtube_manager_app/youtube_list.txt"


def load_data():
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            print(f"data:{data}")
            return data
    except FileNotFoundError:
        return []


def save_data():
    with open(file_path, "w") as file:
        json.dump()


def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. ")


def add_videos(videos: list):
    name = input("Enter the name of the video: ")
    length = input("Enter the length of the video: ")
    videos.append({"name": name, "time": length})


def update_video(videos):
    pass


def delete_video(videos):
    pass


def main():
    videos = []
    while True:
        print(f"Youtube Manager App")
        print(f"1. List the favourite videos")
        print(f"2. Add youtube video(s)")
        print(f"3. Update a youtube video detail")
        print(f"4. Delete a youtube video")
        print(f"5. Exit the app")

        choice = input("Please select an option:")

        match choice:
            case "1":
                list_all_videos(video)
            case "2":
                add_videos(video)
            case "3":
                update_video(video)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print(f"Invalid Input!")


if __name__ == "__main__":
    main()
