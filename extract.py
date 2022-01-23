from src.frame_extract import FrameExtract


input_dir = './input/' #Directory that contains the videos, you
                        #want to extract frames
destination_dir = './output/' #destination directory where extracted frames
                                # will be stored. For each video it will create
                                # separate subfolder by each video's name
dim = (224,224) #optional

FrameExtract(input_dir,destination_dir,dim)
