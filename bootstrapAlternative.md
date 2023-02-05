<!-- #############HTML############# -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <link rel="stylesheet" href="styles.css">
    <title>Image Filter</title>
</head>
<body>
    
    <!-- ##############################Heading####################################### -->

    <div class="heading">
        <h1>Image Filter</h1>
        <p class="description">"<em>Add any preset to your image and make it look </em><strong>Amazing</strong>!"</p>
    </div>

    <!-- ############################ImageFilter##################################### -->

    <h1 class="h4 text-center mb-3">Drag &amp; drop file upload example</h1>

    <form>
    
      <fieldset class="upload_dropZone text-center mb-3 p-4">
    
        <legend class="visually-hidden">Image uploader</legend>
    
        <svg class="upload_svg" width="60" height="60" aria-hidden="true">
          <use href="#icon-imageUpload"></use>
        </svg>
    
        <p class="small my-2">Drag &amp; Drop background image(s) inside dashed region<br><i>or</i></p>
    
        <input id="upload_image_background" data-post-name="image_background" data-post-url="https://someplace.com/image/uploads/backgrounds/" class="position-absolute invisible" type="file" multiple accept="image/jpeg, image/png, image/svg+xml" />
    
        <label class="btn btn-upload mb-3" for="upload_image_background">Choose file(s)</label>
    
        <div class="upload_gallery d-flex flex-wrap justify-content-center gap-3 mb-0"></div>
    
      </fieldset>
    
    
    
      
    
    </form>
    
    
    <svg style="display:none">
      <defs>
        <symbol id="icon-imageUpload" clip-rule="evenodd" viewBox="0 0 96 96">
          <path d="M47 6a21 21 0 0 0-12.3 3.8c-2.7 2.1-4.4 5-4.7 7.1-5.8 1.2-10.3 5.6-10.3 10.6 0 6 5.8 11 13 11h12.6V22.7l-7.1 6.8c-.4.3-.9.5-1.4.5-1 0-2-.8-2-1.7 0-.4.3-.9.6-1.2l10.3-8.8c.3-.4.8-.6 1.3-.6.6 0 1 .2 1.4.6l10.2 8.8c.4.3.6.8.6 1.2 0 1-.9 1.7-2 1.7-.5 0-1-.2-1.3-.5l-7.2-6.8v15.6h14.4c6.1 0 11.2-4.1 11.2-9.4 0-5-4-8.8-9.5-9.4C63.8 11.8 56 5.8 47 6Zm-1.7 42.7V38.4h3.4v10.3c0 .8-.7 1.5-1.7 1.5s-1.7-.7-1.7-1.5Z M27 49c-4 0-7 2-7 6v29c0 3 3 6 6 6h42c3 0 6-3 6-6V55c0-4-3-6-7-6H28Zm41 3c1 0 3 1 3 3v19l-13-6a2 2 0 0 0-2 0L44 79l-10-5a2 2 0 0 0-2 0l-9 7V55c0-2 2-3 4-3h41Z M40 62c0 2-2 4-5 4s-5-2-5-4 2-4 5-4 5 2 5 4Z"/>
        </symbol>
      </defs>
    </svg>



    <!-- ##############################SCRIPT######################################## -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
    <script src="index.js" charset="UTF-8"></script>
</body>
</html>


<!-- #############CSS############# -->


<!-- #############SCRIPT############# -->