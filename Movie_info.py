class Movie_information():

        def __init__(self):
            self._movienames = ""
            self._youtubekey = ""
            self._posterpath = ""

        @property
        def movienames(self):
            print("in the name getter: ")
            return self._movienames

        @movienames.setter
        def movienames(self, name):
            print("in the name setter: ")
            self._movienames = name + self._movienames

        @property
        def youtubekey(self):
            print("in the key getter: ")
            return self._youtubekey

        @youtubekey.setter
        def youtubekey(self, key):
            print("in the key setter: ")
            self._youtubekey = key + self._youtubekey

        @property
        def posterpath(self):
            print("in the path getter: ")
            return self._posterpath

        @posterpath.setter
        def posterpath(self, path):
            print("in the path setter: ")
            self._posterpath = path + self._posterpath

        # def __init__(self,name,key,path):
        #     self.movienames = name
        #     self.posterpath = path
        #     self.youtubekey = key

        # def __repr__(self):
        #     return repr(self.data)
