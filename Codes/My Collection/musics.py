from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import os
import shutil


class Music:
    def __init__(self, directory, strict=True):
        self.directory = directory
        self.strict = strict
        self.albums = set()
        self.albums_list = []
        self.valid_folders = []
        self.num_songs_per_album = {}

    def audio_file(self, name):
        if name.endswith(".mp3"):
            file_path = os.path.join(self.directory, name)
            audio = MP3(file_path, ID3=EasyID3)
        else:
            return None
        return audio

    def get_song_param(self, audio, param):
        if audio:
            if param in audio.keys():
                return audio[param][0]
            else:
                print(f"Only these parameters are available {audio.keys}")
                return None

    def non_strict_album_names(self, strict_album):
        if strict_album:
            return strict_album.split("(")[0].strip()
        else:
            return None

    def get_all_albums(self):
        non_strict_albums = []
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
        special_chars = r"/ \ : * ? < > |".split()
        for char in special_chars:
            if char in old_name:
                old_name.replace(char, "")
        return old_name

    def get_songs_per_album(self):
        if not self.albums:
            self.get_all_albums()

        for album in self.albums:
            if album is None:
                self.num_songs_per_album["others"] = self.albums_list.count(album)
            else:
                self.num_songs_per_album[album] = self.albums_list.count(album)

    def get_valid_folders(self, min_num=3):
        if not self.num_songs_per_album:
            self.get_songs_per_album()

        for key, value in self.num_songs_per_album.items():
            if value > min_num:
                self.valid_folders.append(self.clean_names(key))

    def move_files(self, min_num=3):
        if not self.valid_folders:
            self.get_valid_folders(min_num)

        for folder in self.valid_folders:
            os.makedirs(os.path.join(self.directory, folder), exist_ok=True)
            for file in os.listdir(self.directory):
                album = self.get_song_param(self.audio_file(file), "album")
                if album:
                    if self.strict:
                        if album == folder:
                            shutil.move(
                                os.path.join(self.directory, file),
                                os.path.join(self.directory, folder),
                            )
                    else:
                        if folder in album:
                            shutil.move(
                                os.path.join(self.directory, file),
                                os.path.join(self.directory, folder),
                            )
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
            for file in os.listdir(self.directory):
                if file.endswith(".mp3"):
                    shutil.move(
                        os.path.join(self.directory, file),
                        os.path.join(self.directory, folder_name),
                    )
        else:
            print("Aborted! \nGood choice! ):")
