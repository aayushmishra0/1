import dropbox
import os 
from dropbox.files import WriteMode 
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        for root, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BJZpJqHzxswDCbJ4NqFtiPAJPOp2B7Or572zVCLcwuc55uH8_4k7LfrfcQynZBHTJdKOmt_f-Y0Ch1GnpuNafPhVuHaS97jeR64MMM_T1QjymFrkLvKC4JKAXV142HZoCFNfxeQz6Wld'
    transferData = TransferData(access_token)

    file_from = input('Enter the file path to transfer:-')
    file_to = input('Enter the full path to upload to dropbox:-')  # The full path to upload the file to, including the file name   

    # API v2
    transferData.upload_file(file_from, file_to)
    print('File has been moved')
main()