import base
import cgi

form = cgi.FieldStorage()
email = form.getvalue("email")


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
print("""<h2>CREATE POST</h2>
<hr>""")
print("""
<form action="postController.py" method="post" enctype='multipart/form-data'>
<input type="hidden" value={} name="email"> 
  <div class="form-group">
    <label for="exampleFormControlTextarea1">Write something here....</label>
    <textarea class="form-control" id="exampleFormControlTextarea1" name = "post_data" rows="3"></textarea>
  </div>
  <div class="form-group">
  <label for="p_pic">Select a photo</label>
    <input type="file" id="p_pic" name="pic_post">
  </div>
  <button type="submit" class="btn btn-primary">POST</button>
</form>
</form>
""".format(email))

print("</div>")
print("""
</body>
</html>
""")
