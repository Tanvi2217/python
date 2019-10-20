import cgi
import base
import model

form = cgi.FieldStorage()
p_data = form.getvalue("post_data")
post_pic = form['pic_post']
email = form.getvalue('email')

model.post(p_data,post_pic,email)
print("""
    <!doctype html>
    <html lang="en">

    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

        <title>Hello, world!</title>
        <link rel="stylesheet" href="styles.css">
    </head>

    <body>
    """)

base.header(email)

print("<div class='container'>")
print("<h3>Post Updated</h3>")
print(email)
print("</div>")
print("""
   </body>
   </html>
   """)

