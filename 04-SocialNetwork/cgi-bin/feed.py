import cgi
import model
import base

form = cgi.FieldStorage()
email = form.getvalue("email")

data = model.post_show(email)


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
    <script>
    var i = 0;
    function buttonClick() {
        document.getElementById('inc').value = ++i;
    }
  
</script
    
    <body>
    """)

base.header(email)


print("<div class='container'>")
print("""<h2>Your feed </h2>
<hr>
""")
for i in range(len(data)):
    print("""
    <div class="row">
        <div class="col-md-4">
            <img src='../post_pic/{}' class='w-100' alt="post_pic">
        </div>
        <div class="col-md-8">
            <h3>Caption : {}</h3>
        <button type="button" class="btn btn-outline-primary" onclick = "buttonClick()">LIKE</button> 
        <input type="text" id="inc" value="0"></input>
        <hr>
        <form action = "comment.py" method = "post">
        <input type="hidden" value={} name="email">
        <input type="text" class="form-control" id="comment" name="com" placeholder="Write a comment....">
        <button type="submit" class="btn btn-outline-secondary" >COMMENT</button> 
        </form>
        <hr>
        
        <button type="button" class="btn btn-outline-success">SHARE</button>
        
        
    </div>
    """.format(data[i][1],data[i][0],email))





print("</div>")

print("""
</body>
</html>
""")

