📘Project Overview 

This project aims for partitioning an image and then compressing it based on the concept of Region of Interest (ROI). The key idea is to divide an image into important and less important parts ,for example, in medical images, the area containing the organ or disease is more important than the background of the image. The important region which is the ROI is compressed without any loss of information, while the remaining part which is the non ROI segment, is compressed more strongly in order to save space. This method helps in reducing image size for efficient and fast storage and compression, which is especially useful in fields like telemedicine, where images are to be shared over limited bandwidth but demands high accuracy in critical areas.


📊Expected Outcomes 

The project expects to create a program that will be capable of performing region-based image compression. Once the input image is given, the program will identify segment regions of interests and the less significant areas. The ROI regions will retain high fidelity, and the  non ROI (less significant regions) regions will undergo higher compression to achieve the goal of optimal storage reduction.The results will aim to show that the program can make images smaller without affecting the quality of the important regions, even if the compression is high. The project will include the code, image of examination, the output results, and weekly progress updates.
