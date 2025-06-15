import ffmpeg

def trim_video(video_name: str, duration: int, start: int=0):
    stream = ffmpeg.input('data/raw_videos/' + video_name + '.mp4')
    stream = stream.trim(start, duration).filter('setpts', 'PTS-STARTPTS')
    stream = ffmpeg.output(stream, 'data/processed_videos/' + video_name + '_trimmed.mp4')
    stream.run()
    print("Video came out")

def reduce_video_fps(video_name: str, fps: int):
    stream = ffmpeg.input('data/raw_videos/' + video_name + '.mp4')
    stream = stream.filter('fps', fps, round='up')
    stream = ffmpeg.output(stream, 'data/processed_videos/' + video_name + '_trimmed.mp4')
    stream.run()
    print("Video came out")

if __name__ == '__main__':
    video_name = 'cricket_test_commentary'
    reduce_video_fps(video_name=video_name, fps=3)
