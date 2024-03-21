from projects.megaepic.homework.Elbey_gamidov.Lesson_16 import creds


db = mysql.connect(
    user=creds.user,
    passwd=creds.passwd,
    host=creds.host,
    port=creds.port,
    database=creds.database
)

