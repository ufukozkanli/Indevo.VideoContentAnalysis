import csv
import numpy as np
import cv2

import tracker_save as ts


def main():
    
    with open(ts.file_track_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        
        rows=list(spamreader)
        rows_data=rows[1:]
        header=rows[0]
        print(header)        
        x = np.array(rows_data)                
        ar_track = x.astype(np.float)
        print(ar_track[0])
    
    if ar_track is  None:
        return
    
    #Find Total Different Object Count
    ar_col_obj_id=np.array(ar_track[:,4],dtype=np.int32)
    #print("obj_id",ar_col_obj_id)
    max_val=np.amax(ar_col_obj_id,axis=0)
    print("Object Count",max_val)
    
    
    #ar_track=np.append(ar_track,np.zeros((ar_track.shape[0],1)),axis=1)
    #print(ar_new_track.shape)
    
    #o2=ar_new_track[ar_new_track[:,4]==2]
    #print(o2)
    get_frm(ar_track)

def get_frm(ar_track):
    dic_data={}
    ar_res=[]
    row_count=ar_track.shape[0]
    for i in range(row_count):    
        row=ar_track[i,:]
        #print(row)
        
        coor = np.array(row[:4], dtype=np.int32)
        (x1, y1), (x2, y2) = (coor[0], coor[1]), (coor[2], coor[3])
        obj_id = int(row[4])
        class_ind = int(row[5]) 
        frame_ind= int(row[6]) 
        
        if not obj_id in dic_data:
            dic_data[obj_id]=1+((obj_id-1)*24)
        else:
            dic_data[obj_id]=dic_data[obj_id]+1
        
        count=dic_data[obj_id]
        ar_res.append(count)
    ar_res=np.array(ar_res)
    ar_res=ar_res.reshape(-1,1)
    #print(ar_track.shape,"->",ar_res.shape)
    ar_new_track=np.append(ar_track,ar_res,axis=1)
    #print(ar_track.shape,"->",ar_new_track.shape)
    #print(ar_new_track[:,6:])
    
    
    np.savetxt(ts.out_tracks_new_path, ar_new_track, delimiter=",")
    ar_new_track=np.genfromtxt(ts.out_tracks_new_path, delimiter=",")
    print(ar_new_track.shape)

def get_nth_frame(frame_number):
    
    video_path   = ts.video_path
    # Detect on video
    vid = cv2.VideoCapture(video_path)
    # By default VideoCapture returns float instead of int
    width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(vid.get(cv2.CAP_PROP_FPS))
    codec = cv2.VideoWriter_fourcc(*'XVID')

    # get total number of frames
    totalFrames = vid.get(cv2.CAP_PROP_FRAME_COUNT)
    
    # check for valid frame number
    if  frame_number >= 0 & frame_number <= totalFrames:
    # set frame position
        vid.set(cv2.CAP_PROP_POS_FRAMES,frame_number)
    
    searchFrame=None
    if vid.isOpened():        
        _, frame = vid.read()    
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        searchFrame=frame
         
    vid.release()
    return searchFrame
#main()
def _get_video_out():
    video_path   = ts.video_path
    vid = cv2.VideoCapture(video_path) # detect on video

    output_path=ts.out_video_path
    # by default VideoCapture returns float instead of int
    width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)) 
    fps = int(vid.get(cv2.CAP_PROP_FPS))
    print("VIDEO PROPERTIES:Width:{}\tHeight:{}\tFps:{}\t".format(width,height,fps))
    codec = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, codec, fps, (width, height)) # output_path must be .mp4

    vid.release()
    return out

def start():
    tracks=np.genfromtxt(ts.out_tracks_new_path, delimiter=",")
    print(tracks.shape)
    
    ar_col_obj_id=np.array(tracks[:,7],dtype=np.int32)
    max_val=np.amax(ar_col_obj_id,axis=0)
    print("Object Count",max_val)

    frame_count=max_val
    vid_out =_get_video_out()
    
    for i in range(frame_count):
        crnt_fr_no=i+1
        
        frame_objs=tracks[tracks[:,7]==crnt_fr_no]
        print("#Frame:{}\tObj:{}".format(crnt_fr_no,frame_objs.shape[0]))

        img=acc_img(frame_objs)        
        #cv2.imwrite("/code2/js/obj_gen/{}.jpg".format(crnt_fr_no),img)
        vid_out.write(img)
    
    vid_out.release()

def acc_img(frm_objs):
    image=get_nth_frame(0)
    image_h, image_w, image_z = image.shape  
    blank_img=cv2.imread(ts.out_bg_img)
    
    for i in range(frm_objs.shape[0]):
        row=frm_objs[i,:]
        coor = np.array(row[:4], dtype=np.int32)
        (x1, y1), (x2, y2)= (coor[0], coor[1]), (coor[2], coor[3])
        (obj_id,class_ind,frame_ind) = ( int(row[4]),int(row[5]),int(row[6]) )
        img=get_obj_img(blank_img,row,frame_ind)
        cv2.imwrite(ts.base_path+"codes/TensorFlow-2.x-YOLOv3/ab123.jpg",img)
        
        
    return blank_img


def get_obj_img(blank_img,row,org_frame_no):
    coor = np.array(row[:4], dtype=np.int32)
    (x1, y1), (x2, y2)= (coor[0], coor[1]), (coor[2], coor[3])
    (obj_id,class_ind,frame_no) = ( int(row[4]),int(row[5]),int(row[6]) )            
    
    image=get_nth_frame(frame_no-1)
    image_h, image_w, image_z = image.shape  
    
    blank_img[y1:y2,x1:x2]=image[y1:y2,x1:x2]
    
    bbox_thick=1
    fontScale = 0.75 * bbox_thick
    Text_colors=(0,0,255) #bgr
    sec=round(org_frame_no/24.0,2)
    label="{} sn".format(sec)
    
    cv2.putText(blank_img, label, (x1, y1-4), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        fontScale, Text_colors, bbox_thick, lineType=cv2.LINE_AA)
    
    return blank_img

main()
start()