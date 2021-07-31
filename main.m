clc; close all;

prueba=imread('baseimages/Capture4.PNG');
figure,imshow(prueba)
d = imdistline;
%33.12


pruebagris=rgb2gray(prueba);%escala de grises
figure,imshow(pruebagris)

pruebabin=imbinarized(prueba); %binarizada
figure,imshow(pruebabin)


