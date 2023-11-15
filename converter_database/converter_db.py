
'''
"-ac" (Audio Channels) 1 = mono, 2 = stereo # Set audio to stereo (2 channels) 
example: '-ac', '2'

"-c:a" (Audio Codec) # Use the Vorbis audio codec #process format
commonly used value
mp3 = libmp3lame
aac = aac
alac = alac
wav = pcm_s16le
m4a = aac
flac = flac
wma = wma
amr = amr
oga = libvorbis

"-q:a" (Audio Quality/Qscale) # Set audio quality to 4(moderate quality) (0-10) 0 is the best
example: '-q:a', '4'

"-q:v"

"-c:v" 
commonly used value
mp4 = libx264 (H.264), '-c:a', 'aac'
avi = mjpeg, '-c:a', 'mp3'
mov = h254, '-c:a', 'aac'
flv = flv, '-c:a', 'mp3'
wmv = wmv2, '-c:a', 'wmav2'
webm = libvpx, '-c:a', 'libvorbis'
mkv = libx264, '-c:a', 'aac'

"-ar" # sample rate e.g. 44100
"-b:a" # Audio Bitrate e.g. 192k
"-b:v: # Video Bitrate e.g. 192k
"-af" audio filter # Volume 

list_of_audio_format = ['.mp3', '.aac', '.alac'('.m4a'), '.wav', '.m4a', 
                         '.flac', '.wma', '.amr', '.oga']
list_of_video_format = ['.mp4', '.avi', '.wmv', '.mov', '.flv', 
                         '.webm', '.mkv']

list_of_cmd = [ "-ac", "-c:a", "-c:v", "-q:a", "-q:v", 
               "-ar", "-b:a", "-b:v", "-af" ]



'''

