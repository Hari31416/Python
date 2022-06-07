from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import os
import shutil
import re
import sys
import datetime
import math


class Music:
    """
    A class with methods to move music file using album name as folder name
    To use this, instantiate the class with `directory` and `strict` as arguments.

    `directory` is the directory where the music files are located.

    `strict` is a boolean value. If True, the folder name will strictly match the album name.
    If `False`, the folder name will be the album name upto any opening parenthesis.

    After instantiating, call `move_files` with a argument `min_num` which is the minimum number of songs
    an album must have to consider it as a valid folder.

    _____________________________________________________________________________________
    Best Way to use the class is first instantiate Music with `strict` as True, then calling `move_files`.
    Then change `strict` to False and call `move_all` to move all the files to a single folder.

    Any remaining files will be placed in a folder called `others` by calling `move_all`.
    """

    def __init__(self, directory, strict=True):
        """
        directory: the directory where the music files are located
        strict: a boolean value.
        album_name: the set of album names
        albums_list: a list of album names(len will be equal to number of songs)
        num_songs_per_album: a dictionary with album name as key and number of songs as value
        valid_folders: a list of valid folders which will be used to create folders
        """
        self.directory = directory
        self.strict = strict
        self.albums = set()
        self.albums_list = []
        self.valid_folders = []
        self.num_songs_per_album = {}

    def audio_file(self, name):
        """
        Retuns the audio file object using mutagen library
        """
        if name.endswith(".mp3"):
            file_path = os.path.join(self.directory, name)
            audio = MP3(file_path, ID3=EasyID3)
        else:
            return None
        return audio

    def get_song_param(self, audio, param):
        """
        returns the value of the parameter `param` from the audio file object `audio`.
        `param` can be any of the following:[album, name, artist, title]
        """
        if audio:
            if param in audio.keys():
                return audio[param][0]
            else:
                print(f"Only these parameters are available {audio.keys}")
                return None

    def non_strict_album_names(self, strict_album):
        """
        return the non-strict album name
        """
        if strict_album:
            return strict_album.split("(")[0].strip()
        else:
            return None

    def get_all_albums(self):
        """
        Gets all the album names from the directory
        """
        for file in os.listdir(self.directory):
            song = self.audio_file(file)
            album = self.get_song_param(song, "album")
            if self.strict:
                self.albums_list.append(album)
            else:
                album = self.non_strict_album_names(album)
                self.albums_list.append(album)
        self.albums = set(self.albums_list)
        return self.albums_list

    def clean_names(self, old_name):
        """
        clean names so that the folder can be create successfully
        """
        special_chars = r"/ \ : * ? < > |".split()
        for char in special_chars:
            if char in old_name:
                old_name.replace(char, "")
        return old_name

    def get_songs_per_album(self):
        """
        gets the `num_songs_per_album` dictionary
        """
        if not self.albums:
            self.get_all_albums()

        for album in self.albums:
            if album is None:
                self.num_songs_per_album["others"] = self.albums_list.count(album)
            else:
                self.num_songs_per_album[album] = self.albums_list.count(album)

    def get_valid_folders(self, min_num=3):
        """
        gets the valid folders which will be used to create folders
        uses the `min_num` to decide which folders are valid
        """
        if not self.num_songs_per_album:
            self.get_songs_per_album()

        for key, value in self.num_songs_per_album.items():
            if value > min_num:
                self.valid_folders.append(self.clean_names(key))

    def move_files(self, min_num=3, by="album"):
        """
        The method which does all the work!
        """
        if not self.valid_folders:
            self.get_valid_folders(min_num)

        for folder in self.valid_folders:
            try:
                os.makedirs(os.path.join(self.directory, folder), exist_ok=True)
            except NotADirectoryError:
                print(f"{folder} is not a valid folder name")
                continue
            for file in os.listdir(self.directory):
                album = self.get_song_param(self.audio_file(file), by)
                if album:
                    if self.strict:
                        if album == folder:
                            shutil.move(
                                os.path.join(self.directory, file),
                                os.path.join(self.directory, folder),
                            )
                    else:
                        if folder in album:
                            try:
                                shutil.move(
                                    os.path.join(self.directory, file),
                                    os.path.join(self.directory, folder),
                                )
                            except BaseException:
                                print(f"{file} is already in {folder}")
                                continue
                else:
                    pass

    def move_all(self, folder_name="others"):
        """
        Use Only When all the other files are placed in their folders
        """
        confirm = input(
            "Are you sure you want to move all the files to {}? (y/n)".format(
                folder_name
            )
        )
        if confirm[0].lower() == "y":
            os.makedirs(os.path.join(self.directory, folder_name), exist_ok=True)
            for file in os.listdir(self.directory):
                if file.endswith(".mp3"):
                    shutil.move(
                        os.path.join(self.directory, file),
                        os.path.join(self.directory, folder_name),
                    )
        else:
            print("Aborted! \nGood choice! ):")


