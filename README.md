# PythonDjango
## Installation
1. Clone this repository
2. pip install -U Pillow
3. Change directory - cd CrimeDetection
4. run python manage.py runserver
      
## Upload Images to Amazon S3 using Django

    # Here is a diagram:
```
djangobucket  ------------> bob ---------> picture1.jpg
                                           picture2.jpg
                                           picture3.jpg
                                           picture4.jpg
```                                           

  ```boto``` is the best way to do this.

You can get an existing bucket using:

```get_bucket(bucket_name, validate=True, headers=None)```

After installing boto, this code should do what you need to do:

```
from boto.s3.connection import S3Connection
from boto.s3.key import Key

conn = S3Connection('<aws access key>', '<aws secret key>')
bucket = conn.get_bucket('<bucket name>')
k = Key(bucket)
k.key = 'file_path_on_s3' # for example, 'images/bob/resized_image1.png'
k.set_contents_from_file(resized_photo)
```
