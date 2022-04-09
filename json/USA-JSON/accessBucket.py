from google.cloud import storage


def initialize(project_id, bucket_name):
    return GoogleStorage(project_id=project_id, bucket_name=bucket_name)


class GoogleStorage(object):
    def __init__(self, project_id=None, bucket_name=None):
        self.project_id = project_id
        self.bucket_name = bucket_name

        self._client = None
        self._bucket = None

    @property
    def _con(self):
        if not self._client:
            self._client = storage.Client(project=self.project_id)
        return self._client

    @property
    def _b(self):
        if not self._bucket:
            self._bucket = self._con.get_bucket(self.bucket_name)
        return self._bucket

    def __enter__(self):
        return self

    def list_bucket_labels(self):
        """List GCS bucket labels for instantiated GoogleStorage class. This is
        useful for testing GCS connectivity purposes."""
        return self._b.labels

    def upload_blob(self, source_file_name, destination_blob_name):
        """Uploads a file to the bucket."""
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
        # The path to your file to upload
        # source_file_name = "local/path/to/file"
        # The ID of your GCS object
        # destination_blob_name = "storage-object-name"

        # storage_client = storage.Client()
        # bucket = storage_client.bucket(bucket_name)
        blob = self._b.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)
