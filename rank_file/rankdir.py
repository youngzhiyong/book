import os
import rankfile

class Rank:
    def __init__(self, root_path = "../gitbook"):
        self.root_path = root_path
    
    def rank(self):
        if not os.path.isdir(self.root_path):
            print(self.root_path, "is not valid rank dir path")
            return
        
        books = os.listdir(self.root_path)
        books.append(self.root_path)
        for book in books:
            book_path = self.root_path + "/" + book
            if not os.path.isdir(book_path):
                continue

            summary = rankfile.Summary(book_path)
            summary.rank_files()

if __name__ == "__main__":
    rank = Rank()
    rank.rank()