class FileManager(Music):
    def __init__(self, directory):
        super().__init__(directory)
        self.directory = directory

    def remove_artist_name(self, raw_name):
        """
        Removes the artist name from the song name
        """
        try:
            pattern = r"-"
            song_name = raw_name[1 + re.search(pattern, raw_name).start() :]
            song_name = song_name.strip()
        except:
            song_name = raw_name
        return song_name

    def rename_file(self, raw_name):
        """
        Renames a song by removing the artist name and appending track number
        """
        audio = self.audio_file(raw_name)
        track = self.get_song_param(audio, "tracknumber")
        try:
            song_name_no_artist = self.remove_artist_name(raw_name)
            new_name = f"{track} - {song_name_no_artist}"
            return new_name
        except:
            return f"{track} - {raw_name}"

    def rename_files_in_directory(self):
        """
        Renames all files in the directory
        Use before the songs are organized in their folder
        """
        for file in os.listdir(self.directory):
            if file.endswith(".mp3"):
                old_name = os.path.join(self.directory, file)
                try:
                    new_name = os.path.join(self.directory, self.rename_file(file))
                    os.rename(old_name, new_name)
                except:
                    print("Cannot rename this file as it already exists: ", file)
                    pass

    def save_file_details_music(self, file_name="index.txt", encoding="utf-8"):
        """
        Saves the contents of the directory to a file
        The name of folder is treated as album name so, use after files are organized
        """
        j = 0
        file_size = 0
        today = datetime.date.today().strftime("%d-%m-%Y")
        file_name = f"{today}_{file_name}"
        with open(os.path.join(self.directory, file_name), "w") as f:
            count = 0
            for folder, sub_folders, files in os.walk(self.directory):
                count += 1
                if count == 1:
                    continue
                folder_name = folder.split("\\")[-1]
                f.writelines(f"Album: " + folder_name + "\n" + "Songs:" + "\n")
                i = 1
                for fi in files:
                    try:
                        if fi.endswith(".mp3"):
                            file = os.path.join(folder, fi)
                            file_size += os.path.getsize(file) / (1024 * 1024)
                            fi = ".".join(fi.split(".")[:-1])
                            if "-" in fi:
                                fi = " ".join(fi.split("-")[1:])
                            f.writelines("\t" + str(i) + ". " + fi + "\n")
                            i += 1
                            j += 1
                    except:
                        pass
                f.writelines("\n\n")
            f.writelines("\n" + "Total number of songs: " + str(j - 1))
            f.writelines(
                "\n" + "Total size of songs: " + str(math.floor(file_size)) + " MB"
            )


def main(directory):
    """
    The main function
    """
    just_file_details = input("Do you want to just get the file details? (y/n)")
    if just_file_details[0].lower() == "y":
        fm = FileManager(directory)
        fm.save_file_details_music()
        print("DONE!!!")
        return None

    print("Initializing...")
    f = FileManager(directory)
    m = Music(directory, strict=True)

    # Rename Files
    rename_ask = input("Want to rename the files? (y/n)")
    if rename_ask[0].lower() == "y":
        print("Renaming files...")
        f.rename_files_in_directory()

    print("Organizing files... Step 1/3\nUsing strict mode")
    # Move file usings strict = True
    by_artist_name = input("Do you want to organize by artist name? (y/n)")
    if by_artist_name[0].lower() == "y":
        by = "artist"
    else:
        by = "album"

    print("Organizing files... Step 2/3\nUsing non-strict mode")
    # Move file usings strict = False
    m = Music(directory, strict=False)
    m.move_files(min_num=3, by=by)

    print("Organizing files... Step 2/3\n Using non-strict mode")
    # Using strict = False
    m = Music(directory, strict=False)

    # Even 2 songs in one album gets their seperate folders
    m.move_files(1, by=by)

    print("Organizing files... Step 3/3\nMoving all the files to 'others'")
    # Finally, move the files
    m.move_all()

    print("Saving file details...")
    # And get the details of the files
    f.save_file_details_music()
    print("DONE!!!")


if __name__ == "__main__":
    if sys.argv:
        main(sys.argv[1])
    else:
        print("Please provide a directory")
