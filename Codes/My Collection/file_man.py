import os
import re
from music import Music


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
        song_name_no_artist = self.remove_artist_name(raw_name)
        new_name = f"{track} - {song_name_no_artist}"
        return new_name

    def rename_files_in_directory(self):
        """
        Renames all files in the directory
        Use before the songs are organized in their folder
        """
        for file in os.listdir(self.directory):
            if file.endswith(".mp3"):
                old_name = os.path.join(self.directory, file)
                new_name = os.path.join(self.directory, self.rename_file(file))
                os.rename(old_name, new_name)

    def save_file_details_music(self, file_name="index.txt"):
        """
        Saves the contents of the directory to a file
        The name of folder is treated as album name so, use after files are organized
        """
        j = 0
        with open(os.path.join(self.directory, file_name), "w") as f:
            count = 0
            for folder, sub_folders, files in os.walk(self.directory):
                count += 1
                if count == 1:
                    continue
                folder = folder.split("\\")[-1]
                f.writelines(f"Album: " + folder + "\n" + "Songs:" + "\n")
                i = 1
                for fi in files:
                    try:
                        if fi.endswith(".mp3"):
                            fi = ".".join(fi.split(".")[:-1])
                            if "-" in fi:
                                fi = " ".join(fi.split("-")[1:])
                            f.writelines(str(i) + ". " + fi + "\n")
                            i += 1
                            j += 1
                    except:
                        pass
                f.writelines("\n\n")
            f.writelines("\n" + "Total number of songs: " + str(j - 1))