Audio = {"mp3": {"-c:a": {"0": {"libmp3lame": {
                                                "-ac": ['2', '1'], # 1 = mono, 2 = stereo
                                                "-ar": ['8000', '11025', '12000', '16000', '22050', '24000', '32000', '44100', '48000', '64000', '96000'], 
                                                "-b:a": ['64000','96000', '128000', '160000', '192000', '240000', '256000'], 
                                                }}}, "container": "mp3"}, 
                 

        "aac": {"-c:a": {"0": {"aac": {
                                                "-ac": ['2', '1'], # 1 = mono, 2 = stereo
                                                "-ar": ['8000', '11025', '12000', '16000', '22050', '24000', '32000', '44100', '48000', '64000', '96000'], 
                                                "-b:a": ['64000','96000', '128000', '160000', '192000', '240000', '256000'],
                                                }}}, "container": "aac"}, 
                

        "alac": {"-c:a": {"0": {"alac": {
                                                "-ac": ['2', '1'], # 1 = mono, 2 = stereo
                                                "-ar": ['16000', '22050', '24000', '32000', '44100', '48000', '64000', '96000', '192000', '384000'], # hi-res
                                                "-b:a": ['128000', '160000', '192000', '240000', '256000', '1411000', '4608000', '9216000'], # hi-res
                                                }}}, "container": "m4a"}, 
                

        "wav": {"-c:a": {"0": {"pcm_s16le": {
                                                "-ac": ['2', '1'], # 1 = mono, 2 = stereo
                                                "-ar": ['16000', '22050', '24000', '32000', '44100', '48000', '64000', '96000', '192000', '384000'], # hi-res
                                                "-b:a": ['128000', '160000', '192000', '240000', '256000', '1411000', '4608000', '9216000'], # hi-res
                                                }}, 

                        "1": {"pcm_s24le": {
                                                "-ac": ['2', '1'], # 1 = mono, 2 = stereo
                                                "-ar": ['16000', '22050', '24000', '32000', '44100', '48000', '64000', '96000', '192000', '384000'], 
                                                "-b:a": ['128000', '160000', '192000', '240000', '256000', '1411000', '4608000', '9216000'],
                                                }},

                        "2": {"pcm_s32le": {
                                                "-ac": ['2', '1'], # 1 = mono, 2 = stereo
                                                "-ar": ['16000', '22050', '24000', '32000', '44100', '48000', '64000', '96000', '192000', '384000'], 
                                                "-b:a": ['128000', '160000', '192000', '240000', '256000', '1411000', '4608000', '9216000'],
                                                }}}, "container": "wav"},
                

        "m4a": {"-c:a": {"0": {"aac": {
                                                "-ac": ['2', '1'], # 1 = mono, 2 = stereo
                                                "-ar": ['8000', '11025', '12000', '16000', '22050', '24000', '32000', '44100', '48000', '64000', '96000'], 
                                                "-b:a": ['64000','96000', '128000', '160000', '192000', '240000', '256000', '320000'], # max 320
                                                }}}, "container": "m4a"},
                

        "flac": {"-c:a": {"0": {"flac": {
                                                "-ac": ['2', '1'], # 1 = mono, 2 = stereo
                                                "-ar": ['16000', '22050', '24000', '32000', '44100', '48000', '64000', '96000', '192000', '384000'], # hi-res
                                                "-b:a": ['128000', '160000', '192000', '240000', '256000', '1411000', '4608000', '9216000'], # hi-res
                                                }}}, "container": "flac"},
                

        "wma": {"-c:a": {"0": {"wmav2": {
                                                "-ac": ['2', '1'], # 1 = mono, 2 = stereo
                                                "-ar": ['22050', '24000', '32000', '44100', '48000'], # min 22050
                                                "-b:a": ['64000','96000', '128000', '160000', '192000', '240000', '256000'],
                                                }}}, "container": "wma"},
                

        "amr": {"-c:a": {"0": {"libopencore_amrnb": {
                                                "-ac": ['1'], # 1 = mono only
                                                "-ar": ['8000'], # 8000 only low quality
                                                "-b:a": ['4750', '5150', '5900', '6700', '7400', '7950', '10200', '12200'],
                                                }},

                        "1": {"libvo_amrwbenc": {
                                                "-ac": ['1'], # 1 = mono only
                                                "-ar": ['16000'], # 16000 only low quality
                                                "-b:a": ['6600', '8850', '12650', '14250', '15850', '18250', '19850', '23050', '23850'],
                                                }}}, "container": "amr"},
                

        "oga": {"-c:a": {"0": {"libvorbis": {
                                                "-ac": ['2', '1'], # 1 = mono, 2 = stereo
                                                "-ar": ['8000', '11025', '12000', '16000', '22050', '24000', '32000', '44100', '48000', '64000', '96000'], 
                                                "-b:a": ['64000','96000', '128000', '160000', '192000', '240000', '256000'],
                                                }}}, "container": "oga"}, 
                
         
        "-q:a": [str(x) for x in range(11)], # default: 5 ,moderate quality

        "-af": {str(i * 10) + '%': str(v / 10.0) for i, v in enumerate(range(31))} # default volume: 100%
}

Video = {"mp4": {"-c:v": {"0": "libx264",

                        "1": "libx265"}}, 

        "avi": {"-c:v": {"0": "libx264",

                        "1": "mpeg4"}},

        "mov": {"-c:v": {"0": "libx264",

                        "1": "prores"}},

        "flv": {"-c:v": {"0": "libx264",
                 
                        "1": "flv"}},

        "webm": {"-c:v": {"0": "libvpx-vp9",

                        "1": "libvpx"}},

        "mkv": {"-c:v": {"0": "libx264",

                        "1": "libx265"}},

        "-af": {str(i * 10) + '%': str(v / 10.0) for i, v in enumerate(range(31))}, # default volume: 100%
         
        "-crf": [str(x) for x in range(52)], #0: lossless, 18: high quality, 23:normal, 28: low, 51 worst

        "-preset": ['ultrafast', 'superfast', 'veryfast', 'faster', 'fast', 'medium', 'slow', 'slower', 'veryslow'], 

        "-q:v": [str(x) for x in range(32)],

        "-vf": {"240p": "320x240", 
                "480p": "640x480",
                "720p": "960x720", 
                "720p_HD": "1280x720", 
                "1080p": "1440x1080",
                "1080p_Full_HD": "1920x1080",
                "1440p_2K_WQHD": "2560x1440",
                "2160p_4K_UHD": "3840x2160"}, 

        "-r": [str(x) for x in range(15, 61)[::5]] 

}

