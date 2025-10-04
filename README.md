## 📘Project Overview 

This project aims for partitioning an image and then compressing it based on the concept of Region of Interest (ROI). The key idea is to divide an image into important and less important parts ,for example, in medical images, the area containing the organ or disease is more important than the background of the image. The important region which is the ROI is compressed without any loss of information, while the remaining part which is the non ROI segment, is compressed more strongly in order to save space. This method helps in reducing image size for efficient and fast storage and compression, which is especially useful in fields like telemedicine, where images are to be shared over limited bandwidth but demands high accuracy in critical areas.

## 🎯Project Objectives 

1. 🖼️ **Image Partitioning:** To divide a medical image into `c` rectangular regions using an efficient image partitioning method.  
2. 🔍 **ROI Preservation:** To ensure that the regions which are more significant (**Region of Interest - ROI**) are retained by **lossless compression**, while the non-ROI regions are compressed via **lossy methods**.  
3. 💾 **Storage & Transmission:** To improve storage capabilities and transmission speed in **DICOM images**, achieving high compression ratios while keeping the diagnostic quality of the original image intact.  
4. ⚡ **Real-time Processing:** To develop a model or framework that can be deployed for **real-time processing** of medical images for storage and transmission using **lossless ROI encoding techniques**.  


## 🏥 Expected Approach

1. 🖼️ Input Image Acquisition:  
Medical images obtained via CT or MRI scans which are in standard Digital Imaging and Communications in Medicine (DICOM) format is used.

2. ✂️ Segmentation:  
The image is segmented into various fragments to only focus on the area of diagnostic importance. This technique may involve use of different clustering techniques.

3. 🔍 Classification:  
Following segmentation, the input image is classified into two major catergories

   1) ROI(Region of Interest) ✅

   2) Non-ROI❌

4. 🧩 Partitioning:  
This is a major step in encoding and compression of image as image is divided in numerous rectangular sections.  
It is perfomed such as to maintain the structural integrity of the image so as to prevent any loss of information from the original input image.

5. 💾 Compression:  
Two different compression techniques will be used for ROI and non-ROI regions.  

   1) ROI regions: Lossless techniques will be employed so as to retain as much information as possible.

   2) Non-ROI regions: Lossy techniques will be used to reduce the size of the file while maintaining the threshold or accepted visual quality of image.

6. 🗂️ Encoding:  
Both the compressed parts would then be converged so as to create the complete image with more focused ROI and reduced storage capacity due to non-ROI.  
This will be helpful for further storage and transmission of image.

7. 🔄 Decompression:  
The final step is decompression of image where in the original image is reconstructed ensuring that ROI is lossless and the image quality is not diminished.



## 📊Expected Outcomes 

The project expects to create a program that will be capable of performing region-based image compression. Once the input image is given, the program will identify segment regions of interests and the less significant areas. The ROI regions will retain high fidelity, and the  non ROI (less significant regions) regions will undergo higher compression to achieve the goal of optimal storage reduction.The results will aim to show that the program can make images smaller without affecting the quality of the important regions, even if the compression is high. The project will include the code, image of examination, the output results, and weekly progress updates.
