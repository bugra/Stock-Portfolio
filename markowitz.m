clear all;close all;clc
load('R.mat'); load('means.mat');
timeIndex = 530;
R(:,:,timeIndex)
e = ones(size(R,1),1);
markowitzWeights = (e' * R(:,:,timeIndex)) / (e' * R(:,:,timeIndex) * e);
display(['Google is (Markowitz)' num2str(markowitzWeights(1))])
display(['Microsoft is (Markowitz)' num2str(markowitzWeights(2))])
display(['Apple is (Markowitz)' num2str(markowitzWeights(3))])
display(['Yahoo  is (Markowitz)' num2str(markowitzWeights(4))])
display(['McDonalds is (Markowitz)' num2str(markowitzWeights(5))])
display(['Coca Cola is (Markowitz)' num2str(markowitzWeights(6))])
display(['Pfizer is (Markowitz)' num2str(markowitzWeights(7))])
display(['Morgan Stanley is (Markowitz)' num2str(markowitzWeights(8))])
meanWeight = (M * R(:,:,timeIndex)) / sum(M * R(:,:,timeIndex) * M') ;
meanWeights = meanWeight / sum(meanWeight);
display(['Google is (Mean Weighted)' num2str(meanWeights(1))])
display(['Microsoft is (Mean Weighted)' num2str(meanWeights(2))])
display(['Apple is (Mean Weighted)' num2str(meanWeights(3))])
display(['Yahoo  is (Mean Weighted)' num2str(meanWeights(4))])
display(['McDonalds is (Mean Weighted)' num2str(meanWeights(5))])
display(['Coca Cola is (Mean Weighted)' num2str(meanWeights(6))])
display(['Pfizer is (Mean Weighted)' num2str(meanWeights(7))])
display(['Morgan Stanley is (Mean Weighted)' num2str(meanWeights(8))])