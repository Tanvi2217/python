import cgi
import model

form = cgi.FieldStorage()
msg = form.getvalue('com')
email = form.getvalue('email')

model.com(msg)

print("""
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <script>
        location.href = "http://localhost:4545/cgi-bin/feed.py?email={}";
    </script>
  </head>
  <body>
  </body>
  </html>
""".format(email))
