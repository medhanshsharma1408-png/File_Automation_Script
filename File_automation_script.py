from pathlib import Path
import shutil
    
class File_automation:
    def __init__(self):
        self.source_folder=Path.home()/"Downloads"
        self.imgs=self.source_folder/"Images"
        self.apps=self.source_folder/"Applications"
        self.doc=self.source_folder/"Docs"
        self.ppt=self.source_folder/"PPTs"
        self.web=self.source_folder/"Webpages"
        self.pdf=self.source_folder/"PDFs"
        self.zip=self.source_folder/"Archives"
        self.other=self.source_folder/"Others"
        for folder in [self.imgs, self.apps, self.doc, self.ppt,self.web, self.pdf, self.zip, self.other]:
            folder.mkdir(exist_ok=True)
        
    def Scanning_and_Moving(self):
        for file in self.source_folder.iterdir():
            if file.is_file():
                file_type=file.suffix.lower()
                try: 
                    if file_type in [".jpg", ".png"]:
                        shutil.move(file,self.imgs/file.name)
                        print("File Moved Succesfully.")
                    elif file_type in [".apk",".exe"]:
                        shutil.move(file,self.apps/file.name)
                        print("File Moved Succesfully.")
                    elif file_type in ".pdf":
                        shutil.move(file,self.pdf/file.name)
                        print("File Moved Succesfully.")
                    elif file_type in ".html":
                        shutil.move(file,self.web/file.name)
                        print("File Moved Succesfully.")
                    elif file_type in ".pptx":
                        shutil.move(file,self.ppt/file.name)
                        print("File Moved Succesfully.")
                    elif file_type in ".docx":
                        shutil.move(file,self.doc/file.name)
                        print("File Moved Succesfully.")
                    elif file_type in ".zip":
                        shutil.move(file,self.zip/file.name)
                        print("File Moved Succesfully.")
                    else:
                        shutil.move(file,self.other/file.name)
                        print("File Moved Succesfully.")
                except FileNotFoundError:
                    print("File not found",file.name)
                except PermissionError:
                    print("Locked:",file.name)
                except Exception as e:
                    print("Unexpected error:",e)

g=File_automation()
g.Scanning_and_Moving()

        
