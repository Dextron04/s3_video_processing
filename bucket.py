import boto3
import time

s3 = boto3.client("s3")
BUCKET_NAME = "dex-video-processing-bucket"

def generate_presigned_url(file_name, expiration=3600):

    try:
        res = s3.generate_presigned_url(
            'put_object',
            Params={
                'Bucket': BUCKET_NAME,
                'Key': file_name
            },
        )
        return res
    except Exception as e:
        print(f"Error generating presigned URL: {e}")


video_url = generate_presigned_url("video.mp4")
print(f"Presigned URL: {video_url}")