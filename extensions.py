def main():
    filename=input("what is the name of the file? ").lower().strip()

    mimey= {
        '.gif' : 'image/gif',
        '.jpg' : 'image/jpeg',
        '.jpeg' : 'image/jpeg',
        '.png' : 'image/png',
        '.pdf' : 'application/pdf',
        '.txt' : 'text/plain',
        '.zip' : 'application/zip'
}

    for mime, media in mimey.items():
        if filename.endswith(mime):
            print(media)
            return

    print("application/octet-stream")

main()
