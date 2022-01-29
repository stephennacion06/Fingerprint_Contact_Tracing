import pyrebase

config = {
    "apiKey": "AIzaSyBqlCGdqvx-yefYo8hywI5uIahH60H8oU0",
    "authDomain": "fingerprint-contact.firebaseapp.com",
    "databaseURL": "",
    "projectId": "fingerprint-contact",
    "storageBucket": "fingerprint-contact.appspot.com",
    "serviceAccount": "webapp/database/serviceAccountKey.json",
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()


def upload_to_firebase(path_on_cloud, path_local):
    storage.child(path_on_cloud).put(path_local)


def download_from_firebase(path_on_cloud, path_local):

    storage.child(path_on_cloud).download(path_on_cloud, "webapp/database/Contact_Tracing.db")
    print('Updating database')



if __name__ == "__main__":
    
# upload_to_firebase('database/Contact_Tracing.db',
#                    'webapp/database/Contact_Tracing.db')

    # download_from_firebase('database/Contact_Tracing.db',
    #                     r'webapp\database\')
    
    # storage.child('database/Contact_Tracing.db').download(path="database/Contact_Tracing.db", filename="webapp/database/Contact_Tracing.db")

    upload_to_firebase('database/Contact_Tracing.db', 'webapp/database/update/Contact_Tracing.db')