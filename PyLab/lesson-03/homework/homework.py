from argparse import ArgumentParser


def read_file_v1(file_path: str) -> str:
    with open(file_path, "r") as file:
        data = file.read()
    # After the "with" block, the file is automatically closed
    return data


def read_file_v2(file_path: str) -> str:
    # Another way to read a file
    file = open(file_path, "r")
    data = file.read()
    # You should close the file manually here
    file.close()
    return data


def convert_time(time: str) -> int:
    # Assume the time is in the format "hh:mm:ss"
    hour, minute, second = time.split(":")
    return int(hour) * 3600 + int(minute) * 60 + int(second)


def main(args: ArgumentParser):
    input_file_path: str = args.input
    data = read_file_v1(input_file_path)
    # Now data is a string contains:
    # "---\n     Fly Me To The Moon\n---\n..."
    # Split the string by "---"
    str_list = data.split("---")

    # Remove space, newline and empty string from each string
    new_list: list[str] = []
    # in the list
    for s in str_list:
        s = s.strip()
        if s != "":
            new_list.append(s)

    print(f"Now there are {len(new_list)} elements in the list")

    song_name = f" {new_list[0]} "
    singer = new_list[1]
    duration = str(convert_time(new_list[2])) + " seconds"
    lyrics = new_list[3]

    # Split lyrics with '\n'
    lyrics_list = lyrics.split("\n")

    # Remove empty string from the list
    max_length = 0
    new_lyrics_list: list[str] = []
    for l in lyrics_list:
        l = l.strip()
        if l != "":
            new_lyrics_list.append(l)
            max_length = max(max_length, len(l))

    print(f"The longest line has {max_length} characters")

    # Final output, each line should be max_length and center aligned
    song_name = song_name.center(max_length, "#")
    singer = singer.center(max_length)
    duration = duration.center(max_length)
    centered_lyrics: list[str] = []
    for l in new_lyrics_list:
        centered_lyrics.append(l.center(max_length))

    print(song_name)
    print(singer)
    print(duration)
    for l in centered_lyrics:
        print(l)


if __name__ == "__main__":
    argparser = ArgumentParser()
    argparser.add_argument("--input", type=str, help="input file")
    args = argparser.parse_args()
    main(args)
