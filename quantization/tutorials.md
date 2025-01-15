# PTQ Pipeline
## Range Setting Methods
With a set of FP numbers, Choose an FP range, the outliers will be clipped to bound.
+ Min-Max: The range is set to \[FP<sub>min</sub>, FP<sub>max</sub>\], no FP numbers will be clipped.
+ MSE: To alleviate the issue of outliers, MSE range setting method find the range \[q<sub>min</sub>, q<sub>max</sub>\] which minimize the MSE between original FP tensor V<sub>orig</sub> and quantized 