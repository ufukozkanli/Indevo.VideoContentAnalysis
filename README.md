> This repository implements Video Synopsis 
### Steps
1. Object Tagging from Video
	1. based on (https://github.com/anushkadhiman/ObjectTracking-DeepSORT-YOLOv3-TF2) repository
2. Summarization of Video from Tag Data
	1. Method 1 Based on (https://github.com/lerker/OpenSourceVS)
	2. Method 2 Custom with (https://github.com/ufukozkanli/Indevo.VideoContentAnalysis/blob/main/codes/extent/embed/video_summary.py)

# 1. Video Özetleme
> Video özeti (Video synopsis), uzun bir videonun kısa bir video özetini oluşturmak için bir yaklaşımdır. Hareketli nesneler (kişi,araç,vs..) izlenir , analiz edilir ve video akışları nesneler ve etkinliklerden oluşan bir veriye dönüştürülür.  
Teknolojide video gözetimi (video surveillance) alanında bir çok özel uygulamalar vardır. CCTV (kapalı devre televizyon) kameralarının kullanımındaki artışa rağmen, kaydedilen görüntülerin özetlenmesi hala maliyetli , emek ve zaman yoğun bir iştir.

![Fig1](https://i.ibb.co/Wpn3HhL/image.png)

*Fig. Video Özeti Kavramsal*

# 2 Application Use Cases
1. Video Kaydı Yapmak (DVR-NVR)
	1. Kamera, işlemci birimi ve depolama aygıtı ile görüntü kaydı yapmak/saklamak(lokal sunucu)
		1. 7 gün boyunca depolama
		2. Kayıtları internet üzerinden canlı izleyebilmek
2. Videodaki insan faaliyetleri için video özetleme ve loglama (Video Synopsis)
	1. Kişi Takibi
		1. Kişileri Her framede Tagleme (ID)
		2. Kişileri frameler arası ID ile ayırlabilme
	2. ID’li kişilerin kayıtta girişten çıkışa kadar ki yerini ve zamanını tespit etmek ve loglamak
		1. Örn: A kişisi  t zamanından t+x zamanına kadar video içerisinde X,Y pixel karesinde gibi..
	3. Video olarak özetleyebilmek ([Örnek Video Özeti Çalışması](https://www.youtube.com/watch?v=oezU4SkQFkU&ab_channel=BriefCam))
  
![Fig2](https://i.ibb.co/52pxM1B/image.png)

*Fig. Sample Summary*

## 1.2. Method
### Modules
 1. Object Tagging & Tracking
 2. Data Generation & Interpration
 3. Summary Video Generation

### Used Libraries
1. [Yolo] (https://github.com/pjreddie/darknet) 
2. [OpenCV] (https://github.com/opencv/opencv)
3. [Deep Sort] (https://github.com/nwojke/deep_sort)
4. [Summary and Video Generation] (https://github.com/lerker/OpenSourceVS)

### Future Works
- [ ] Performance Improvements (Near Real Time Summarization)
	1. YoloV3->YoloV4
	2. Optimum object selection in time series for summary
- [ ] Video Summary Application Development
	1. Video Area Restriction
	2. Video Summary Database Operations
- [ ] Cloud Service Development

## References
1.  Example Videos
	1. [BriefCam Syndex Pro - Review, Research, Respond](https://www.youtube.com/watch?v=oezU4SkQFkU)
	2. [BriefCam for business: Who's clocking out early at BriefCam](https://www.youtube.com/watch?v=lHhqFEeDk08&list=PLWqMrMMWGxu4EVTJx3LWFZuztpii0clhD)
	3. [BriefCam - shoe department - full Video Synopsis](https://www.youtube.com/watch?v=kFViLl9rDC0&list=PLWqMrMMWGxu6BA9DcOkO604IA-TUtuxLK)
2.  Example Products
	1. [https://www.proficomms.cz/files/datasheets/Kedacom/KEDACOM%20-%20Technology%20Brief%20-%20Recognitive%20NVR%20(v2.3)%20BF.pdf](https://www.proficomms.cz/files/datasheets/Kedacom/KEDACOM%20-%20Technology%20Brief%20-%20Recognitive%20NVR%20(v2.3)%20BF.pdf)
	2. [https://www.mistralsolutions.com/articles/video-synopsis-use-video-surveillance/](https://www.mistralsolutions.com/articles/video-synopsis-use-video-surveillance/)
	3. [https://www.genetec.com/solutions/resources/briefcam-video-synopsis-technology-and-security-center-integration](https://www.genetec.com/solutions/resources/briefcam-video-synopsis-technology-and-security-center-integration)  
	4. [https://www.convergint.com/app_category/video-synopsis/](https://www.convergint.com/app_category/video-synopsis/)
3.  Patents
	1. [https://patents.google.com/patent/US8311277B2/en](https://patents.google.com/patent/US8311277B2/en)  
	2. [https://patents.google.com/patent/US8787730](https://patents.google.com/patent/US8787730)

4. Object Tagging & Tracking
	1. https://medium.com/analytics-vidhya/object-tracking-using-deepsort-in-tensorflow-2-ec013a2eeb4f
		1. https://github.com/anushkadhiman/ObjectTracking-DeepSORT-YOLOv3-TF2
		2. [CoLab Sample](https://colab.research.google.com/drive/1GYuZ8GKEzrKHuA-hRQzA_K1ZgCWKrHWp#scrollTo=53NkVCGue5Uo)
	2. https://github.com/LeonLok/Deep-SORT-YOLOv4
	3. [https://github.com/kevinvincent/DimensionFour](https://github.com/kevinvincent/DimensionFour)

5. Others
	 1. [https://github.com/search?o=desc&q=video+synopsis&s=stars&type=Repositories](https://github.com/search?o=desc&q=video+synopsis&s=stars&type=Repositories)
