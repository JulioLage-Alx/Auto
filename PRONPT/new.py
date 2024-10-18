from tiktok_uploader.upload import upload_video, upload_videos
from tiktok_uploader.auth import AuthBackend
BROWSERS =['edge']
# single video
upload_video('C:\\Users\\julio\\OneDrive\\Documentos\\GitHub\\Auto\\VIDEOS\\2024-09-26_01-39-55.mp4',
            description='this is my description',
            cookies='C:\\Users\\julio\\OneDrive\\Documentos\\GitHub\\Auto\\COOKIES\\cookies.txt',browser=choice(BROWSERS))