Image = {"image": {"format":["jpg", "png"], 
                   "-q:v": [str(x) for x in range(32)],
                   "-r": [str(x) for x in range(15, 61)[::5]], 
                   "-vf": 
                        {"240p": "320x240", 
                        "480p": "640x480",
                        "720p": "960x720", 
                        "720p_HD": "1280x720", 
                        "1080p": "1440x1080",
                        "1080p_Full_HD": "1920x1080",
                        "1440p_2K_WQHD": "2560x1440",
                        "2160p_4K_UHD": "3840x2160"}}}

Gif = {"gif": {"-vf": 
                    {"240p": "320x240", 
                    "480p": "640x480",
                    "720p": "960x720", 
                    "720p_HD": "1280x720", 
                    "1080p": "1440x1080",
                    "1080p_Full_HD": "1920x1080",
                    "1440p_2K_WQHD": "2560x1440",
                    "2160p_4K_UHD": "3840x2160"},
                "-q:v": [str(x) for x in range(32)],
                "-t": '', 
                "-r": [str(x) for x in range(15, 61)[::5]], 
                "-loop": ''}}

message = {
    
        'format': 

    """--------------------------------------
Output format Options

***Press enter for default option (mp3)

Please enter the output format below :
                                  
- mp3(default)   
- aac
- alac
- wav
- m4a
- flac
- wma
- amr
- oga
            
--------------------------------------
"""
,       
        'option': {
    
                'mp3': {'-c:a':{'audio_code':
                                """\n--------------------------------------
Audio Codec Options

***Press enter for default option 

Please enter the value below :
                                
1. libmp3lame(default)  
        
--------------------------------------\n""", '0':{'libmp3lame':{}}}}, 
                'aac': {'-c:a':{'audio_code':
                                """\n--------------------------------------
Audio Codec Options

***Press enter for default option 

Please enter the value below :
                                
1. aac(default) 
        
--------------------------------------\n""", '0':{'aac':{}}}}, 
                'alac': {'-c:a':{'audio_code':
                                 """\n--------------------------------------
Audio Codec Options

***Press enter for default option 

Please enter the value below :
                                
1. alac(default) 
        
--------------------------------------\n""", '0':{'alac':{}}}}, 
                'wav': {'-c:a':{'audio_code':
                """\n--------------------------------------
Audio Codec Options

***Press enter for default option (pcm_s16le)

Please enter the value below :
                                
1. pcm_s16le(default) 
2. pcm_s24le   
3. pcm_s32le
        
--------------------------------------\n""", 

                '0':{'pcm_s16le':{}},
                '1':{'pcm_s24le':{}}, 
                '2':{'pcm_s32le':{}}}}, 

                'm4a': {'-c:a':{'audio_code':
                                """\n--------------------------------------
Audio Codec Options

***Press enter for default option 

Please enter the value below :
                                
1. aac(default) 
        
--------------------------------------\n""", '0':{'aac':{}}}}, 
                'flac': {'-c:a':{'audio_code':
                                 """\n--------------------------------------
Audio Codec Options

***Press enter for default option 

Please enter the value below :
                                
1. flac(default) 
        
--------------------------------------\n""", '0':{'flac':{}}}}, 
                'wma': {'-c:a':{'audio_code':
                                """\n--------------------------------------
Audio Codec Options

***Press enter for default option 

Please enter the value below :
                                
1. wmav2(default) 
        
--------------------------------------\n""", '0':{'wmav2':{}}}}, 
                'amr': {'-c:a':{'audio_code':
                                """\n--------------------------------------
Audio Codec Options

***Press enter for default option 

Please enter the value below :
                                
1. libopencore_amrnb(default)
2. libvo_amrwbenc
        
--------------------------------------\n""", '0':{'libopencore_amrnb':{'-ac':'', '-ar':'', '-b:a':''}}, '1':{'libvo_amrwbenc':{}}}}, 
                'oga': {'-c:a':{'audio_code':
                                """\n--------------------------------------
Audio Codec Options

***Press enter for default option 

Please enter the value below :
                                
1. oga(default)
        
--------------------------------------\n""", '0':{'libvorbis':{}}}},

                '-q:a':"""\n--------------------------------------
Audio Quality/Qscale Options

***Press enter for default option (Qscale:5)

Please enter a number (1-10):

( 0:highest quality, 10: lowest quality)
                                                
--------------------------------------\n""",

                '-af':"""\n--------------------------------------
Output Volume Options

***Press enter for default option (Volume: 100%)

Please enter a percentage of volume (0% to 300%):
                  
--------------------------------------\n"""
        }, 

        'error':{ 
        "re-enter a valid option": "\nPlease enter a valid option\n", 
        "re-enter a valid format": "\nPlease enter a valid file format\n"
        }
}

