Global arguments:
    https   = 1|0           # Returns only https.
    format  = json|plain    # Desired format.

    For list:
        number  = n < 100       # Number of results.

    country ???
    ssl ???
    

Get one:
    /get_proxy/<format>
        "https://164.41.21.118:8080"

    /get_proxy?https=1&format=json
        ["https://164.41.21.118:8080"]


Get list:
    /get_proxy_list/<format>/<number>
    [
        "http://107.151.152.213:80", 
        "http://31.171.249.87:80", 
        ....
    ]

    /get_proxy_list?number=20&format=plain
        "http://107.151.152.213:80", 
        "http://31.171.249.87:80", 
        ....

