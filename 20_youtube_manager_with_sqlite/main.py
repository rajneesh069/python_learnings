import sqlite3

conn = sqlite3.connect("youtube_manager.db")
cursor = conn.cursor()


def list_videos():
    cursor.execute(
        """
    SELECT * FROM videos
"""
    )
    print("*" * 15)
    for row in cursor.fetchall():
        print(f"Video ID: {row[0]}")
        print(f"Name: {row[1]}")
        print(f"Duration: {row[2]}")
        print("\n")
    print("*" * 15)
    conn.commit()


def add_a_video(name, duration):
    cursor.execute(
        """
    INSERT INTO videos (name, duration) 
    VALUES (?, ?)
""",
        (name, duration),
    )
    conn.commit()


def update_a_video(video_id, new_name, new_duration):
    list_videos()
    print("\n")
    cursor.execute(
        """
    UPDATE videos
    SET name= ?, duration = ?
    WHERE id = ?
""",
        (
            new_name,
            new_duration,
            video_id,
        ),
    )
    conn.commit()


def delete_video(video_id):
    list_videos()
    print("\n")
    cursor.execute(
        """
    DELETE FROM videos
    WHERE id = ?
""",
        (video_id,),
    )


def main():
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        duration TEXT NOT NULL
    )
    """
    )
    print("Youtube Manager App")

    while True:
        print(f"1. List all videos")
        print(f"2. Add a video")
        print(f"3. Update a video")
        print(f"4. Delete a video")
        print(f"5. Exit the app")

        option = input("Please select an option: ")

        match option:
            case "1":
                list_videos()
            case "2":
                name = input("Please enter the name of the video: ")
                duration = input("Please enter the duration of the video: ")
                add_a_video(name, duration)
            case "3":
                list_videos()
                print("\n")
                video_id = input("Please enter the ID of the video to be updated: ")
                new_name = input("Please enter the name of the video: ")
                new_duration = input("Please enter the duration of the video: ")
                update_a_video(video_id, new_name, new_duration)
            case "4":
                list_videos()
                print("\n")
                video_id = input("Please enter the ID of the video to be deleted: ")
                delete_video(video_id)
            case "5":
                break
            case _:
                print(f"Invalid Input")

    cursor.close()
    conn.close()
    return


if __name__ == "__main__":
    main()