# Message of Audio Channel Options
for k1 in message['option']:
    if k1 == 'amr':
        for k2 in message['option'][k1]['-c:a']:
            if k2 != 'audio_code':
                for k3 in message['option'][k1]['-c:a'][k2]:
                    message['option'][k1]['-c:a'][k2][k3]['-ac'] = """\n--------------------------------------
Audio Channel Options

*** Press enter for default option (stereo)

Please enter the value below :
                                  
1. mono(default)
                  
--------------------------------------\n"""

    elif k1 != '-q:a' and k1 != '-af':
        for k2 in message['option'][k1]['-c:a']:
            if k2 != 'audio_code':
                for k3 in message['option'][k1]['-c:a'][k2]:
                    message['option'][k1]['-c:a'][k2][k3]['-ac'] = """\n--------------------------------------
Audio Channel Options

*** Press enter for default option (stereo)

Please enter the value below :

1. stereo(default)                                 
2. mono
                  
--------------------------------------\n"""

# Message of Sample rate(Hz) Options
for k1 in message['option']:
    if k1 == 'amr':
        for k2 in message['option'][k1]['-c:a']:
            if k2 != 'audio_code':
                for k3 in message['option'][k1]['-c:a'][k2]:
                    if k3 == 'amr_nb':
                        message['option'][k1]['-c:a'][k2][k3]['-ar'] = """\n--------------------------------------
Sample rate(Hz) Options

***Press enter for default option (44100Hz)

Please enter the value below :
                                  
1. 8000(default)
                  
--------------------------------------\n"""
                    else:
                        message['option'][k1]['-c:a'][k2][k3]['-ar'] = """\n--------------------------------------
Sample rate(Hz) Options

***Press enter for default option (44100Hz)

Please enter the value below :
                                  
1. 16000(default)
                  
--------------------------------------\n"""

    elif k1 == 'wma':
        for k2 in message['option'][k1]['-c:a']:
            if k2 != 'audio_code':
                for k3 in message['option'][k1]['-c:a'][k2]:
                    message['option'][k1]['-c:a'][k2][k3]['-ar'] = """\n--------------------------------------
Sample rate(Hz) Options

***Press enter for default option (44100Hz)

Please enter the value below :
                                  
1. 22050
2. 24000(default)
3. 32000
4. 44100
5. 48000
          
--------------------------------------\n"""

    elif k1 == 'alac' or k1 == 'wav' or k1 == 'flac' :
        for k2 in message['option'][k1]['-c:a']:
            if k2 != 'audio_code':
                for k3 in message['option'][k1]['-c:a'][k2]:
                    message['option'][k1]['-c:a'][k2][k3]['-ar'] = """\n--------------------------------------
Sample rate(Hz) Options

***Press enter for default option (44100Hz)

Please enter the value below :

1. 16000
2. 22050
3. 24000
4. 32000
5. 44100(default)
6. 48000
7. 64000
8. 96000
9. 192000
10. 384000
          
--------------------------------------\n"""
    elif k1 != '-q:a' and k1 != '-af':
        for k2 in message['option'][k1]['-c:a']:
            if k2 != 'audio_code':
                for k3 in message['option'][k1]['-c:a'][k2]:
                    message['option'][k1]['-c:a'][k2][k3]['-ar'] = """\n--------------------------------------
Sample rate(Hz) Options

***Press enter for default option (44100Hz)

Please enter the value below :

1. 8000
2. 11025
3. 12000
4. 16000
5. 22050
6. 24000
7. 32000
8. 44100(default)
9. 48000
10. 64000
11. 96000

--------------------------------------\n"""

