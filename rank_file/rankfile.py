import os
import sys
import re

class Summary:
    def __init__(self, rank_path:str = None, summary_file:str = "SUMMARY.md"):
        self.rank_path = self.__get_rank_path(rank_path)
        self.summary_file = self.rank_path + "/" + summary_file
        self.cur_dir_name = os.path.split(os.getcwd())[1]
        self.summary = open(self.summary_file, "w", encoding="utf-8")
        self.special_file = "LICENSE README.md book.json" + summary_file
    
    def __del__(self):
        self.summary.close()
    
    def __get_rank_path(self, rank_dir):
        if rank_dir and os.path.isdir(rank_dir):
            return rank_dir

        expect_argc = 2
        if len(sys.argv) != expect_argc:
            print("argc real[%d] != expect[%d]" % (len(sys.argv), expect_argc))
            return None
    
        rank_path = sys.argv[1]
        if not os.path.isdir(rank_path):
            print(rank_path, "is not valid path")
            return None
        
        return rank_path
        
    def rank_book_name(self, book_name = "young book"):
        book_title = self.get_title(1, book_name)
        self.write_text(book_title)
    
    def rank_overview(self, filename:str = "README.md"):
        if not isinstance(filename, str):
            return
        
        overview_file = self.rank_path + "/" + filename
        if not os.path.isfile(overview_file):
            print(overview_file, "is not exist!")
            return

        text = "概述"
        link = filename
        text_link = self.get_text_link(text, link)
        overview = self.get_list(0, text_link)
        self.write_text(overview)
    
    def rank_files(self):
        self.rank_book_name()
        self.rank_overview()
        self.rank_docs(self.rank_path)

    def rank_docs(self, path, level = 0):
        files = os.listdir(path)
        files.sort()
        for file in files:
            if file in self.special_file:
                continue

            file_path = path + "/" + file

            if os.path.isdir(file_path):
                if level == 0:
                    title_level = level + 2
                    content = self.get_title(title_level, file)
                else:
                    content = self.get_list(level, file)
                self.write_text(content)
                self.rank_docs(file_path, level + 1)
            else:
               text = self.extract_text(file)
               link = self.extract_link(file_path)
               text_link = self.get_text_link(text, link)
               content = self.get_list(level, text_link)
               self.write_text(content)

    def extract_text(self, filename):
        text = filename.split(".")[0]
        if re.match("[0-9]._", text):
            text = text.split("_")[1]
        
        return text
    
    def extract_link(self, file_path):
        link = file_path.split(self.rank_path + "/")[1]
        return link
    
    def get_text_link(self, text:str, link:str):
        return "[" + text + "]" + "(" + link + ")"
    
    def get_title(self, level:int, text:str):
        return "\n" + "#" * level + " " + text + "\n"
    
    def get_list(self, level:int, text:str):
        table_space = 4
        if level > 0:
            level -= 1
        return " " * table_space * level + "* " + text 
    
    def write_text(self, text):
        self.summary.write((text + "\n"))
    
    

if __name__ == "__main__":
    summary = Summary()
    summary.rank_files()
