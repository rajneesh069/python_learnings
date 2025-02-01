import json

file_path = "./youtube_list.txt"


def load_data():
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []


def save_data(videos):
    with open(file_path, "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("*" * 50)
    print(f"List of all videos:")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video["name"]} of {video["duration"]}")
    print("*" * 50)


def add_videos(videos: list):
    name = input("Enter the name of the video: ")
    duration = input("Enter the length/duration of the video: ")
    videos.append({"name": name, "duration": duration})
    save_data(videos)


def update_video(videos):
    list_all_videos(videos)
    idx = int(input("Enter the video number to update: "))
    if 1 <= idx <= len(videos):
        name = input("Enter the new video name: ")
        duration = input("Enter the new video duration: ")
        videos[idx - 1] = {"name": name, "duration": duration}
        save_data(videos)
    else:
        print("Please select a valid video number.")


def delete_video(videos):
    list_all_videos(videos)
    idx = int(input("Enter the video number to delete"))
    if 1 <= idx <= len(videos):
        del videos[idx - 1]
        save_data(videos)
    else:
        print("Please select a valid video number.")


def main():
    videos = load_data()
    print(f"\nYoutube Manager App")
    while True:
        print("-----------------------------")
        print(f"1. List the favourite videos")
        print(f"2. Add a youtube video")
        print(f"3. Update a youtube video detail")
        print(f"4. Delete a youtube video")
        print(f"5. Exit the app")
        print("----------------------------")
        choice = input("Please select an option: ")
        print("----------------------------")
        print("\n")
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print(f"Invalid Input!")


if __name__ == "__main__":
    main()