# Message of Audio Bitrate(kbps) Options
for k1 in message['option']:
    
    if k1 == 'alac' or k1 == 'wav' or k1 == 'flac' :
        for k2 in message['option'][k1]['-c:a']:
            if k2 != 'audio_code':
                for k3 in message['option'][k1]['-c:a'][k2]:
                    
                    message['option'][k1]['-c:a'][k2][k3]['-b:a'] = """\n--------------------------------------
Audio Bitrate(kbps) Options

***Press enter for default option 

Please enter the value below :
                                  
1. 128kbps
2. 160kbps
3. 192kbps
4. 240kbps
5. 250kbps(default)
6. 1411kbps
7. 4608kbps
8. 9216kbps
                  
--------------------------------------\n"""

    elif k1 == 'amr':
        for k2 in message['option'][k1]['-c:a']:
            if k2 == '0':
                for k3 in message['option'][k1]['-c:a'][k2]:
                    message['option'][k1]['-c:a'][k2][k3]['-b:a'] = """\n--------------------------------------
Audio Bitrate(kbps) Options

***Press enter for default option 

Please enter the value below :
                                  
1. 4.75kbps
2. 5.15kbps
3. 5.90kbps
4. 6.70kbps
5. 7.40kbps(default)
6. 7.95kbps
7. 10.20kbps
8. 12.20kbps
                  
--------------------------------------\n"""
        else:
            for k3 in message['option'][k1]['-c:a'][k2]:
                    message['option'][k1]['-c:a'][k2][k3]['-b:a'] = """\n--------------------------------------
Audio Bitrate(kbps) Options

***Press enter for default option 

Please enter the value below :
                                  
1. 6.60kbps
2. 8.85kbps
3. 12.65kbps
4. 14.25kbps
5. 15.85kbps(default)
6. 18.25kbps
7. 19.85kbps
8. 23.05kbps
9. 23.85kbps
                  
--------------------------------------\n"""


    elif k1 == 'm4a':
        for k2 in message['option'][k1]['-c:a']:
            if k2 != 'audio_code':
                for k3 in message['option'][k1]['-c:a'][k2]:
                    message['option'][k1]['-c:a'][k2][k3]['-b:a'] = """\n--------------------------------------
Audio Bitrate(kbps) Options

***Press enter for default option 

Please enter the value below :
                                  
1. 64kbps
2. 96kbps
3. 128kbps
4. 160kbps
5. 192kbps(default)
6. 240kbps
7. 256kbps
8. 320kbps
                  
--------------------------------------\n"""

    elif k1 != '-q:a' and k1 != '-af':
        for k2 in message['option'][k1]['-c:a']:
            if k2 != 'audio_code':
                for k3 in message['option'][k1]['-c:a'][k2]:
                    message['option'][k1]['-c:a'][k2][k3]['-b:a'] = """\n--------------------------------------
Audio Bitrate(kbps) Options

***Press enter for default option 

Please enter the value below :
                                  
1. 64kbps
2. 96kbps
3. 128kbps
4. 160kbps
5. 192kbps(default)
6. 240kbps
7. 256kbps
                  
--------------------------------------\n"""

def main():
    pass

if __name__=='__main__':
    main()
