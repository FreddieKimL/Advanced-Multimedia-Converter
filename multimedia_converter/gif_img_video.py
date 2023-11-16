import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(f'{parent_dir}\\converter_database')

import converter_db as db
import subprocess
from typing import Union


class Converter:
    def __init__(self) -> None:

        self.ffmpeg = r"C:\Users\Fredd\AppData\Local\Programs\ffmpeg\bin\ffmpeg"
        
        self.video_cmd_dict = db.Video
        self.image_cmd_dict = db.Image
        self.gif_cmd_dict = db.Gif

        
        self.tuple_of_gif_format = ('gif', )
        self.tuple_of_video_format = ('mp4', 'avi', 'mov', 'flv', 'webm', 'mkv')
        self.tuple_of_image_format = ('jpg', 'png')
        
        self.error_message = db.message_for_gif_video_img['error']
        self.option_message = db.message_for_gif_video_img['option']
        self.format_message = db.message_for_gif_video_img['format']
        self.txtfolder_message = db.message_for_gif_video_img['textfolder']

    def original_video_gif_fps(self) -> tuple[str, str]:
        """
        Summary of the Function:
        Get the framerate of the file directly, if the input file format is video or gif

        Returns:
        self.frame_rate (str)
        self.height (str)

        """
        cmd = [
        "ffprobe",
        "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=r_frame_rate,width,height",
        "-of", "default=noprint_wrappers=1:nokey=1",
        f"{self.input_full_file}"]
    
        try:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
            lines = output.splitlines()
            self.height = lines[0]
            self.width = lines[1]
            frame_rate = lines[2]
            self.original_resolution = f"{self.width}x{self.height}"
            self.frame_rate = frame_rate.split('/')[0]

            print("Frame Rate:", self.frame_rate)
            print("Resolution:", self.original_resolution)
            
            return self.frame_rate, self.height
        
        except subprocess.CalledProcessError as e:
            print("Error:", e.returncode, e.output)
            exit()

    def is_valid_input_format(self) -> tuple[str, tuple, tuple, tuple]:
        """
        Summary of the Function:
        Check whether the input format is valid, format must be within the gif, image or video format list

        Parameters:
        self.input_file_format (str)
        self.tuple_of_audio_format (tuple)
        self.tuple_of_video_format (tuple)
        self.tuple_of_image_format (tuple)

        Returns:
        self.input_file_format (str)
        self.tuple_of_video_format (tuple)
        self.tuple_of_gif_format (tuple)
        self.tuple_of_image_format (tuple)
        
        """
        valid_format = self.tuple_of_gif_format + self.tuple_of_video_format + self.tuple_of_image_format
        
        if self.input_file_format in valid_format:
            return self.input_file_format, self.tuple_of_video_format, self.tuple_of_gif_format, self.tuple_of_image_format

    def get_input_format_and_filename(self) -> tuple[list, str]:
        """
        Summary of the Function:
        Collect the input filename and format, and then check whether the format is exist or not
        Only valid input is accepted, otherwise, error message printed.

        Parameters:
        user input (str): filename and file format (e.g. sample.mp4)
        self.error_message (str)
        
        Returns:
        [self.input_file_format (str), self.input_file_format (str)] (list)
        'v' (str): as an index = Input is a Video file
        'g' (str): as an index = Input is a Gif file
        'i' (str): as an index = Input is a image file
        
        """
        while True:
            user_input = input("Please enter a filename (w/ the file format): ")
            self.input_filename = user_input.rsplit('.', 1)[0]
            self.input_file_format = user_input.rsplit('.', 1)[-1].lower()
            self.input_full_file = '.'.join([self.input_filename, self.input_file_format])  

            if self.is_valid_input_format():
                print(f"\nThe is a {self.input_file_format} file \n")
                
                if self.input_file_format in self.is_valid_input_format()[1]:
                    self.input_format_type = 'v'
                    return self.input_full_file, self.input_format_type 
                
                elif self.input_file_format in self.is_valid_input_format()[2]:  
                    self.input_format_type = 'g'
                    return self.input_full_file, self.input_format_type
                
                elif self.input_file_format in self.is_valid_input_format()[3]:  
                    self.input_format_type = 'i'
                    return self.input_full_file, self.input_format_type
            else:
                print(self.error_message["re-enter a valid format"])

    def get_output_format(self, user_input, default_ouput_format) -> tuple[str, str]:
        """
        Summary of the Function:
        Collect the desired output file format. If input is an empty string, default file format is mp4(video), gif and png(image).
        Format is only accepted, when the file format is in the check list

        Parameters:
        user input (str): file format (e.g. wav)
        default file format (str): mp4(video), gif and png(image)

        Returns:
        self.output_format (str): the output format processed
        str: a symbol of output format type

        """

        if user_input == "":
            self.output_format = default_ouput_format
            print(f"\n*** Default output format is {default_ouput_format} ***\n")
            return self.output_format
    
        elif user_input != "":
            self.output_format = user_input
            print(f"\n*** Output file format is {self.output_format} ***\n")
            return self.output_format
        
    def get_valid_txt_folder(self, item_list: list) -> str:
        """
        Summary of the Function:
        Check whether valid txt file found in the directory
        

        Parameters:
        item_list (list): a list of valid filein the directory
        
        Returns:
        item_list[user_input_index] (str): the selected name of the file

        """

        while True:
            user_input = input(self.txtfolder_message)
            try:
                user_input_index = int(user_input) - 1
                if user_input_index in range(len(item_list)):
                    return item_list[user_input_index]
                        
                else:
                    print(self.error_message["re-enter a valid option"])
                    return self.get_valid_txt_folder(item_list)

            except ValueError:
                print(self.error_message["re-enter a valid option"])
                return self.get_valid_txt_folder(item_list)

    def get_output_container(self) -> str: #txt folder name is here
        """
        Summary of the Function:
        Collect the desired output file format. default file format is mp4(video), gif and png(image).
        Format is only accepted, when the file format is in the check list
        3 different kinds of input_format_type will be classified as video, image and gif and get the corresponding output format

        Parameters:
        user input (str): file format (e.g. wav)
        self.video_cmd_dict (dict): get a list of valid formats as a check list, database
        self.image_cmd_dict (dict)
        self.gif_cmd_dict (dict)

        
        Returns:
        self.output_format (str): the output format processed

        """
        while True:
            self.img_folder_list = [file for file in os.listdir(os.getcwd()) if os.path.isdir(file)]
            self.valid_folder_list = [folder for folder in self.img_folder_list if folder.lower().endswith(self.input_file_format)]

            format_video = list(self.video_cmd_dict.keys())
            format_gif = list(self.gif_cmd_dict.keys()) 
            format_image = list(self.image_cmd_dict['image']['format'])

            user_input = input(self.format_message).lower()

            if user_input in format_video or user_input in format_gif:
                if self.input_format_type == 'i':
                    if len(self.valid_folder_list) > 0:
                        self.img_folder = self.get_valid_txt_folder(self.valid_folder_list)
                        self.default_input_fps = self.img_folder.split('_')[-3].rstrip("fps")
                        
                    else:
                        print(f"\nNo valid {self.input_file_format} txt folder found")
                        exit()
                
                if user_input in format_video:
                    default_ouput_format = 'mp4'
                    self.output_format_type = 'v'
                    return self.get_output_format(user_input, default_ouput_format), self.output_format_type 
                
                else:
                    default_ouput_format = 'gif'
                    self.output_format_type = 'g'
                    return self.get_output_format(user_input, default_ouput_format), self.output_format_type
                
            elif user_input in format_image:
                default_ouput_format = 'png'
                self.output_format_type = 'i'
                return self.get_output_format(user_input, default_ouput_format), self.output_format_type
            
            else:
                print(self.error_message["re-enter a valid format"])
                
    def get_output_filename(self) -> str:
        """
        Summary of the Function:
        Collect the desired output filename. If input is empty, the default output filename is equal 
        to input filename.

        Parameters:
        user input (str): filename (e.g. sample)
        self.input_filename (str): the name of input file (original file)
        
        Returns:
        self.output_filename (str)

        """
        
        user_input = input("Please enter the output filename: (default: input filename) ")
        if user_input == "":
            user_input = self.input_filename
            self.output_filename = user_input

            print(f"\nOutput filename: {self.output_filename}\n")
            return self.output_filename
        
        print(f"\nOutput filename: {user_input}\n")
        self.output_filename = user_input
        return self.output_filename

    def option_selector(self, user_input: str, index: str, parameter: str, message: str) -> list:
        """
        Summary of the Function:
        An option selector to extract the corresponding value from self.cmd_dict based on the user option input.
        If the input option is checked as not valid (option value cannot be found in cmd_dict), the process will 
        be loop back to run the option_filter Function for re-entering a valid input

        Parameters:
        user_input (str): the number of selection
        index (str): the index of parameter from the list
        parameter (str)
        message (str): selection options from option filter (Func)

        Returns:
        self.output_filename (str)
        [parameter (str), parameter value from database (str)] (list):
        """

        if self.output_format_type == 'g':
            
            if parameter == "-vf":
                key_list = list(self.gif_cmd_dict['gif'][parameter].keys())
                while True:
                    try:
                        user_input_index = int(user_input) - 1
                        if user_input_index in range(len(key_list)):
                                self.vf_scale_resolution = self.gif_cmd_dict['gif'][parameter][key_list[user_input_index]]
                                vf_scale_value = self.vf_scale_resolution.split('x')[0]
                                return [parameter, f"scale={vf_scale_value}:-1:flags=lanczos"]
                        else:
                            return self.option_filter(index, message, parameter)

                    except ValueError:
                        return self.option_filter(index, message, parameter)
                    
            elif parameter == "-q:v" or parameter == "-r":
                key_list = self.gif_cmd_dict['gif'][parameter]

                while True:
                    try:
                        user_input_index = int(user_input)
                        if user_input_index in range(len(key_list)):
                                if parameter == '-r':
                                    self.input_fps = self.gif_cmd_dict['gif'][parameter][user_input_index]
                                return [parameter, self.gif_cmd_dict['gif'][parameter][user_input_index]]
                        else:
                            return self.option_filter(index, message, parameter)

                    except ValueError:
                        return self.option_filter(index, message, parameter)
                
            else:
                while True:
                    if user_input.isdigit() and int(user_input) >= 0:
                        return [parameter, user_input]
                    else:
                        return self.option_filter(index, message, parameter)

        if self.output_format_type == 'i':

            if parameter == "-vf":
                key_list = list(self.image_cmd_dict['image'][parameter].keys())
                while True:
                    try:
                        user_input_index = int(user_input) - 1
                        if user_input_index in range(len(key_list)):
                                self.vf_scale_display_name = key_list[user_input_index].lower()
                                self.vf_scale_resolution = self.image_cmd_dict['image'][parameter][key_list[user_input_index]]
                                vf_scale_value = self.vf_scale_resolution.split('x')[0]
                                return [parameter, f"scale={vf_scale_value}:-1:flags=lanczos"]
                        else:
                            return self.option_filter(index, message, parameter)

                    except ValueError:
                        return self.option_filter(index, message, parameter)
                    
            elif parameter == "-q:v" or parameter == "-r":
                key_list = self.image_cmd_dict['image'][parameter]

                while True:
                    try:
                        user_input_index = int(user_input)
                        if user_input_index in range(len(key_list)):
                                if parameter == '-r':
                                    self.input_fps = self.image_cmd_dict['image'][parameter][user_input_index]
                                
                                return [parameter, self.image_cmd_dict['image'][parameter][user_input_index]]
                        else:
                            return self.option_filter(index, message, parameter)

                    except ValueError:
                        return self.option_filter(index, message, parameter)

        if self.output_format_type == 'v':

            if parameter == "-c:v":
                key_list = list(self.video_cmd_dict[self.output_format][parameter].keys())
                
                while True:
                    try:
                        user_input_index = int(user_input) - 1
                        if user_input_index in range(len(key_list)):
                            return [parameter, self.video_cmd_dict[self.output_format][parameter][key_list[user_input_index]]]
                        else:
                            return self.option_filter(index, message, parameter)

                    except ValueError:
                        return self.option_filter(index, message, parameter)

            elif parameter == '-preset' or parameter == '-crf' or parameter == '-r' or parameter == '-q:v':
                key_list = self.video_cmd_dict[parameter]

                while True:
                    try:
                        user_input_index = int(user_input) - 1
                        if user_input_index in range(len(key_list)):
                                if parameter == '-r':
                                    self.input_fps = self.video_cmd_dict[parameter][user_input_index]
                                return [parameter, self.video_cmd_dict[parameter][user_input_index]]
                        else:
                            return self.option_filter(index, message, parameter)

                    except ValueError:
                        return self.option_filter(index, message, parameter)

            elif parameter == "-vf":
                key_list = list(self.video_cmd_dict[parameter].keys())
                while True:
                    try:
                        user_input_index = int(user_input) - 1
                        if user_input_index in range(len(key_list)):
                                self.vf_scale_resolution = self.video_cmd_dict[parameter][key_list[user_input_index]]
                                vf_scale_value = self.vf_scale_resolution.split('x')[0]
                                return [parameter, f"scale={vf_scale_value}:-1:flags=lanczos"]
                        else:
                            return self.option_filter(index, message, parameter)

                    except ValueError:
                        return self.option_filter(index, message, parameter)

            elif parameter == '-af':
                while True:
                    if user_input in self.video_cmd_dict[parameter]:
                        return [parameter, self.video_cmd_dict[parameter][user_input]]
                    else:
                        return self.option_filter(index, message, parameter)

    def option_filter(self, index:str, message: str, parameter: str) -> list:
        """
        Summary of the Function:
        an option filter for filtering option of each parameter. 
        If input is a empty string, default value will be selected.
        Otherwise, option selector will be run for option selection

        Parameters:
        index (str): the index of parameter from the list
        parameter (str)
        message (str): selection options from option filter (Func)

        Returns:
        [parameter (str), parameter value (str)] (list)
        
        """
        user_input = input (message).lower()
        if user_input == "":
            if parameter == "-r":
                if self.input_format_type == 'i' and self.output_format_type != 'i':
                    print(f'Default FPS: {self.default_input_fps}')
                    self.input_fps = self.default_input_fps
                    return ['-r', self.input_fps]
                
                elif self.input_format_type != 'i' and self.output_format_type == 'i':
                    print(f'Default FPS: {self.frame_rate}')
                    self.input_fps = self.frame_rate
                    return ['-r', self.input_fps]
                
        else:
            return self.option_selector(user_input, index, parameter, message)

    def option_organizer(self):
        """
        Summary of the Function:
        a container to organize all the related parameter for cmd list. 
        For each the parameter, self.option_filter (Function) will be run for filtering option.

        Returns:
        option_list (list): A list of corresponding parameter and selected value for cmd based on the converting format

        """
        option_list = []

        if self.output_format_type == 'g':
            message_output_fps = self.option_message['gif']['-r']
            message_input_fps = self.option_message['gif']['-r']
            message_vf = self.option_message['gif']['-vf']
            message_qv = self.option_message['gif']['-q:v']
            message_time = self.option_message['gif']['-t']
            message_loop = self.option_message['gif']['-loop']

            if self.input_format_type != 'i':
                message_list = [message_vf, message_qv, message_time, message_loop, message_output_fps]
                parameter_list = ['-vf', '-q:v', '-t', '-loop', '-r']

            elif self.input_format_type == 'i':
                message_list = [message_input_fps, message_qv, message_time, message_loop]
                parameter_list = ['-r', '-q:v', '-t', '-loop']

            for index, message in enumerate(message_list):
                parameter = parameter_list[index]
            
                result = self.option_filter(index, message, parameter)
                if result != None:
                    option_list.extend(result)
            return option_list
        
        elif self.output_format_type == 'i': # v to i, g to i
            message_vf = self.option_message['image']['-vf']
            message_qv = self.option_message['image']['-q:v']
            message_output_fps = self.option_message['image']['-r']

            if self.input_format_type != 'i':
                message_list = [message_vf, message_qv, message_output_fps]
                parameter_list = ['-vf', '-q:v', '-r']

            else:
                option_list = ['-q:v', '0']
                return option_list

            for index, message in enumerate(message_list):
                parameter = parameter_list[index]
                result = self.option_filter(index, message, parameter)
                if result != None:
                    option_list.extend(result)

            return option_list
    
        elif self.output_format_type == 'v':
            
            message_videocodec = self.option_message['video'][self.output_format]
            message_vol = self.option_message['video']['-af']
            message_qv = self.option_message['video']['-q:v']
            message_crf = self.option_message['video']['-crf']
            message_preset = self.option_message['video']['-preset']
            message_resolution = self.option_message['video']['-vf']
            message_input_fps = self.option_message['video']['-r']
            message_output_fps = self.option_message['video']['-r']

            if self.input_format_type == 'g':
                option_list = ['-pix_fmt', 'yuv420p']
                return option_list

            elif self.input_format_type == 'v':
                message_list = [message_videocodec, message_preset, message_resolution, message_qv, message_crf, message_vol, message_output_fps]
                parameter_list = ['-c:v', '-preset', '-vf', '-q:v', '-crf', '-af', '-r']

            elif self.input_format_type == 'i':
                message_list = [message_input_fps, message_preset, message_resolution, message_qv, message_crf]
                parameter_list = ['-r', '-preset', '-vf', '-q:v', '-crf']

            for index, message in enumerate(message_list):
                parameter = parameter_list[index]
                result = self.option_filter(index, message, parameter)
                if result != None:
                    option_list.extend(result)
            
            return option_list

    def image_related_processor(self, input_format_type: str, output_format_type: str, cmd_list: list, output_filename: str, output_format:str) -> list:
        """
        Summary of the Function:
        If the conversion includes img, no matter input file or output file, this function needed to be run
        1. if it is a video/gif to image process, a txt folder need to be created and cmd list is modified
        2. if it is a image to video/gif process, cmd list is modified

        Parameters:
        input_format_type (str): 'v', 'g', 'i'
        output_format_type (str): 'v', 'g', 'i'
        cmd_list (list)
        output_filename (str)
        output_format (str)

        Returns:
        cmd_list (list)
        
        """
        if  input_format_type != 'i' and output_format_type == 'i': # create a txt folder for video or gif to image 

            if '-r' in cmd_list and '-vf' in cmd_list:
                if input_format_type == 'v':
                    self.image_output_folder = f'video_{self.vf_scale_resolution}_{self.input_fps}fps_{output_filename}_{self.output_format}'
                else:
                    self.image_output_folder = f'gif_{self.vf_scale_resolution}_{self.input_fps}fps_{output_filename}_{self.output_format}'
                    
            else:
                if input_format_type == 'v':
                    self.image_output_folder = f'video_{self.original_resolution}_{self.input_fps}fps_{output_filename}_{self.output_format}'
                else:
                    self.image_output_folder = f'gif_{self.original_resolution}_{self.input_fps}fps_{output_filename}_{self.output_format}'

            if not os.path.exists(self.image_output_folder):
                os.mkdir(self.image_output_folder)
                cmd_list.extend(("-qmin", "1", "-qmax", "1", "-y", os.path.join(self.image_output_folder, f"{self.image_output_folder}%05d.{output_format}")))
            else:
                cmd_list.extend(("-qmin", "1", "-qmax", "1", "-y", os.path.join(self.image_output_folder, f"{self.image_output_folder}%05d.{output_format}")))

        elif input_format_type == 'i' and output_format_type != 'i':

            txtfile = f"{self.input_filename}.txt"

            cmd_list.insert(1, "-f")
            cmd_list.insert(2, "concat")
            input_fps_parameter = cmd_list.pop(5)
            cmd_list.insert(3, input_fps_parameter)
            input_fps = cmd_list.pop(6)
            cmd_list.insert(4, input_fps)
                
            img_folder_path = os.path.join(os.getcwd(), self.img_folder)
            img_txt_path = os.path.join(img_folder_path, txtfile)

            cmd_list[6] = img_txt_path
            if output_format_type == 'v':
                cmd_list.extend(('-pix_fmt', 'yuv420p', "-y", f"{output_filename}.{output_format}"))
            else:
                cmd_list.extend(('-pix_fmt', 'bgr8', "-y", f"{output_filename}.{output_format}"))

            
        return cmd_list
    
    def get_cmd(self) -> list:
        """
        Summary of the Function:
        The main body of this audio and video converter.
        1. Check and get input file format and its name.
        2. Check and get output file format and its name.
        3. Choose desired option for the cmd.

        Parameters:
        self.option_organizer (Func)
        self.remove_video (Func)

        Returns:
        cmd_list (list): a list of command for ffmpeg process 

        """

        valid_file, input_format_type = self.get_input_format_and_filename()    

        if input_format_type == 'v' or input_format_type == 'g' :
            self.original_video_gif_fps()

        output_filename = self.get_output_filename()

        output_format, output_format_type = self.get_output_container()

        if os.path.exists(os.path.join(os.getcwd(), f'{output_filename}.{output_format}')):
            print('Same file existed')
            exit()

        cmd_list = [self.ffmpeg, "-i", valid_file]
        cmd_list.extend(self.option_organizer())

        if  input_format_type != 'i' and output_format_type == 'i' or input_format_type == 'i' and output_format_type != 'i':
            self.image_related_processor(input_format_type, output_format_type, cmd_list, output_filename, output_format)
        
        else:
            cmd_list.extend(("-y", f"{output_filename}.{output_format}"))

        print(cmd_list)    
        return cmd_list

    
def main():
    convert = Converter()
    def ffmpeg(cmd):
        """
        Summary of the Function:
        Convert a audio/video format to another audio/video format

        Parameters:
        convert.get_cmd() (Func): cmd (list)  
         
        Returns:
        the converted output file
        
        """
        if subprocess.run(cmd).returncode == 0:
            print ("Script ran successfully")
        else:
            print ("There was an error running your script")

        if convert.input_format_type != 'i':
            if convert.output_format_type == 'i':
                
                image_output_folder_path = os.path.join(os.getcwd(), convert.image_output_folder)
                output_txt_path = os.path.join(image_output_folder_path, f'{convert.input_filename}.txt')
                file_list = os.listdir(image_output_folder_path)

                with open(output_txt_path, "w") as txt_file:
                    for file in file_list:
                        if file.lower().endswith(f'.{convert.output_format}'):
                            txt_file.write(f"file '{file}'\n")
                            txt_file.write("duration 0.2\n")
                            
        
    ffmpeg(convert.get_cmd())

if __name__=='__main__':
    main()

    

    




