<html lang="en">
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Mono&display=swap" rel="stylesheet">
</head>
<body>
    <main
        class="container w-xl-50 w-xxl-50 w-lg-50 w-md-50 d-flex justify-content-center mt-3 border border-1 flex-column bg-light">
        <h1 class="text-center display-5 fw-bold text-dark " >API Docs</h1>
        <p class="text-center text-dark">
            The open and supported part of the Anipic API is incredibly easy to use.
            <br>
            You can find more information about how to utilize this in your application below.
        </p>
        <div class="btn-group" role="group" aria-label="Basic radio toggle button group">
            <input type="radio" class="btn-check " name="section" id="imageSection" autocomplete="off" 
                checked>
            <label class="btn btn-outline-dark py-3 border-0 me-2 " for="imageSection"> <h5>Image API</h5></label>
            <input type="radio" class="btn-check" name="section" id="quoteSection"  autocomplete="off" disabled>
            <label class="btn btn-outline-dark py-3 border-0 " for="quoteSection" disabled><h5 class="text-dark">Quotes API</h5></label>
        </div>
        <hr>
        <section id="image" style="display: block;">
            <h2 class="text-center mb-2 text-dark">Image Categories</h2>
            <div class="btn-group d-flex justify-content-center w-25 mx-auto role=" group"
                aria-label="Basic radio toggle button group">
                <input type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" 
                    checked>
                <label class="btn btn-outline-dark border-0  me-2" for="btnradio1"> SFW</label>
                <input type="radio" class="btn-check " name="btnradio" id="btnradio2" autocomplete="off"
                   disabled>
                <label class="btn btn-outline-dark  border-0" for="btnradio2">NSFW</label>
            </div>
            <ul class="list-group text-start w-50 mt-2    " style="display: block; margin: auto; max-height: 250px;
                        overflow-y: auto;  " id="sfw">
                <li class="list-group-item ">Cat girl</li>
                <li class="list-group-item ">Waifu</li>
                <li class="list-group-item ">Maid</li>
                <li class="list-group-item ">Kawaii</li>
                <li class="list-group-item ">Pat</li>
            </ul>
            <hr>
            <h2 class="text-center  mb-2 text-dark ">Get Image</h2>
            <table class="table w-50 " style="margin-left: 375px;">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">URL</th>
                        <th scope="col">Type</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td scope="row">https://anipic.live/pics/type/category</td>
                        <td>GET</td>
                    </tr>
                </tbody>
            </table>
            <p class="fst-italic mx-auto text-center" style="font-size:10px;">
                *The only valid types are sfw and nfsw.You can
                choose category according to the types you like from the ones given above.
            </p>
            <h5 class="text-center  mb-2 ">Search Parameters</h5>
            <table class="table w-50 mx-auto">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">Name</th>
                        <th scope="col">Type</th>
                        <th scope="col">Default</th>
                        <th scope="col">Description</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td >limit</td>
                        <td>Integer</td>
                        <td>12</td>
                        <td>Number of images to return</td>
                    </tr>
                    <tr>
                        <td >offset</td>
                        <td>Integer</td>
                        <td>0</td>
                        <td>Offset parameter controls the starting point within the collection of resource results</td>
                    </tr>
                </tbody>
            </table>
            <hr>
            <h2 class="text-center  mb-2 text-dark">Response</h2>
            <span class="justify-content-center text-dark h5" id="response" style="display: flex;">{....}</span>
        </section>
    </main>
</body>
</html>
