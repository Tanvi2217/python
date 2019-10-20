def header(email):
    print(f"""
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    
  <a class="navbar-brand" href="#">
        <img src="http://pngimg.com/uploads/twitter/twitter_PNG19.png" width="30" height="30" class="d-inline-block align-top" alt=""> My Personal Network
    </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="post.py?email={email}">CreatePost <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="feed.py?email={email}">Feed <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="showProfile.py?email={email}">Profile</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="chat.py?email={email}">Chat</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="editProfile.py?email={email}" tabindex="-1" aria-disabled="true">Edit Profile</a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-primary my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
    """)


def footer():
    pass