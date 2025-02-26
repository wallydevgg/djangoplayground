from django.conf import settings
from boto3 import client


class Bucket:
    def __init__(self, folder):
        self.name = settings.AWS_S3_BUCKET_NAME
        self.folder = folder
        self.region = settings.AWS_REGION
        self.access_id = settings.AWS_ACCESS_ID
        self.access_secret = settings.AWS_ACCESS_SECRET_KEY

        self.client = client(
            "s3",
            region_name=self.region,
            aws_access_key_id=self.access_id,
            aws_secret_access_key=self.access_secret,
        )

        self.__url = f"https://{self.name}.s3.{self.region}.amazonaws.com"

    def uploadObject(self, filename, stream):
        try:
            self.client.upload_fileobj(
                stream,
                self.name,
                f"{self.folder}/{filename}",
                ExtraArgs={"ACL": "public-read"},
            )
            return f"{self.__url}/{self.folder}/{filename}"
        except Exception as e:
            raise Exception(f"Bucket upload error -> {str(e)}") from e
