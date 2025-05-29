import boto3
from botocore.exceptions import ClientError
import glob
from typing import Tuple, List
from xml.etree import ElementTree as ET
from tqdm import tqdm

from bluer_objects.storage.base import StorageInterface
from bluer_objects import env, file, path
from bluer_objects import objects
from bluer_objects.logger import logger


# https://docs.arvancloud.ir/fa/developer-tools/sdk/object-storage/
class ArvancloudInterface(StorageInterface):
    name = "arvancloud"

    def upload(
        self,
        object_name: str,
        filename: str = "",
        log: bool = True,
    ) -> bool:
        if filename:
            local_path = objects.path_of(
                object_name=object_name,
                filename=filename,
            )

            try:
                s3_resource = boto3.resource(
                    "s3",
                    endpoint_url=env.ARVANCLOUD_STORAGE_ENDPOINT_URL,
                    aws_access_key_id=env.ARVANCLOUD_STORAGE_AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=env.ARVANCLOUD_STORAGE_AWS_SECRET_ACCESS_KEY,
                )

            except Exception as e:
                logger.error(e)
                return False

            try:
                bucket = s3_resource.Bucket(env.ARVANCLOUD_STORAGE_BUCKET)

                with open(local_path, "rb") as fp:
                    bucket.put_object(
                        ACL="private",
                        Body=fp,
                        Key=f"{object_name}/{filename}",
                    )
            except ClientError as e:
                logger.error(e)
                return False

            return super().upload(
                object_name=object_name,
                filename=filename,
                log=log,
            )

        object_path = "{}/".format(objects.object_path(object_name=object_name))
        for filename_ in tqdm(
            sorted(
                glob.glob(
                    objects.path_of(
                        object_name=object_name,
                        filename="**",
                    ),
                    recursive=True,
                )
            )
        ):
            if not file.exists(filename_):
                continue

            if not self.upload(
                object_name=object_name,
                filename=filename_.split(object_path, 1)[1],
                log=log,
            ):
                return False

        return True
