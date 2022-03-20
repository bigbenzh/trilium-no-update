with open("src/public/app/widgets/buttons/global_menu.js","r+") as f:
    d = f.read()
    d = d.replace("const latestVersion = await this.fetchLatestVersion();","const latestVersion = glob.triliumVersion;")
    f.seek(0)
    f.write(d)
    f.truncate() # resize the file to avoid extra bytes

