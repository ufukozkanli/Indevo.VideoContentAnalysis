base_path="/media/data/projects/protekBase/test/"
set_folder="hkt" #"breifcam" 
video_path=base_path+"dataset/hamKayit/video_draft.mp4" #"dataset/breifcam.mp4" 




file_track_path=base_path+"results/{}/objects.csv".format(set_folder)
out_video_path=base_path+"results/{}/out.mp4".format(set_folder)

out_bg_img=base_path+"results/{}/bg_mog.jpg".format(set_folder)

out_tracks_new_path=base_path+"results/{}/data_process.txt".format(set_folder)
out_tracks_path=base_path+"results/{0}/objects.csv".format(set_folder)

import csv


#Create file and add header
def start():
    global wr    
    header_data=["x1", "y1", "x2", "y2","tracking_id", "index","n"]
    with open(out_tracks_path, 'w') as fp:
        pass
    _write_row(header_data)

def _write_row(row_data):
    with open(out_tracks_path, 'a+', newline='',encoding="utf-8") as fp:
        wr = csv.writer(fp, quoting=csv.QUOTE_ALL)
        wr.writerow(row_data)

#Save  to File 
def save(row_items): 
    global wr
  
    #items
    #box_item=bbox.tolist() + [tracking_id, index,n]
    _write_row(row_items)